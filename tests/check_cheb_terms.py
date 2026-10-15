#!/usr/bin/env python3
"""check_cheb_terms.py -- a standalone check of a b-file of Chebyshev-Carmichael numbers (OEIS A299799).

    python3 check_cheb_terms.py cn2x/runs/cheb_1e25/b299799_1e25.txt

Standard library only; reads nothing but the b-file and recomputes every factorisation by trial division (exact: each
factor removed is prime because all smaller factors are already gone, and the loop stops when d^2 exceeds the remaining
cofactor, which is then prime).  For each term n it checks A299799's definition directly:
  * n is odd, composite and squarefree;
  * Carmichael: p - 1 divides n - 1 for every prime p | n (A002997);
  * Chebyshev: n == 1 or p (mod (p^2 - 1)/2) for every prime p | n (A299799's comment), equivalently n == +-1 (mod p-1)
    and n == +-1 (mod p+1) (A175530's criterion), which is also checked;
and reports which terms are also order-2 Carmichael numbers (A175531: n == 1 or p (mod p^2 - 1) for every p).
"""
import sys


def factor(n):
    f, d = [], 2
    while n > 1:
        if d * d > n:
            f.append(n)
            break
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            f.append(d if e == 1 else (d, e))
        d = 3 if d == 2 else d + 2
    return f


def main():
    rows = [l.split() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
    idx, terms = [int(r[0]) for r in rows], [int(r[1]) for r in rows]
    ok = idx == list(range(1, len(terms) + 1)) and all(a < b for a, b in zip(terms, terms[1:]))
    print(f"{len(terms)} terms; indexed 1..{len(terms)} and strictly increasing: {ok}")
    n_cn2 = 0
    for i, n in zip(idx, terms):
        f = factor(n)
        sq = all(isinstance(p, int) for p in f)
        carm = sq and all((n - 1) % (p - 1) == 0 for p in f)
        cheb = sq and all(n % ((p * p - 1) // 2) in (1 % ((p * p - 1) // 2), p % ((p * p - 1) // 2)) for p in f)
        pm = sq and all((n % (p - 1) in (1 % (p - 1), (p - 2) % (p - 1))) and (n % (p + 1) in (1, p)) for p in f)
        cn2 = sq and all(n % (p * p - 1) in (1, p) for p in f)
        good = n % 2 == 1 and len(f) >= 3 and sq and carm and cheb and pm
        ok &= good
        n_cn2 += cn2
        print(f"a({i}) = {n}  {'OK' if good else 'FAIL'}  {'CN2' if cn2 else 'cheb only'}  = {' * '.join(map(str, f))}")
    print(f"\n{'ALL TERMS SATISFY THE DEFINITION' if ok else 'FAILED'}; {n_cn2} are also order-2 Carmichael numbers (A175531)")
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
