---
location: post
title: Certified Chebyshev Census Below 10^25
author: Claude Opus 5.5 and JCP
date: 2026-10-13
---

# Certificate: the Chebyshev–Carmichael numbers below $10^{25}$

**Date:** 13 October 2026 (runs the same day)
**Definition:** OEIS A299799, Carmichael numbers that are Chebyshev pseudoprimes: odd composite $n$ with $n \equiv 1$ or $p \pmod{(p^2-1)/2}$ for every prime $p \mid n$. Equivalently (A175530's criterion, with Carmichael's condition), $n$ is squarefree, $p-1 \mid n-1$, and $n \equiv \pm 1$ modulo both $p-1$ and $p+1$, for every $p \mid n$.
**Status:** the computations are complete and every check below passes. The result uses the engines and proofs of the order-2 certificate (the order-2 certificate ([carmichael-order2-census-2](https://github.com/pudepiedj/carmichael-order2-census-2), `docs/CN2_Certificate_1e28.md`)) unchanged, in their $D = 2$ ("cheb") mode.
**Run directory:** `results/cert_1e25/` (the validation run to $10^{22}$ is in a validation run (not included))

---

## 1. The result

> **There are exactly 26 Chebyshev–Carmichael numbers (A299799) below $10^{25}$** (§4). No assumption is made about table caps or switch primes.

A299799 has listed 12 terms, with the comment "No other terms below 10^22". This census confirms those 12, and adds **14 new terms** in $[10^{22}, 10^{25})$:
- **6 that are Chebyshev numbers but not order-2 Carmichael numbers**, none of which appears anywhere in OEIS: about $1.94\times10^{23}$, $6.24\times10^{23}$, $1.33\times10^{24}$, $1.46\times10^{24}$, $3.46\times10^{24}$ and $4.81\times10^{24}$;
- **8 order-2 Carmichael numbers**, a(7)–a(14) of A175531. Every order-2 Carmichael number is a Chebyshev number, since $(p^2-1)/2$ divides $p^2-1$, but these had not been added to A299799.

The 26 are 14 order-2 Carmichael numbers (exactly A175531 below $10^{25}$, all rigid) and 12 Chebyshev-only numbers. Unlike the order-2 numbers, which skip decades 22 and 23, the Chebyshev numbers include two in decade 23.

## 2. Why the order-2 engines and proofs apply

The three engines take the modulus $g(p) = (p^2-1)/D$ as a parameter: $D = 1$ for Howe's order-2 numbers, $D = 2$ here. With $D = 2$ they search exactly the A299799 condition. Both proofs are written for general $D \in \lbrace 1, 2\rbrace$, and each fact they use holds for $D = 2$:
- **F1:** $n$ is odd and $3 \nmid n$, since $(q^2-1)/2$ is still even and divisible by 3;
- **F2:** $n/p > g(p)$, since $(p^2-1)/2 > p$ for $p \ge 5$;
- **F3:** $n$ has at least three primes;
- **F4:** the role bounds, including the strict last-prime bound ($2m = t^2$ is impossible for odd $t$);
- **F5:** the admissibility facts;
- **F6:** Chebyshev numbers are Carmichael numbers, since $p-1 \mid (p-1)(p+1)/2$.

The search is split exactly as in the order-2 certificate:

| part | which $n$ | engine |
|---|---|---|
| capped | $p_{k-1} \le T = 7{,}000$ | `cn2xh`, `CN2X_MODE=cheb`, `CN2X_TCAP=7000`, `CN2X_LASTCALC=1` |
| pair tail | $p_{k-1} > T$ and $p_k \le q^* = 5{,}500{,}000$ | `cn2pair`, cheb mode |
| $(q,a)$ tail | a prime above $q^*$ | `cn2tail`, cheb mode, $R_0 = q^*$ |

## 3. The runs

All six engine files have the same sha256 as those of the order-2 certificate (recorded in `ENGINES.sha256` and rechecked after the runs):

| | pair tail | $(q,a)$ tail | capped |
|---|---|---|---|
| shards | 4,096 / 4,096 | 154 / 154 | 214,135 / 214,135 |
| completion record | `"complete":true`, mode 2 | `"complete":true`, mode 2 | `"complete":true`, mode 2, `"lastcalc":1`, `skipmask 0` |
| work | $7.2\times10^{10}$ pairs; $2.02\times10^{10}$ candidates (equal to the dry count) | $4.13\times10^{10}$ tests | $1.29\times10^{11}$ nodes |
| Fermat survivors | 15,035 | 91 | 767,985 |
| numbers below $X$ | 2 | 0 | 26 |
| time (30 threads) | 20 min | 6 min | 39 min |

**Verification.**
- **The capped half:** `cn2_split_campaign.py verify --dir results/cert_1e25` (`result.json`) finds 26 numbers, with phase consistency OK.
- **The tail:** `cn2_tail_verify.py --X 1e25 --mode cheb … --T 7000` gives **PASS**. It finds exactly the two numbers whose second-largest prime exceeds $T$ (terms 18 and 19 below), and nothing else.
- **The union** of the two halves is the 26 terms.

No `UNPROVEN-PRIMALITY` flag was raised.

## 4. The 26 terms

"Guaranteed by" names the part whose theorem covers the term. The capped run also found terms 18 and 19 through LIST. The b-file is `results/cert_1e25/b299799_1e25.txt`.

| # | $n$ | $\log_{10} n$ | $k$ | prime factors | class | in A299799 before? | guaranteed by |
|---|---|---|---|---|---|---|---|
| 1 | 443372888629441 | 14.65 | 8 | 17 · 31 · 41 · 43 · 89 · 97 · 167 · 331 | CN2 (rigid) | yes | capped |
| 2 | 582920080863121 | 14.77 | 7 | 41 · 53 · 79 · 103 · 239 · 271 · 509 | **cheb only** | yes | capped |
| 3 | 39671149333495681 | 16.60 | 9 | 17 · 37 · 41 · 71 · 79 · 97 · 113 · 131 · 191 | CN2 (rigid) | yes | capped |
| 4 | 842526563598720001 | 17.93 | 8 | 17 · 61 · 71 · 89 · 197 · 311 · 769 · 2729 | CN2 (rigid) | yes | capped |
| 5 | 2380296518909971201 | 18.38 | 9 | 19 · 41 · 43 · 71 · 89 · 127 · 199 · 449 · 991 | CN2 (rigid) | yes | capped |
| 6 | 3188618003602886401 | 18.50 | 8 | 29 · 37 · 79 · 181 · 191 · 449 · 701 · 3457 | CN2 (rigid) | yes | capped |
| 7 | 33711266676317630401 | 19.53 | 9 | 17 · 29 · 37 · 41 · 151 · 199 · 449 · 571 · 5851 | **cheb only** | yes | capped |
| 8 | 54764632857801026161 | 19.74 | 9 | 41 · 53 · 79 · 137 · 139 · 181 · 239 · 271 · 1429 | **cheb only** | yes | capped |
| 9 | 122762671289519184001 | 20.09 | 11 | 13 · 17 · 19 · 29 · 41 · 89 · 97 · 127 · 199 · 251 · 449 | **cheb only** | yes | capped |
| 10 | 361266866679292635601 | 20.56 | 11 | 17 · 23 · 29 · 37 · 41 · 43 · 61 · 109 · 199 · 419 · 881 | **cheb only** | yes | capped |
| 11 | 4208895375600667752001 | 21.62 | 10 | 17 · 29 · 31 · 43 · 71 · 79 · 199 · 389 · 2521 · 5851 | CN2 (rigid) | yes | capped |
| 12 | 7673096805497432749441 | 21.88 | 10 | 29 · 31 · 37 · 43 · 53 · 109 · 127 · 571 · 3079 · 4159 | **cheb only** | yes | capped |
| 13 | 193966598206145637873001 | 23.29 | 11 | 19 · 23 · 29 · 41 · 71 · 89 · 101 · 103 · 701 · 1429 · 5669 | **cheb only** | **new** | capped |
| 14 | 623655451404913888200241 | 23.79 | 9 | 23 · 79 · 109 · 239 · 881 · 883 · 1223 · 1973 · 7019 | **cheb only** | **new** | capped |
| 15 | 1159954316194989017102401 | 24.06 | 9 | 31 · 47 · 109 · 137 · 307 · 2927 · 3079 · 4049 · 4759 | CN2 (rigid) | **new** | capped |
| 16 | 1327183446436495124400001 | 24.12 | 11 | 13 · 17 · 23 · 29 · 89 · 97 · 251 · 449 · 641 · 1499 · 9631 | **cheb only** | **new** | capped |
| 17 | 1457044155748208447259841 | 24.16 | 10 | 79 · 97 · 131 · 139 · 191 · 229 · 379 · 461 · 571 · 2393 | **cheb only** | **new** | capped |
| 18 | 2088144166339753513992001 | 24.32 | 8 | 113 · 199 · 239 · 263 · 701 · 7919 · 15391 · 17291 | CN2 (rigid) | **new** | tail |
| 19 | 2196407820059694924883201 | 24.34 | 9 | 53 · 109 · 127 · 281 · 307 · 379 · 647 · 10529 · 13441 | CN2 (rigid) | **new** | tail |
| 20 | 3339611018825185787482801 | 24.52 | 12 | 19 · 41 · 43 · 53 · 67 · 89 · 103 · 131 · 137 · 307 · 389 · 1429 | CN2 (rigid) | **new** | capped |
| 21 | 3464334205088776324905601 | 24.54 | 12 | 17 · 31 · 37 · 41 · 43 · 59 · 113 · 181 · 199 · 233 · 521 · 3457 | **cheb only** | **new** | capped |
| 22 | 4105879060352839139462401 | 24.61 | 8 | 89 · 239 · 401 · 2143 · 2311 · 3571 · 3761 · 7237 | CN2 (rigid) | **new** | capped |
| 23 | 4809665063400557951190601 | 24.68 | 10 | 41 · 53 · 67 · 103 · 151 · 379 · 571 · 701 · 2393 · 5851 | **cheb only** | **new** | capped |
| 24 | 5002862939121639632040001 | 24.70 | 11 | 31 · 53 · 79 · 89 · 101 · 151 · 181 · 251 · 379 · 647 · 2549 | CN2 (rigid) | **new** | capped |
| 25 | 7865064643837556041286401 | 24.90 | 11 | 23 · 37 · 67 · 89 · 101 · 109 · 181 · 199 · 433 · 571 · 15809 | CN2 (rigid) | **new** | capped |
| 26 | 9400084864021826054720641 | 24.97 | 11 | 23 · 31 · 53 · 79 · 103 · 197 · 239 · 379 · 521 · 727 · 4523 | CN2 (rigid) | **new** | capped |

## 5. Checks

| check | result |
|---|---|
| all three runs complete, every shard recorded exactly once | ✓ |
| engine hashes identical to the order-2 certificate's | ✓ |
| capped run in cheb mode with LASTCALC and no skips | ✓ |
| no `UNPROVEN-PRIMALITY` flags | ✓ |
| the tail finds exactly the terms only it guarantees (2), nothing else | ✓ |
| all 12 terms of A299799 below $10^{22}$ (OEIS b-file) are found | ✓ |
| all 14 order-2 numbers below $10^{25}$ (A175531, proved) are found | ✓ |
| standalone check (`tests/check_cheb_terms.py`, standard library only): every term satisfies the definition | ✓ all 26 |
| shard replay (`cn2_replay_run.py`): sampled shards re-run alone on one thread reproduce their counters | ✓ 100 capped (uniform) and 30 capped (work-weighted), 60 pair and 30 $(q,a)$ shards, all counters identical (the tail sample is 19.5% of its work) |
| **validation run to $10^{22}$** (a validation run (not included), $T = 3{,}000$, $q^* = 10^6$): exactly A299799's 12 terms, nothing missing or new | ✓ |

The two reference lists are independent of this computation: OEIS's A299799 below $10^{22}$, and the separately certified order-2 census. Every reference number was found, and the six numbers outside both lists were each re-verified from scratch by trial division.

## 6. Reproducing

```bash
cd cheb-cn2-census
python3 cn2_split_campaign.py init --X 1e25 --R0 7000 --dir DIR --capped-only --lastcalc --mode cheb
# pair tail: copy and compile the certified cn2x/cn2pair.c (carmichael-order2-census-2) into DIR/pair
cd DIR/pair && CN2X_MODE=cheb ./cn2pair 10000000000000000000000000 7000 5500000 . 30 0 4096 60 0
cd DIR/tail && CN2X_MODE=cheb ./cn2tail 10000000000000000000000000 5500000 . 30 0 268435456 60 95
cd cheb-cn2-census && python3 cn2_split_campaign.py run --dir DIR --now --threads 30
python3 cn2_split_campaign.py verify --dir DIR
python3 cn2_tail_verify.py --X 1e25 --mode cheb --pair DIR/pair --qa DIR/tail --T 7000 --reference DIR/reference_cheb_1e25.json
python3 tests/check_cheb_terms.py DIR/b299799_1e25.txt
python3 cn2_replay_run.py --dir DIR --T 7000 --qstar 5500000
```

## 7. Cost

The census took about 65 minutes on 30 threads. At the same settings the pair stage had about 2.2 times as many candidates as in Howe mode, because the weaker congruences (modulus halved) leave larger classes. A Chebyshev census to $10^{28}$ would cost more than the order-2 one (25.6 h). Before planning one, the factor should be measured with a capped cheb run at a size where Howe-mode timings exist.
