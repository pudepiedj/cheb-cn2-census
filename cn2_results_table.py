#!/usr/bin/env python3
"""cn2_results_table.py -- one wide line per term of a verified run: index, n, log10, k, p_sw, p_k-1, pmax, gap, class,
where each term is already known, and the prime factors.

    python3 cn2_results_table.py --dir cn2x/runs/cheb_1e28 [--oeis cn2x/runs/cheb_1e25/A299799_oeis.json]
                                 [--reference cn2x/runs/cheb_1e28/reference_cheb_1e28.json] [--out TABLE.txt]

Reads <dir>/result.json (written by cn2_split_campaign.py verify).  The class is judged against Howe's order-2 definition
(mod p^2 - 1) whatever the run's mode:
  CN2           n == 1 (mod p^2 - 1) at every prime p | n  (rigid order-2; also a Chebyshev number)
  CN2 type-p q  order 2, with n == q (mod q^2 - 1) at the listed primes
  cheb only     Chebyshev-Carmichael but not order 2; 'halfway at' lists the primes where n is half way round p^2 - 1,
                n == 1 + (p^2-1)/2 or p + (p^2-1)/2 (mod p^2 - 1)
'known' is: OEIS (in the sequence's DATA when --oeis is given), A175531 (an order-2 term in the --reference list), ref
(another term in the --reference list), or NEW.
On a terminal, cheb-only lines are yellow and NEW lines bold; piped, written through tee, with NO_COLOR, or to --out the
text is plain.
"""
import argparse, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sympy import factorint      # noqa: E402


def load(path):
    if not path:
        return set()
    if path.endswith('.json'):
        d = json.load(open(path))
        return {int(v) for v in (d['found'] if isinstance(d, dict) else d)}
    return {int(l.split()[1]) for l in open(path) if l.strip() and not l.startswith('#')}


def klass(n, ps):
    if all(n % (p * p - 1) in (1, p) for p in ps):
        tp = [p for p in ps if n % (p * p - 1) != 1]
        return ('CN2' if not tp else 'CN2 type-p ' + ','.join(map(str, tp))), ''
    return 'cheb only', ','.join(str(p) for p in ps if n % (p * p - 1) not in (1, p))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir', required=True)
    ap.add_argument('--oeis')
    ap.add_argument('--reference')
    ap.add_argument('--out')
    a = ap.parse_args()
    r = json.load(open(os.path.join(a.dir, 'result.json')))
    X, mode = int(r['X']), r['mode']
    oeis, ref = load(a.oeis), load(a.reference)
    found = sorted(int(v) for v in r['found'])
    sw = r.get('switch_prime', {})
    rows, counts = [], {}
    for i, n in enumerate(found, 1):
        ps = sorted(factorint(n))
        c, half = klass(n, ps)
        counts[c.split()[0] if c.startswith('CN2') else c] = counts.get(c.split()[0] if c.startswith('CN2') else c, 0) + 1
        known = 'OEIS' if n in oeis else ('A175531' if c.startswith('CN2') else 'ref') if n in ref else 'NEW'
        s = sw.get(str(n))
        rows.append((c, known, f"{i:>3} {n:>29} {math.log10(n):>7.3f} {len(ps):>3} {(s if s else '-')!s:>6} {ps[-2]:>7} "
                                 f"{ps[-1]:>8} {ps[-1] / ps[-2]:>6.1f}  {c:<10} {half:<16} {known:<7} "
                                 + ' * '.join(map(str, ps))))
    head = (f"{'i':>3} {'n':>29} {'log10':>7} {'k':>3} {'p_sw':>6} {'p_k-1':>7} {'pmax':>8} {'gap':>6}  {'class':<10} "
            f"{'halfway at':<16} {'known':<7} prime factors")
    title = (f"{a.dir}: mode {mode}, X = 10^{round(math.log10(X))}; {len(found)} terms: "
             + ', '.join(f"{v} {k}" for k, v in sorted(counts.items())))
    if a.out:
        with open(a.out, 'w') as fh:
            fh.write(title + '\n' + head + '\n' + '\n'.join(t for _, _, t in rows) + '\n')
        print(f"wrote {a.out}")
        return
    color = sys.stdout.isatty() and not os.environ.get('NO_COLOR')
    YEL, BOLD, OFF = ('\033[33m', '\033[1m', '\033[0m') if color else ('', '', '')
    print(title)
    print(head)
    for c, known, t in rows:
        c0 = (YEL if c == 'cheb only' else '') + (BOLD if known == 'NEW' else '')
        print(f"{c0}{t}{OFF if c0 else ''}")


if __name__ == '__main__':
    main()
