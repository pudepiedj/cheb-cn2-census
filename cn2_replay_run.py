#!/usr/bin/env python3
"""cn2_replay_run.py -- replay sampled shards of a certification run directory, alone and single-threaded.

    python3 cn2_replay_run.py --dir cn2x/runs/cheb_1e25 --T 7000 --qstar 5500000
                              [--capped 100] [--weighted 30] [--pair 60] [--tail 30] [--procs 30] [--seed 2026]

The general form of tests/replay_shards.py in carmichael-order2-census-2.  For a run directory laid out as
DIR/{split.json, capped/, pair/, tail/} (capped from cn2_split_campaign.py init --capped-only --lastcalc; pair/ and tail/
holding cn2pair and cn2tail), it re-runs randomly chosen shards with the run's OWN frozen binaries.  Each engine skips
every shard named in its done.log, so a fresh directory whose done.log names every OTHER shard makes the engine run just
one shard, on ONE thread (no concurrency, no donation); its counters must equal the production record exactly.
--weighted adds capped shards sampled in proportion to their node counts (donation happens in the heavy ones).
The mode (rigid/howe/cheb) and X come from split.json; T and q* are the pair/tail parameters the run used.
"""
import argparse, json, os, random, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor


def records(path, nf):
    out = {}
    for l in open(path):
        t = l.split()
        if len(t) == nf + 2 and t[0] == 'D':
            out.setdefault(int(t[1]), t[2:])
    return out


def replay(exe, args_fn, env, sid, n, nf, tmp, tag):
    d = os.path.join(tmp, f"{tag}_{sid}")
    os.mkdir(d)
    z = ' '.join('0' * nf)
    with open(os.path.join(d, 'done.log'), 'w') as fh:
        for i in range(n):
            if i != sid:
                fh.write(f"D {i} {z}\n")
    t0 = time.time()
    subprocess.run([exe] + args_fn(d), env=env, capture_output=True, text=True)
    new = [l.split()[2:] for l in open(os.path.join(d, 'done.log')) if l.split()[:2] == ['D', str(sid)]]
    return sid, (new[-1] if new else None), time.time() - t0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir', required=True); ap.add_argument('--T', type=int, required=True)
    ap.add_argument('--qstar', type=int, required=True)
    ap.add_argument('--capped', type=int, default=100); ap.add_argument('--weighted', type=int, default=30)
    ap.add_argument('--pair', type=int, default=60); ap.add_argument('--tail', type=int, default=30)
    ap.add_argument('--procs', type=int, default=30); ap.add_argument('--seed', type=int, default=2026)
    a = ap.parse_args()
    D = os.path.abspath(a.dir)
    sp = json.load(open(os.path.join(D, 'split.json')))
    X, mode = sp['X'], sp['mode']
    env = dict(os.environ, CN2X_MODE=mode)
    for k in ('CN2X_LASTCALC', 'CN2X_SKIP_PRIMES', 'CN2X_TCAP', 'CN2X_NMIN'):
        env.pop(k, None)
    spec = [
        ('capped', os.path.join(D, 'capped', 'cn2xh'), 9, os.path.join(D, 'capped', 'done.log'),
         lambda d: [X, d, '1', '0', str(sp['ratio']), str(sp['sieve']), str(sp['mshard']), str(sp['batch']),
                    str(sp['donate_q']), '0', '0'],
         dict(env, CN2X_TCAP=str(sp['R0']), **({'CN2X_LASTCALC': '1'} if sp.get('lastcalc') else {}))),
        ('pair', os.path.join(D, 'pair', 'cn2pair'), 6, os.path.join(D, 'pair', 'done.log'), None, env),
        ('tail', os.path.join(D, 'tail', 'cn2tail'), 4, os.path.join(D, 'tail', 'done.log'),
         lambda d: [X, str(a.qstar), d, '1', '0', str(sp['W']), '0', str(sp['nsmall'])], env),
    ]
    rnd = random.Random(a.seed)
    fails = 0
    with tempfile.TemporaryDirectory() as tmp:
        for tag, exe, nf, log, args_fn, e in spec:
            prod = records(log, nf)
            n = len(prod)
            assert sorted(prod) == list(range(n)), f"{tag}: done.log is not shards 0..{n - 1}"
            if tag == 'pair':
                ns = n
                args_fn = lambda d, ns=ns: [X, str(a.T), str(a.qstar), d, '1', '0', str(ns), '0', '0']
            plans = []
            if tag == 'capped':
                plans.append(('uniform', sorted(rnd.sample(range(n), min(a.capped, n)))))
                if a.weighted:
                    keys = sorted(range(n), key=lambda i: rnd.random() ** (1.0 / max(int(prod[i][0]), 1e-9)), reverse=True)
                    plans.append(('weighted', sorted(keys[:a.weighted])))
            else:
                plans.append(('uniform', sorted(rnd.sample(range(n), min(a.pair if tag == 'pair' else a.tail, n)))))
            tot = sum(int(v[0]) for v in prod.values()) or 1
            for kind, sample in plans:
                t0 = time.time()
                with ThreadPoolExecutor(a.procs) as ex:
                    res = list(ex.map(lambda s: replay(exe, args_fn, e, s, n, nf, tmp, f"{tag}{kind}"), sample))
                bad = [(s, prod[s], g) for s, g, _ in res if g != prod[s]]
                fails += len(bad)
                share = sum(int(prod[s][0]) for s in sample) / tot
                print(f"[{'PASS' if not bad else 'FAIL'}] {tag} ({kind}): {len(sample)} of {n:,} shards replayed alone on one "
                      f"thread; counters identical for {len(sample) - len(bad)}  ({time.time() - t0:.0f} s; sample holds "
                      f"{share:.2%} of the work)", flush=True)
                for s, p, g in bad[:10]:
                    print(f"    shard {s}: production {p}, replay {g}")
    print('ALL PASS' if not fails else f"FAILED: {fails} shards differ")
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
