---
location: post
title: Certified Chebyshev Census Below 10^28
author: Claude Opus 5.5 and JCP
date: 2026-10-15
---

# Certificate: the Chebyshev–Carmichael numbers below $10^{28}$

**Date:** 15 October 2026 (runs 13–15 October)
**Definition:** OEIS A299799, Carmichael numbers that are Chebyshev pseudoprimes: odd composite $n$ with $n \equiv 1$ or $p \pmod{(p^2-1)/2}$ for every prime $p \mid n$. Equivalently (A175530's criterion, with Carmichael's condition), $n$ is squarefree, $p-1 \mid n-1$, and $n \equiv \pm 1$ modulo both $p-1$ and $p+1$, for every $p \mid n$.
**Status:** the computations are complete and every check below passes. The result uses the engines and proofs of the order-2 certificate (the order-2 certificate ([carmichael-order2-census-2](https://github.com/pudepiedj/carmichael-order2-census-2), `docs/CN2_Certificate_1e28.md`)) unchanged, in their $D = 2$ ("cheb") mode, exactly as the census below $10^{25}$ (`docs/CN2_Cheb_Certificate_1e25.md`) did.
**Run directory:** `results/cert_1e28/`

---

## 1. The result

> **There are exactly 87 Chebyshev–Carmichael numbers (A299799) below $10^{28}$** (§4). No assumption is made about table caps or switch primes.

The 87 are:
- **45 order-2 Carmichael numbers**: exactly the 45 terms of A175531 below $10^{28}$, all rigid. Every order-2 Carmichael number is a Chebyshev number, since $(p^2-1)/2$ divides $p^2-1$. This run found no order-2 number outside that list, so it is also an independent check of the order-2 census below $10^{28}$.
- **42 Chebyshev-only numbers**: Chebyshev–Carmichael but not of order 2. At one or more of its primes each one sits "halfway round" $p^2-1$, that is, $n \equiv 1 + \tfrac{p^2-1}{2}$ or $p + \tfrac{p^2-1}{2} \pmod{p^2-1}$ (the column "halfway at" in §4).

A299799 lists 12 terms. Against that entry:
- **a(1)–a(12)** are confirmed;
- **75 terms are new to A299799**:
  - 39 are order-2 terms of A175531 that had not been added;
  - 36 are Chebyshev-only numbers that appear nowhere in OEIS. Six of them lie below $10^{25}$ (found by the census to $10^{25}$); **30 lie in $[10^{25}, 10^{28})$ and are new with this run**. Each of the 30 was searched for in OEIS (15 October 2026) with no hit.
- **a(1)–a(26)** are exactly the certified census below $10^{25}$.

**Smallest new terms.** The smallest term above $10^{25}$ is a(27) $= 12071465216556111317952001$, a(15) of A175531. The smallest Chebyshev-only term above $10^{25}$ is a(28) $= 13935937975195278973392001 \approx 1.39\times10^{25}$.

**Distribution by decade:**

| decade | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| terms | 2 | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 0 | 2 | 12 | 13 | 19 | 29 |

**Other facts from the census:**
- **Halfway primes.** Of the 42 Chebyshev-only terms, 20 are halfway at one prime, 13 at two, 5 at three, 3 at four and 1 at five.
- **Smallest prime.** No term is divisible by 5 or 7. Three terms have 11 as their smallest prime: two order-2 terms and one Chebyshev-only term, a(29) $\approx 1.91\times10^{25}$.
- **Largest prime.** The largest prime factor of any term is 474,949, in the Chebyshev-only a(82) $\approx 6.69\times10^{27}$. Its second-largest prime is 9,323, so it lies in the capped part. For the order-2 terms the largest is 209,089.

## 2. Why the order-2 engines and proofs apply

This section is unchanged from the census below $10^{25}$. The three engines take the modulus $g(p) = (p^2-1)/D$ as a parameter: $D = 1$ for Howe's order-2 numbers, and $D = 2$ here. With $D = 2$ they search exactly the A299799 condition. Both proofs are written for general $D \in \lbrace 1, 2\rbrace$, and each fact they use holds for $D = 2$:
- **F1:** $n$ is odd and $3 \nmid n$;
- **F2:** $n/p > g(p)$;
- **F3:** $n$ has at least three primes;
- **F4:** the role bounds;
- **F5:** the admissibility facts;
- **F6:** Chebyshev numbers are Carmichael numbers, since $p-1 \mid (p-1)(p+1)/2$.

The search is split exactly as in the order-2 certificate below $10^{28}$, with the same $T$:

| part | which $n$ | engine |
|---|---|---|
| capped | $p_{k-1} \le T = 15{,}000$ | `cn2xh`, `CN2X_MODE=cheb`, `CN2X_TCAP=15000`, `CN2X_LASTCALC=1` |
| pair tail | $p_{k-1} > T$ and $p_k \le q^* = 27{,}500{,}000$ | `cn2pair`, cheb mode |
| $(q,a)$ tail | a prime above $q^*$ | `cn2tail`, cheb mode, $R_0 = q^*$ |

## 3. The runs

All six engine files have the same sha256 as those of the order-2 certificate. They are recorded in `ENGINES.sha256` and were rechecked after the runs.

| | pair tail | $(q,a)$ tail | capped |
|---|---|---|---|
| shards | 4,096 / 4,096 | 5,584 / 5,584 | 275,259 / 275,259 |
| completion record | `"complete":true`, mode 2 | `"complete":true`, mode 2 | `"complete":true`, mode 2, `"lastcalc":1`, `skipmask 0` |
| work | $1.46\times10^{12}$ pairs; $9.75\times10^{11}$ candidates (equal to the dry count) | $1.50\times10^{12}$ tests over 129,622,001 primes $q$ | $3.59\times10^{12}$ nodes; $2.46\times10^{12}$ LIST candidates |
| Fermat survivors | 71,217 | 223 | 6,995,051 |
| numbers below $X$ | 1 | 0 | 87 |
| time (30 threads) | 12.6 h | 6.8 h | 20.6 h |

The whole census took about 40 hours.

**Verification.**
- **The capped half:** `cn2_split_campaign.py verify --dir results/cert_1e28` (`result.json`, `verify.log`) finds 87 numbers, with phase consistency OK and no missing reference. Its "CONDITIONAL" scope line and "tail: False" warning are expected: `split.json` describes the capped stage only, and the tail is run and verified separately.
- **The tail:** `cn2_tail_verify.py --X 1e28 --mode cheb … --T 15000` gives **PASS**. It finds exactly one number whose second-largest prime exceeds $T$, $2088144166339753513992001$ (term 18; primes 15391 and 17291 are both above $T$), and nothing else.
- **The union** of the two halves is the 87 terms. The capped run also found term 18, through LIST.

No `UNPROVEN-PRIMALITY` flag was raised.

## 4. The 87 terms

"Guaranteed by" names the part whose theorem covers the term. The b-file is `results/cert_1e28/b299799_1e28.txt`, and the wide table with switch primes and gaps is `results/cert_1e28/results_table.txt` (`cn2_results_table.py`).

| # | $n$ | $\log_{10} n$ | $k$ | prime factors | class | halfway at | in A299799 before? | guaranteed by |
|---|---|---|---|---|---|---|---|---|
| 1 | 443372888629441 | 14.65 | 8 | 17 · 31 · 41 · 43 · 89 · 97 · 167 · 331 | CN2 (rigid) |  | yes | capped |
| 2 | 582920080863121 | 14.77 | 7 | 41 · 53 · 79 · 103 · 239 · 271 · 509 | **cheb only** | 79,239,271 | yes | capped |
| 3 | 39671149333495681 | 16.60 | 9 | 17 · 37 · 41 · 71 · 79 · 97 · 113 · 131 · 191 | CN2 (rigid) |  | yes | capped |
| 4 | 842526563598720001 | 17.93 | 8 | 17 · 61 · 71 · 89 · 197 · 311 · 769 · 2729 | CN2 (rigid) |  | yes | capped |
| 5 | 2380296518909971201 | 18.38 | 9 | 19 · 41 · 43 · 71 · 89 · 127 · 199 · 449 · 991 | CN2 (rigid) |  | yes | capped |
| 6 | 3188618003602886401 | 18.50 | 8 | 29 · 37 · 79 · 181 · 191 · 449 · 701 · 3457 | CN2 (rigid) |  | yes | capped |
| 7 | 33711266676317630401 | 19.53 | 9 | 17 · 29 · 37 · 41 · 151 · 199 · 449 · 571 · 5851 | **cheb only** | 449 | yes | capped |
| 8 | 54764632857801026161 | 19.74 | 9 | 41 · 53 · 79 · 137 · 139 · 181 · 239 · 271 · 1429 | **cheb only** | 79,239,271 | yes | capped |
| 9 | 122762671289519184001 | 20.09 | 11 | 13 · 17 · 19 · 29 · 41 · 89 · 97 · 127 · 199 · 251 · 449 | **cheb only** | 127 | yes | capped |
| 10 | 361266866679292635601 | 20.56 | 11 | 17 · 23 · 29 · 37 · 41 · 43 · 61 · 109 · 199 · 419 · 881 | **cheb only** | 17,881 | yes | capped |
| 11 | 4208895375600667752001 | 21.62 | 10 | 17 · 29 · 31 · 43 · 71 · 79 · 199 · 389 · 2521 · 5851 | CN2 (rigid) |  | yes | capped |
| 12 | 7673096805497432749441 | 21.88 | 10 | 29 · 31 · 37 · 43 · 53 · 109 · 127 · 571 · 3079 · 4159 | **cheb only** | 127 | yes | capped |
| 13 | 193966598206145637873001 | 23.29 | 11 | 19 · 23 · 29 · 41 · 71 · 89 · 101 · 103 · 701 · 1429 · 5669 | **cheb only** | 23,41,71,89,103 | **new** | capped |
| 14 | 623655451404913888200241 | 23.79 | 9 | 23 · 79 · 109 · 239 · 881 · 883 · 1223 · 1973 · 7019 | **cheb only** | 79,239,881 | **new** | capped |
| 15 | 1159954316194989017102401 | 24.06 | 9 | 31 · 47 · 109 · 137 · 307 · 2927 · 3079 · 4049 · 4759 | CN2 (rigid) |  | **new** | capped |
| 16 | 1327183446436495124400001 | 24.12 | 11 | 13 · 17 · 23 · 29 · 89 · 97 · 251 · 449 · 641 · 1499 · 9631 | **cheb only** | 641 | **new** | capped |
| 17 | 1457044155748208447259841 | 24.16 | 10 | 79 · 97 · 131 · 139 · 191 · 229 · 379 · 461 · 571 · 2393 | **cheb only** | 191 | **new** | capped |
| 18 | 2088144166339753513992001 | 24.32 | 8 | 113 · 199 · 239 · 263 · 701 · 7919 · 15391 · 17291 | CN2 (rigid) |  | **new** | tail |
| 19 | 2196407820059694924883201 | 24.34 | 9 | 53 · 109 · 127 · 281 · 307 · 379 · 647 · 10529 · 13441 | CN2 (rigid) |  | **new** | capped |
| 20 | 3339611018825185787482801 | 24.52 | 12 | 19 · 41 · 43 · 53 · 67 · 89 · 103 · 131 · 137 · 307 · 389 · 1429 | CN2 (rigid) |  | **new** | capped |
| 21 | 3464334205088776324905601 | 24.54 | 12 | 17 · 31 · 37 · 41 · 43 · 59 · 113 · 181 · 199 · 233 · 521 · 3457 | **cheb only** | 3457 | **new** | capped |
| 22 | 4105879060352839139462401 | 24.61 | 8 | 89 · 239 · 401 · 2143 · 2311 · 3571 · 3761 · 7237 | CN2 (rigid) |  | **new** | capped |
| 23 | 4809665063400557951190601 | 24.68 | 10 | 41 · 53 · 67 · 103 · 151 · 379 · 571 · 701 · 2393 · 5851 | **cheb only** | 41,103,151,2393 | **new** | capped |
| 24 | 5002862939121639632040001 | 24.70 | 11 | 31 · 53 · 79 · 89 · 101 · 151 · 181 · 251 · 379 · 647 · 2549 | CN2 (rigid) |  | **new** | capped |
| 25 | 7865064643837556041286401 | 24.90 | 11 | 23 · 37 · 67 · 89 · 101 · 109 · 181 · 199 · 433 · 571 · 15809 | CN2 (rigid) |  | **new** | capped |
| 26 | 9400084864021826054720641 | 24.97 | 11 | 23 · 31 · 53 · 79 · 103 · 197 · 239 · 379 · 521 · 727 · 4523 | CN2 (rigid) |  | **new** | capped |
| 27 | 12071465216556111317952001 | 25.08 | 12 | 37 · 41 · 53 · 59 · 89 · 109 · 127 · 151 · 191 · 233 · 379 · 811 | CN2 (rigid) |  | **new** | capped |
| 28 | 13935937975195278973392001 | 25.14 | 12 | 23 · 29 · 37 · 71 · 83 · 109 · 113 · 127 · 199 · 251 · 419 · 2927 | **cheb only** | 127 | **new** | capped |
| 29 | 19087839966156095154384001 | 25.28 | 12 | 11 · 17 · 37 · 41 · 79 · 113 · 139 · 181 · 251 · 379 · 911 · 3457 | **cheb only** | 3457 | **new** | capped |
| 30 | 31280524488319495535546401 | 25.50 | 11 | 19 · 23 · 43 · 59 · 71 · 109 · 271 · 311 · 701 · 1301 · 47431 | CN2 (rigid) |  | **new** | capped |
| 31 | 32492501043239735947612801 | 25.51 | 11 | 11 · 31 · 41 · 79 · 103 · 271 · 313 · 389 · 911 · 2521 · 3769 | CN2 (rigid) |  | **new** | capped |
| 32 | 36991212507320386599648001 | 25.57 | 11 | 11 · 31 · 37 · 53 · 97 · 191 · 379 · 883 · 1151 · 2549 · 3041 | CN2 (rigid) |  | **new** | capped |
| 33 | 44774022865681509785985601 | 25.65 | 11 | 19 · 41 · 67 · 89 · 101 · 131 · 139 · 233 · 271 · 1301 · 63799 | CN2 (rigid) |  | **new** | capped |
| 34 | 50473184681492173584023041 | 25.70 | 11 | 37 · 53 · 67 · 131 · 139 · 181 · 229 · 419 · 577 · 911 · 2311 | CN2 (rigid) |  | **new** | capped |
| 35 | 54475112449147532388966721 | 25.74 | 10 | 29 · 97 · 103 · 139 · 181 · 307 · 827 · 1061 · 2393 · 11593 | CN2 (rigid) |  | **new** | capped |
| 36 | 68886771046178424397858801 | 25.84 | 11 | 53 · 71 · 79 · 101 · 109 · 139 · 181 · 461 · 647 · 911 · 3079 | **cheb only** | 79,911 | **new** | capped |
| 37 | 71712112526158742082244801 | 25.86 | 11 | 23 · 29 · 41 · 79 · 101 · 131 · 419 · 449 · 911 · 1223 · 11969 | **cheb only** | 449,11969 | **new** | capped |
| 38 | 76587257660615840312697601 | 25.88 | 11 | 13 · 19 · 31 · 67 · 107 · 139 · 197 · 479 · 1471 · 1801 · 40151 | CN2 (rigid) |  | **new** | capped |
| 39 | 85737999338407807647656401 | 25.93 | 12 | 23 · 29 · 53 · 79 · 101 · 103 · 109 · 181 · 199 · 239 · 647 · 4861 | **cheb only** | 79,239 | **new** | capped |
| 40 | 111356194710608262218643841 | 26.05 | 10 | 41 · 61 · 79 · 113 · 131 · 379 · 683 · 2729 · 4159 · 12959 | CN2 (rigid) |  | **new** | capped |
| 41 | 191970596806626660335913601 | 26.28 | 13 | 17 · 23 · 31 · 37 · 43 · 53 · 71 · 113 · 199 · 241 · 337 · 419 · 3457 | **cheb only** | 3457 | **new** | capped |
| 42 | 213622061697266764349808001 | 26.33 | 12 | 23 · 29 · 31 · 71 · 89 · 97 · 103 · 181 · 251 · 307 · 1871 · 6271 | **cheb only** | 6271 | **new** | capped |
| 43 | 227541194846069456562210001 | 26.36 | 12 | 17 · 19 · 29 · 41 · 53 · 79 · 131 · 139 · 199 · 727 · 4933 · 10889 | **cheb only** | 17,79,4933 | **new** | capped |
| 44 | 244041085292561389352520001 | 26.39 | 11 | 23 · 61 · 113 · 131 · 193 · 251 · 271 · 337 · 701 · 911 · 4159 | **cheb only** | 193,4159 | **new** | capped |
| 45 | 257553076956557894240652001 | 26.41 | 12 | 13 · 29 · 43 · 67 · 71 · 101 · 109 · 197 · 199 · 271 · 3499 · 8161 | **cheb only** | 8161 | **new** | capped |
| 46 | 373851853012084355680131361 | 26.57 | 11 | 37 · 71 · 103 · 109 · 131 · 181 · 239 · 419 · 461 · 3079 · 3761 | CN2 (rigid) |  | **new** | capped |
| 47 | 419746116449969951645203201 | 26.62 | 12 | 17 · 37 · 43 · 53 · 71 · 109 · 151 · 191 · 281 · 881 · 1409 · 3761 | CN2 (rigid) |  | **new** | capped |
| 48 | 472936079653356733106893201 | 26.67 | 10 | 23 · 43 · 197 · 349 · 419 · 521 · 701 · 911 · 5851 · 8527 | **cheb only** | 911,8527 | **new** | capped |
| 49 | 480650413824292471675755841 | 26.68 | 11 | 29 · 41 · 89 · 131 · 197 · 239 · 271 · 727 · 881 · 1429 · 2969 | CN2 (rigid) |  | **new** | capped |
| 50 | 507710311713618241797676801 | 26.71 | 11 | 41 · 47 · 71 · 89 · 127 · 151 · 241 · 967 · 1103 · 2089 · 4049 | CN2 (rigid) |  | **new** | capped |
| 51 | 571197082724681188312817281 | 26.76 | 11 | 29 · 43 · 67 · 71 · 131 · 211 · 307 · 953 · 1021 · 1429 · 8161 | CN2 (rigid) |  | **new** | capped |
| 52 | 598764213578029575774297601 | 26.78 | 13 | 23 · 29 · 43 · 53 · 79 · 109 · 113 · 127 · 181 · 239 · 379 · 433 · 449 | CN2 (rigid) |  | **new** | capped |
| 53 | 667882655094744395121816001 | 26.82 | 10 | 67 · 83 · 131 · 163 · 199 · 239 · 461 · 2393 · 5167 · 20747 | CN2 (rigid) |  | **new** | capped |
| 54 | 749114380387868248644660001 | 26.87 | 10 | 23 · 41 · 67 · 97 · 109 · 379 · 1567 · 4999 · 7309 · 51679 | **cheb only** | 97,1567,51679 | **new** | capped |
| 55 | 768927403921604814222336001 | 26.89 | 10 | 43 · 67 · 137 · 251 · 271 · 349 · 769 · 1427 · 4159 · 17981 | CN2 (rigid) |  | **new** | capped |
| 56 | 847201873829461072769246401 | 26.93 | 11 | 37 · 41 · 43 · 71 · 103 · 239 · 281 · 379 · 2287 · 2549 · 11969 | **cheb only** | 11969 | **new** | capped |
| 57 | 922904786964947393227420801 | 26.97 | 10 | 17 · 37 · 41 · 311 · 929 · 1217 · 1301 · 1601 · 3191 · 15313 | CN2 (rigid) |  | **new** | capped |
| 58 | 946295515632681859275671041 | 26.98 | 11 | 29 · 43 · 89 · 109 · 131 · 181 · 229 · 991 · 1427 · 1429 · 7129 | CN2 (rigid) |  | **new** | capped |
| 59 | 1445961713544933049178794081 | 27.16 | 12 | 23 · 37 · 41 · 43 · 53 · 89 · 109 · 241 · 571 · 929 · 2089 · 7019 | **cheb only** | 929 | **new** | capped |
| 60 | 1480947968491738280801467201 | 27.17 | 10 | 17 · 59 · 71 · 419 · 521 · 683 · 811 · 3191 · 4159 · 12959 | **cheb only** | 4159 | **new** | capped |
| 61 | 1710675679046386360978509841 | 27.23 | 11 | 43 · 59 · 89 · 131 · 233 · 311 · 433 · 463 · 1429 · 1489 · 1871 | **cheb only** | 433,463,1489,1871 | **new** | capped |
| 62 | 1800270906592423387847044321 | 27.26 | 10 | 79 · 97 · 103 · 137 · 211 · 1019 · 1117 · 2861 · 2969 · 8161 | **cheb only** | 97,8161 | **new** | capped |
| 63 | 1800352719110727998002987201 | 27.26 | 13 | 17 · 19 · 59 · 71 · 79 · 89 · 97 · 131 · 233 · 349 · 449 · 463 · 881 | **cheb only** | 449 | **new** | capped |
| 64 | 1862295045464158166966504401 | 27.27 | 11 | 43 · 47 · 71 · 107 · 197 · 239 · 307 · 919 · 1301 · 2311 · 3037 | **cheb only** | 47,239 | **new** | capped |
| 65 | 1941211286859256920630460801 | 27.29 | 12 | 31 · 37 · 41 · 43 · 89 · 101 · 151 · 199 · 307 · 463 · 2089 · 11969 | CN2 (rigid) |  | **new** | capped |
| 66 | 2119047331560739293908113921 | 27.33 | 12 | 17 · 37 · 43 · 47 · 79 · 89 · 113 · 127 · 571 · 911 · 3541 · 8969 | CN2 (rigid) |  | **new** | capped |
| 67 | 2142752298785201165308646401 | 27.33 | 11 | 23 · 37 · 83 · 113 · 163 · 191 · 601 · 701 · 911 · 3079 · 7297 | CN2 (rigid) |  | **new** | capped |
| 68 | 2325041445996414342573536161 | 27.37 | 11 | 19 · 29 · 47 · 71 · 79 · 137 · 557 · 619 · 2729 · 10711 · 11593 | CN2 (rigid) |  | **new** | capped |
| 69 | 2981071306952233928836603201 | 27.47 | 11 | 17 · 41 · 181 · 199 · 349 · 449 · 587 · 599 · 881 · 1171 · 2089 | **cheb only** | 449 | **new** | capped |
| 70 | 3002549563607572248383836801 | 27.48 | 12 | 13 · 29 · 43 · 89 · 109 · 127 · 263 · 353 · 461 · 827 · 1049 · 4049 | **cheb only** | 127 | **new** | capped |
| 71 | 3055408335216475232299905601 | 27.49 | 12 | 23 · 89 · 101 · 103 · 113 · 131 · 151 · 241 · 449 · 571 · 727 · 1429 | **cheb only** | 449 | **new** | capped |
| 72 | 3184712715668896364421268801 | 27.50 | 12 | 31 · 37 · 41 · 71 · 79 · 131 · 191 · 199 · 571 · 661 · 1217 · 5279 | **cheb only** | 191,1217 | **new** | capped |
| 73 | 3213322593860118229475166721 | 27.51 | 10 | 37 · 61 · 67 · 71 · 419 · 433 · 617 · 1103 · 11593 · 209089 | CN2 (rigid) |  | **new** | capped |
| 74 | 4291812303515083594987740001 | 27.63 | 11 | 43 · 47 · 73 · 113 · 151 · 223 · 461 · 571 · 599 · 5851 · 8287 | **cheb only** | 223,8287 | **new** | capped |
| 75 | 4383862422930048259296295201 | 27.64 | 11 | 37 · 53 · 71 · 97 · 163 · 379 · 419 · 491 · 701 · 1709 · 21319 | **cheb only** | 97 | **new** | capped |
| 76 | 4497699707671000342005093601 | 27.65 | 10 | 19 · 59 · 89 · 233 · 431 · 601 · 701 · 7309 · 9631 · 15137 | **cheb only** | 9631,15137 | **new** | capped |
| 77 | 4635427415991948819511107841 | 27.67 | 13 | 23 · 29 · 37 · 53 · 71 · 89 · 113 · 127 · 191 · 271 · 379 · 647 · 3079 | CN2 (rigid) |  | **new** | capped |
| 78 | 4955815709824370817666240001 | 27.70 | 12 | 41 · 67 · 71 · 73 · 103 · 131 · 199 · 239 · 271 · 701 · 1091 · 2617 | **cheb only** | 73 | **new** | capped |
| 79 | 5466953848346666426169619201 | 27.74 | 11 | 37 · 59 · 79 · 109 · 113 · 151 · 229 · 1217 · 2311 · 4523 · 5851 | CN2 (rigid) |  | **new** | capped |
| 80 | 6037031106243073961934109201 | 27.78 | 12 | 23 · 37 · 89 · 109 · 131 · 151 · 181 · 211 · 281 · 397 · 1483 · 5851 | CN2 (rigid) |  | **new** | capped |
| 81 | 6473975735726053723736568001 | 27.81 | 13 | 23 · 31 · 53 · 71 · 79 · 97 · 131 · 151 · 181 · 239 · 419 · 593 · 1481 | CN2 (rigid) |  | **new** | capped |
| 82 | 6689253573790144737930673201 | 27.83 | 10 | 13 · 47 · 67 · 149 · 239 · 307 · 919 · 3673 · 9323 · 474949 | **cheb only** | 47,239 | **new** | capped |
| 83 | 6901344518427089880041692801 | 27.84 | 12 | 29 · 37 · 41 · 43 · 71 · 101 · 127 · 151 · 701 · 1871 · 3457 · 5851 | **cheb only** | 127,3457 | **new** | capped |
| 84 | 7006270310872326698183179201 | 27.85 | 10 | 41 · 71 · 89 · 103 · 199 · 211 · 5851 · 6359 · 8161 · 20593 | CN2 (rigid) |  | **new** | capped |
| 85 | 8601689148505906566116203201 | 27.93 | 10 | 59 · 71 · 109 · 241 · 349 · 521 · 701 · 2053 · 2843 · 105071 | CN2 (rigid) |  | **new** | capped |
| 86 | 8838800136403254764954638201 | 27.95 | 12 | 29 · 43 · 67 · 71 · 101 · 109 · 139 · 151 · 919 · 1427 · 1597 · 3079 | **cheb only** | 71,151,919,3079 | **new** | capped |
| 87 | 9799274291299994931676646401 | 27.99 | 12 | 31 · 41 · 53 · 71 · 101 · 103 · 199 · 239 · 379 · 449 · 4159 · 5851 | CN2 (rigid) |  | **new** | capped |

## 5. Checks

| check | result |
|---|---|
| all three runs complete, every shard recorded exactly once | ✓ |
| engine hashes identical to the order-2 certificate's | ✓ |
| capped run in cheb mode with LASTCALC and no skips | ✓ |
| no `UNPROVEN-PRIMALITY` flags | ✓ |
| the tail finds exactly the term only it guarantees (1), nothing else | ✓ |
| all 12 terms of A299799 (OEIS DATA) are found | ✓ |
| all 26 terms of the certified census below $10^{25}$ are found, as a(1)–a(26) | ✓ |
| all 45 order-2 numbers below $10^{28}$ (A175531, certified) are found, and no other order-2 number | ✓ |
| standalone check (`tests/check_cheb_terms.py`, standard library only): every term satisfies the definition | ✓ all 87 |
| shard replay (`cn2_replay_run.py`): sampled shards re-run alone on one thread reproduce their counters | ✓ 100 capped (uniform) and 30 capped (work-weighted), 60 pair and 30 $(q,a)$ shards, all counters identical (`replay.log`; the samples hold 0.34%, 1.67% and 0.54% of their stages' work) |
| the 30 new Chebyshev-only terms: no OEIS hit | ✓ |

The reference lists are independent of this computation: OEIS's A299799, and the separately certified order-2 census. Every reference number was found, and each of the 30 numbers outside both lists was re-verified from scratch by trial division.

## 6. Reproducing

```bash
cd cheb-cn2-census
python3 cn2_split_campaign.py init --X 1e28 --R0 15000 --dir DIR --capped-only --lastcalc --mode cheb
# pair tail and (q,a) tail: copy and compile the certified cn2x/cn2pair.c and cn2x/cn2tail.c into DIR/pair and DIR/tail
cd DIR/pair && CN2X_MODE=cheb ./cn2pair 10000000000000000000000000000 15000 27500000 . 30 0 4096 60 0
cd DIR/tail && CN2X_MODE=cheb ./cn2tail 10000000000000000000000000000 27500000 . 30 0 268435456 60 95
cd cheb-cn2-census && python3 cn2_split_campaign.py run --dir DIR --now --threads 30
python3 cn2_split_campaign.py verify --dir DIR --reference results/cert_1e25
python3 cn2_tail_verify.py --X 1e28 --mode cheb --pair DIR/pair --qa DIR/tail --T 15000 --reference DIR/reference_cheb_1e28.json
python3 tests/check_cheb_terms.py DIR/b299799_1e28.txt
python3 cn2_replay_run.py --dir DIR --T 15000 --qstar 27500000
python3 cn2_results_table.py --dir DIR --oeis results/A299799_oeis.json --reference DIR/reference_cheb_1e28.json
```

`reference_cheb_1e28.json` holds the 57 reference numbers: the 26 of the census below $10^{25}$, together with the 45 of A175531 below $10^{28}$.

## 7. Cost

Against the order-2 census at the same $T$ (25.6 h; its $q^*$ was 24,500,000, against 27,500,000 here), the Chebyshev census took about 1.6 times as long:

| stage | order 2 | Chebyshev | ratio |
|---|---|---|---|
| capped | 12.9 h | 20.6 h | 1.6 |
| pair tail | 8.0 h | 12.6 h | 1.6 |
| $(q,a)$ tail | 4.7 h | 6.8 h | 1.4 |

The halved modulus leaves larger residue classes, so every stage has more candidates. The $(q,a)$ tail's test rate also fell to $6.1\times10^{7}$ per second, half its rate at $10^{25}$.
