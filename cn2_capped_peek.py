#!/usr/bin/env python3
"""cn2_capped_peek.py -- look at what a capped cn2xh run (campaign directory) has found so far, by smallest prime.

    python3 cn2_capped_peek.py --dir cn2x/runs/cert_1e28_T15e3 [--roots 5 7 11 13] [--reference results/b175531.txt] [--procs 4]

Reads <dir>/capped/out.txt (H = direct hits, S = LIST/LASTCALC survivors still to factor), verifies the survivors whose
smallest prime is one of --roots (all roots if omitted), and lists the order-2 numbers below X found for each root,
against the reference list if given.  Safe while the run is going: a half-written last line is skipped.  A root's list is
final only once the run has moved past that root (the progress line's "root i/N").
"""
import argparse, json, os, sys
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cn2_order2_defs import verify_candidate, load_reference   # noqa: E402
from sympy import factorint, primerange            # noqa: E402


def smallest_prime(m, plist):
    for p in plist:
        if m % p == 0:
            return p
    return min(factorint(m))


def klass(n, f):
    """class of a verified find, judged against Howe's order-2 definition (mod p^2-1) whatever the run's mode.
    'cheb only' names the primes where n is halfway round p^2-1 (n == r + (p^2-1)/2, r = 1 or p)."""
    ps = sorted(f)
    if all(n % (p * p - 1) in (1, p) for p in ps):
        tp = [p for p in ps if n % (p * p - 1) != 1]
        return 'CN2 rigid' if not tp else 'CN2 type-p ' + ','.join(map(str, tp))
    return 'cheb only (halfway at ' + ','.join(str(p) for p in ps if n % (p * p - 1) not in (1, p)) + ')'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir', required=True)
    ap.add_argument('--roots', type=int, nargs='*')
    ap.add_argument('--reference')
    ap.add_argument('--procs', type=int, default=4)
    a = ap.parse_args()
    p = json.load(open(os.path.join(a.dir, 'split.json')))
    X, mode = int(p['X']), p.get('mode', 'howe')
    plist = list(primerange(5, 1000))
    jobs = []
    for l in open(os.path.join(a.dir, 'capped', 'out.txt')):
        if not l.endswith('\n'):
            continue
        t = l.split()
        if len(t) == 2 and t[0] == 'H' and t[1].isdigit():
            m, s = int(t[1]), 1
        elif len(t) == 5 and t[0] == 'S' and t[1].isdigit() and t[4].isdigit():
            m, s = int(t[1]), int(t[4])
        else:
            continue
        r = smallest_prime(m, plist)
        if a.roots is None or r in a.roots:
            jobs.append((m, s, mode))
    with Pool(a.procs) as pl:
        got = sorted({n for n in pl.imap_unordered(verify_candidate, jobs, chunksize=512) if n is not None and n < X})
    color = sys.stdout.isatty() and not os.environ.get('NO_COLOR')       # never colour output piped or written through tee
    YEL, BOLD, OFF = ('\033[33m', '\033[1m', '\033[0m') if color else ('', '', '')
    by = {}
    for n in got:
        by.setdefault(min(factorint(n)), []).append(n)
    ref = None
    if a.reference:
        ref = [n for n in load_reference(a.reference) if n < X]
    roots = a.roots if a.roots is not None else sorted(set(by) | ({min(factorint(n)) for n in ref} if ref else set()))
    print(f"{a.dir}: X = {X:.0e}, mode {mode}; survivors checked {len(jobs):,}; {'terms' if mode == 'cheb' else 'order-2 numbers'} found {len(got)}"
          + (" (cheb mode: each find is classed CN2 or cheb only against mod p^2-1)" if mode == "cheb" else ""))
    for r in roots:
        have = by.get(r, [])
        line = f"  smallest prime {r:>4}: found {len(have)}"
        if ref is not None:
            want = sorted(n for n in ref if min(factorint(n)) == r)
            line += f" of {len(want)} known" + (f"; NEW {[str(n) for n in sorted(set(have) - set(want))]}" if set(have) - set(want) else "")
        print(line)
        for n in have:
            f = factorint(n)
            c = klass(n, f)
            new = ref is not None and n not in ref
            flag = ('   *** NEW ORDER-2 (CN2) NUMBER ***' if new and c.startswith('CN2') else '   NEW' if new else '')
            c0 = (YEL if c.startswith('cheb') else '') + (BOLD if new else '')   # yellow = cheb only, bold = NEW
            print(f"{c0}      {n}  ({n:.4e})  {c}{flag}{OFF if c0 else ''}")
            print(f"          = {' * '.join(map(str, sorted(f)))}")


if __name__ == '__main__':
    main()
