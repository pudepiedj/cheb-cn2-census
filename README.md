# Chebyshev–Carmichael numbers: a certified census

This repository contains the programs, the run records, the proofs and the checks behind a complete list of the Chebyshev–Carmichael numbers (OEIS [A299799](https://oeis.org/A299799)) below $10^{28}$:

> **There are exactly 87 Chebyshev–Carmichael numbers below 10²⁸.**

**In brief.**
- **What they are:** composite numbers that pass two primality tests for every base. One is Fermat's test, $a^n \equiv a \pmod n$, and the other uses Chebyshev polynomials, $T_n(a) \equiv a \pmod n$. The next section explains what this means.
- **The 87 terms:**
  - 45 are Carmichael numbers of order 2. These are exactly the 45 terms of [A175531](https://oeis.org/A175531) below $10^{28}$.
  - 42 are Chebyshev only.
- **Against OEIS:** below $10^{22}$ the census reproduces exactly the 12 terms A299799 lists. **75 terms are new to A299799**:
  - 39 are order-2 terms of A175531 that had never been listed there;
  - 36 are Chebyshev-only numbers that appear nowhere in OEIS. 30 of these lie between $10^{25}$ and $10^{28}$.

**Status.** The computation is complete and every check passes ([certificate](docs/CN2_Cheb_Certificate_1e28.md)). The search uses the same engines and the same two coverage proofs that certified the order-2 census below $10^{28}$ ([carmichael-order2-census-2](https://github.com/pudepiedj/carmichael-order2-census-2)). Here they run with the Chebyshev modulus $(p^2-1)/2$ in place of $p^2-1$. An earlier census below $10^{25}$, with 26 terms, is certified separately ([certificate](docs/CN2_Cheb_Certificate_1e25.md)). Its terms are a(1)–a(26) here.

**Not A175530.** The larger sequence [A175530](https://oeis.org/A175530) (Chebyshev pseudoprimes) also contains numbers that are not Carmichael numbers, such as $79397009999$, which is $\equiv -1$ modulo every $p \pm 1$. This census covers only the Carmichael ones, A299799 $=$ A175530 $\cap$ A002997.

## What is a Chebyshev–Carmichael number?

### Fermat's test, and the numbers that fool it

If $p$ is prime, then $a^p \equiv a \pmod p$ for every whole number $a$ (Fermat's little theorem). It is tempting to use this as a primality test, but some composite numbers pass it for every $a$. These are the **Carmichael numbers** (A002997). The smallest is $561 = 3\cdot 11\cdot 17$. Korselt's criterion says exactly which numbers they are: a composite $n$ is a Carmichael number when it is squarefree and $p-1$ divides $n-1$ for every prime $p \mid n$.

### The same test with Chebyshev polynomials

The **Chebyshev polynomials** are defined by $T_n(\cos\theta) = \cos n\theta$. Equivalently, $T_0 = 1$, $T_1 = x$ and $T_{n+1} = 2x\thinspace T_n - T_{n-1}$, which gives
$$T_2 = 2x^2 - 1, \qquad T_3 = 4x^3 - 3x, \qquad T_5 = 16x^5 - 20x^3 + 5x, \ \dots$$
They behave like powers: just as $(x^m)^n = x^{mn}$, so $T_m(T_n(x)) = T_{mn}(x)$. They also obey their own version of Fermat's theorem: **if $p$ is an odd prime, then $T_p(a) \equiv a \pmod p$ for every whole number $a$.** (For $p = 2$ it fails, since $T_2(0) = -1$.) For example, with $p = 3$, $T_3(a) = 4a^3 - 3a \equiv a^3 \equiv a \pmod 3$.

A composite $n$ with $T_n(a) \equiv a \pmod n$ for every $a$ is a **Chebyshev pseudoprime** (A175530). A **Chebyshev–Carmichael number** (A299799) passes both tests for every $a$: it is a Carmichael number and a Chebyshev pseudoprime. Neither test can tell it from a prime.

### The rule that decides it

For a squarefree $n$, the Chebyshev test holds exactly when every prime $p \mid n$ satisfies
$$n \equiv \pm 1 \pmod{p-1} \quad\text{and}\quad n \equiv \pm 1 \pmod{p+1}.$$
Being a Carmichael number as well forces the $+$ sign mod $p-1$. That leaves two cases for each prime:

| mod $p-1$ | mod $p+1$ | together |
|---|---|---|
| $n \equiv 1$ | $n \equiv 1$ | $n \equiv 1 \pmod{(p^2-1)/2}$ |
| $n \equiv 1$ | $n \equiv -1$ | $n \equiv p \pmod{(p^2-1)/2}$ |

The modulus is $(p^2-1)/2$, not $p^2-1$, because $p-1$ and $p+1$ are consecutive even numbers. Their only common factor is 2, so their least common multiple is half their product. This gives the definition OEIS states:
$$n \text{ is a Chebyshev–Carmichael number} \iff n \text{ is odd and composite, and } n \equiv 1 \text{ or } p \pmod{\tfrac{p^2-1}{2}} \text{ for every prime } p \mid n.$$

**Where the $\pm$ comes from.** Substitute $a = (u + u^{-1})/2$. Then $T_n(a) = (u^n + u^{-n})/2$, so Chebyshev's test only ever sees $u$ through $u + u^{-1}$, and it cannot tell $u$ from $1/u$. Modulo $p$, the numbers $u$ that arise are of two kinds:
- ordinary residues mod $p$, a group of $p-1$ elements;
- elements of "norm 1" in the field of $p^2$ elements, a group of $p+1$ elements.

So the test asks only that $u^n = u$ or $u^n = u^{-1}$ in each of these groups. That is the $\pm 1$ mod $p-1$ and mod $p+1$.

### How it differs from a Carmichael number of order 2

A **Carmichael number of order 2** (Howe's definition, A175531) satisfies the same congruence with the *full* modulus:
$$n \equiv 1 \text{ or } p \pmod{p^2-1} \quad\text{for every prime } p \mid n.$$
This says that $n$ imitates a prime in the whole field of $p^2$ elements: raising to the $n$-th power fixes every element or acts as Frobenius ($a \mapsto a^p$) on all of them. Chebyshev's test asks less. It looks only at the two subgroups above, each up to the swap $u \leftrightarrow 1/u$, and the two subgroups together make up only half of the field's $p^2 - 1$ non-zero elements.

| | Carmichael of order 2 (A175531) | Chebyshev–Carmichael (A299799) |
|---|---|---|
| condition at each prime $p \mid n$ | $n \equiv 1$ or $p \pmod{p^2-1}$ | $n \equiv 1$ or $p \pmod{(p^2-1)/2}$ |
| in the commonest case, $n - 1$ must be divisible by | $(p-1)(p+1)$, the product | $\operatorname{lcm}(p-1,\thinspace p+1)$, half the product |
| imitates a prime for | powers $a^n$ in the whole field of $p^2$ elements | Chebyshev polynomials $T_n(a)$ |

**So every Carmichael number of order 2 is a Chebyshev–Carmichael number, but not the other way round.** The difference is exactly one factor of 2 in the modulus. At some prime, a Chebyshev–Carmichael number that is not of order 2 sits exactly halfway round the larger modulus: $n \equiv 1 + \tfrac{p^2-1}{2}$ or $p + \tfrac{p^2-1}{2} \pmod{p^2-1}$.

**Example.** $a(2) = 582920080863121 = 41\cdot 53\cdot 79\cdot 103\cdot 239\cdot 271\cdot 509$ is the smallest Chebyshev–Carmichael number that is not of order 2.
- At $p = 79$: $p - 1 = 78$, $p + 1 = 80$, $(p^2-1)/2 = 3120$ and $p^2 - 1 = 6240$.
  - $n - 1$ is divisible by 78, by 80 and so by 3120. That makes $79$ a Chebyshev prime of $n$.
  - However, $n \equiv 3121 = 1 + 3120 \pmod{6240}$. That is halfway, so $n$ fails the order-2 condition at 79.
- The same happens at $239$ and at $271$.
- At the other four primes $n \equiv 1 \pmod{p^2-1}$.

By contrast, the smallest term, $a(1) = 443372888629441 = 17\cdot 31\cdot 41\cdot 43\cdot 89\cdot 97\cdot 167\cdot 331$, satisfies $n \equiv 1 \pmod{p^2-1}$ at all eight primes. So it is of order 2 as well, and it is also the first term of A175531.

**A note on the word "order".** "Order 2" refers to the field of $p^2$ elements, and Howe defines Carmichael numbers of every order $m$ using fields of $p^m$ elements. Chebyshev numbers form a single family, with no order attached. They sit between order 1 (ordinary Carmichael numbers) and order 2: every order-2 number is one, and every one is an ordinary Carmichael number.

**Why the order-2 numbers appear in this list.** A299799 is defined by the Chebyshev condition alone, so every term of A175531 is automatically a term of A299799. This census lists them all. In the table below each term is marked as order 2 (it is in both sequences) or Chebyshev only.

## The terms below 10²⁸

Also in `results/b299799.txt`. The wide table with switch primes and gaps is `results/cert_1e28/results_table.txt` (`cn2_results_table.py`). "Halfway at" lists the primes where a Chebyshev-only term sits halfway round $p^2-1$, that is, $n \equiv 1 + \tfrac{p^2-1}{2}$ or $p + \tfrac{p^2-1}{2} \pmod{p^2-1}$, so it fails the order-2 condition there.

| n | a(n) | log10 | class | halfway at | prime factors | in OEIS before this census |
|---|---|---|---|---|---|---|
| 1 | 443372888629441 | 14.65 | order 2 |  | 17 · 31 · 41 · 43 · 89 · 97 · 167 · 331 | A299799 |
| 2 | 582920080863121 | 14.77 | Chebyshev only | 79, 239, 271 | 41 · 53 · 79 · 103 · 239 · 271 · 509 | A299799 |
| 3 | 39671149333495681 | 16.60 | order 2 |  | 17 · 37 · 41 · 71 · 79 · 97 · 113 · 131 · 191 | A299799 |
| 4 | 842526563598720001 | 17.93 | order 2 |  | 17 · 61 · 71 · 89 · 197 · 311 · 769 · 2729 | A299799 |
| 5 | 2380296518909971201 | 18.38 | order 2 |  | 19 · 41 · 43 · 71 · 89 · 127 · 199 · 449 · 991 | A299799 |
| 6 | 3188618003602886401 | 18.50 | order 2 |  | 29 · 37 · 79 · 181 · 191 · 449 · 701 · 3457 | A299799 |
| 7 | 33711266676317630401 | 19.53 | Chebyshev only | 449 | 17 · 29 · 37 · 41 · 151 · 199 · 449 · 571 · 5851 | A299799 |
| 8 | 54764632857801026161 | 19.74 | Chebyshev only | 79, 239, 271 | 41 · 53 · 79 · 137 · 139 · 181 · 239 · 271 · 1429 | A299799 |
| 9 | 122762671289519184001 | 20.09 | Chebyshev only | 127 | 13 · 17 · 19 · 29 · 41 · 89 · 97 · 127 · 199 · 251 · 449 | A299799 |
| 10 | 361266866679292635601 | 20.56 | Chebyshev only | 17, 881 | 17 · 23 · 29 · 37 · 41 · 43 · 61 · 109 · 199 · 419 · 881 | A299799 |
| 11 | 4208895375600667752001 | 21.62 | order 2 |  | 17 · 29 · 31 · 43 · 71 · 79 · 199 · 389 · 2521 · 5851 | A299799 |
| 12 | 7673096805497432749441 | 21.88 | Chebyshev only | 127 | 29 · 31 · 37 · 43 · 53 · 109 · 127 · 571 · 3079 · 4159 | A299799 |
| 13 | 193966598206145637873001 | 23.29 | Chebyshev only | 23, 41, 71, 89, 103 | 19 · 23 · 29 · 41 · 71 · 89 · 101 · 103 · 701 · 1429 · 5669 | **no** |
| 14 | 623655451404913888200241 | 23.79 | Chebyshev only | 79, 239, 881 | 23 · 79 · 109 · 239 · 881 · 883 · 1223 · 1973 · 7019 | **no** |
| 15 | 1159954316194989017102401 | 24.06 | order 2 |  | 31 · 47 · 109 · 137 · 307 · 2927 · 3079 · 4049 · 4759 | A175531 only |
| 16 | 1327183446436495124400001 | 24.12 | Chebyshev only | 641 | 13 · 17 · 23 · 29 · 89 · 97 · 251 · 449 · 641 · 1499 · 9631 | **no** |
| 17 | 1457044155748208447259841 | 24.16 | Chebyshev only | 191 | 79 · 97 · 131 · 139 · 191 · 229 · 379 · 461 · 571 · 2393 | **no** |
| 18 | 2088144166339753513992001 | 24.32 | order 2 |  | 113 · 199 · 239 · 263 · 701 · 7919 · 15391 · 17291 | A175531 only |
| 19 | 2196407820059694924883201 | 24.34 | order 2 |  | 53 · 109 · 127 · 281 · 307 · 379 · 647 · 10529 · 13441 | A175531 only |
| 20 | 3339611018825185787482801 | 24.52 | order 2 |  | 19 · 41 · 43 · 53 · 67 · 89 · 103 · 131 · 137 · 307 · 389 · 1429 | A175531 only |
| 21 | 3464334205088776324905601 | 24.54 | Chebyshev only | 3457 | 17 · 31 · 37 · 41 · 43 · 59 · 113 · 181 · 199 · 233 · 521 · 3457 | **no** |
| 22 | 4105879060352839139462401 | 24.61 | order 2 |  | 89 · 239 · 401 · 2143 · 2311 · 3571 · 3761 · 7237 | A175531 only |
| 23 | 4809665063400557951190601 | 24.68 | Chebyshev only | 41, 103, 151, 2393 | 41 · 53 · 67 · 103 · 151 · 379 · 571 · 701 · 2393 · 5851 | **no** |
| 24 | 5002862939121639632040001 | 24.70 | order 2 |  | 31 · 53 · 79 · 89 · 101 · 151 · 181 · 251 · 379 · 647 · 2549 | A175531 only |
| 25 | 7865064643837556041286401 | 24.90 | order 2 |  | 23 · 37 · 67 · 89 · 101 · 109 · 181 · 199 · 433 · 571 · 15809 | A175531 only |
| 26 | 9400084864021826054720641 | 24.97 | order 2 |  | 23 · 31 · 53 · 79 · 103 · 197 · 239 · 379 · 521 · 727 · 4523 | A175531 only |
| 27 | 12071465216556111317952001 | 25.08 | order 2 |  | 37 · 41 · 53 · 59 · 89 · 109 · 127 · 151 · 191 · 233 · 379 · 811 | A175531 only |
| 28 | 13935937975195278973392001 | 25.14 | Chebyshev only | 127 | 23 · 29 · 37 · 71 · 83 · 109 · 113 · 127 · 199 · 251 · 419 · 2927 | **no** |
| 29 | 19087839966156095154384001 | 25.28 | Chebyshev only | 3457 | 11 · 17 · 37 · 41 · 79 · 113 · 139 · 181 · 251 · 379 · 911 · 3457 | **no** |
| 30 | 31280524488319495535546401 | 25.50 | order 2 |  | 19 · 23 · 43 · 59 · 71 · 109 · 271 · 311 · 701 · 1301 · 47431 | A175531 only |
| 31 | 32492501043239735947612801 | 25.51 | order 2 |  | 11 · 31 · 41 · 79 · 103 · 271 · 313 · 389 · 911 · 2521 · 3769 | A175531 only |
| 32 | 36991212507320386599648001 | 25.57 | order 2 |  | 11 · 31 · 37 · 53 · 97 · 191 · 379 · 883 · 1151 · 2549 · 3041 | A175531 only |
| 33 | 44774022865681509785985601 | 25.65 | order 2 |  | 19 · 41 · 67 · 89 · 101 · 131 · 139 · 233 · 271 · 1301 · 63799 | A175531 only |
| 34 | 50473184681492173584023041 | 25.70 | order 2 |  | 37 · 53 · 67 · 131 · 139 · 181 · 229 · 419 · 577 · 911 · 2311 | A175531 only |
| 35 | 54475112449147532388966721 | 25.74 | order 2 |  | 29 · 97 · 103 · 139 · 181 · 307 · 827 · 1061 · 2393 · 11593 | A175531 only |
| 36 | 68886771046178424397858801 | 25.84 | Chebyshev only | 79, 911 | 53 · 71 · 79 · 101 · 109 · 139 · 181 · 461 · 647 · 911 · 3079 | **no** |
| 37 | 71712112526158742082244801 | 25.86 | Chebyshev only | 449, 11969 | 23 · 29 · 41 · 79 · 101 · 131 · 419 · 449 · 911 · 1223 · 11969 | **no** |
| 38 | 76587257660615840312697601 | 25.88 | order 2 |  | 13 · 19 · 31 · 67 · 107 · 139 · 197 · 479 · 1471 · 1801 · 40151 | A175531 only |
| 39 | 85737999338407807647656401 | 25.93 | Chebyshev only | 79, 239 | 23 · 29 · 53 · 79 · 101 · 103 · 109 · 181 · 199 · 239 · 647 · 4861 | **no** |
| 40 | 111356194710608262218643841 | 26.05 | order 2 |  | 41 · 61 · 79 · 113 · 131 · 379 · 683 · 2729 · 4159 · 12959 | A175531 only |
| 41 | 191970596806626660335913601 | 26.28 | Chebyshev only | 3457 | 17 · 23 · 31 · 37 · 43 · 53 · 71 · 113 · 199 · 241 · 337 · 419 · 3457 | **no** |
| 42 | 213622061697266764349808001 | 26.33 | Chebyshev only | 6271 | 23 · 29 · 31 · 71 · 89 · 97 · 103 · 181 · 251 · 307 · 1871 · 6271 | **no** |
| 43 | 227541194846069456562210001 | 26.36 | Chebyshev only | 17, 79, 4933 | 17 · 19 · 29 · 41 · 53 · 79 · 131 · 139 · 199 · 727 · 4933 · 10889 | **no** |
| 44 | 244041085292561389352520001 | 26.39 | Chebyshev only | 193, 4159 | 23 · 61 · 113 · 131 · 193 · 251 · 271 · 337 · 701 · 911 · 4159 | **no** |
| 45 | 257553076956557894240652001 | 26.41 | Chebyshev only | 8161 | 13 · 29 · 43 · 67 · 71 · 101 · 109 · 197 · 199 · 271 · 3499 · 8161 | **no** |
| 46 | 373851853012084355680131361 | 26.57 | order 2 |  | 37 · 71 · 103 · 109 · 131 · 181 · 239 · 419 · 461 · 3079 · 3761 | A175531 only |
| 47 | 419746116449969951645203201 | 26.62 | order 2 |  | 17 · 37 · 43 · 53 · 71 · 109 · 151 · 191 · 281 · 881 · 1409 · 3761 | A175531 only |
| 48 | 472936079653356733106893201 | 26.67 | Chebyshev only | 911, 8527 | 23 · 43 · 197 · 349 · 419 · 521 · 701 · 911 · 5851 · 8527 | **no** |
| 49 | 480650413824292471675755841 | 26.68 | order 2 |  | 29 · 41 · 89 · 131 · 197 · 239 · 271 · 727 · 881 · 1429 · 2969 | A175531 only |
| 50 | 507710311713618241797676801 | 26.71 | order 2 |  | 41 · 47 · 71 · 89 · 127 · 151 · 241 · 967 · 1103 · 2089 · 4049 | A175531 only |
| 51 | 571197082724681188312817281 | 26.76 | order 2 |  | 29 · 43 · 67 · 71 · 131 · 211 · 307 · 953 · 1021 · 1429 · 8161 | A175531 only |
| 52 | 598764213578029575774297601 | 26.78 | order 2 |  | 23 · 29 · 43 · 53 · 79 · 109 · 113 · 127 · 181 · 239 · 379 · 433 · 449 | A175531 only |
| 53 | 667882655094744395121816001 | 26.82 | order 2 |  | 67 · 83 · 131 · 163 · 199 · 239 · 461 · 2393 · 5167 · 20747 | A175531 only |
| 54 | 749114380387868248644660001 | 26.87 | Chebyshev only | 97, 1567, 51679 | 23 · 41 · 67 · 97 · 109 · 379 · 1567 · 4999 · 7309 · 51679 | **no** |
| 55 | 768927403921604814222336001 | 26.89 | order 2 |  | 43 · 67 · 137 · 251 · 271 · 349 · 769 · 1427 · 4159 · 17981 | A175531 only |
| 56 | 847201873829461072769246401 | 26.93 | Chebyshev only | 11969 | 37 · 41 · 43 · 71 · 103 · 239 · 281 · 379 · 2287 · 2549 · 11969 | **no** |
| 57 | 922904786964947393227420801 | 26.97 | order 2 |  | 17 · 37 · 41 · 311 · 929 · 1217 · 1301 · 1601 · 3191 · 15313 | A175531 only |
| 58 | 946295515632681859275671041 | 26.98 | order 2 |  | 29 · 43 · 89 · 109 · 131 · 181 · 229 · 991 · 1427 · 1429 · 7129 | A175531 only |
| 59 | 1445961713544933049178794081 | 27.16 | Chebyshev only | 929 | 23 · 37 · 41 · 43 · 53 · 89 · 109 · 241 · 571 · 929 · 2089 · 7019 | **no** |
| 60 | 1480947968491738280801467201 | 27.17 | Chebyshev only | 4159 | 17 · 59 · 71 · 419 · 521 · 683 · 811 · 3191 · 4159 · 12959 | **no** |
| 61 | 1710675679046386360978509841 | 27.23 | Chebyshev only | 433, 463, 1489, 1871 | 43 · 59 · 89 · 131 · 233 · 311 · 433 · 463 · 1429 · 1489 · 1871 | **no** |
| 62 | 1800270906592423387847044321 | 27.26 | Chebyshev only | 97, 8161 | 79 · 97 · 103 · 137 · 211 · 1019 · 1117 · 2861 · 2969 · 8161 | **no** |
| 63 | 1800352719110727998002987201 | 27.26 | Chebyshev only | 449 | 17 · 19 · 59 · 71 · 79 · 89 · 97 · 131 · 233 · 349 · 449 · 463 · 881 | **no** |
| 64 | 1862295045464158166966504401 | 27.27 | Chebyshev only | 47, 239 | 43 · 47 · 71 · 107 · 197 · 239 · 307 · 919 · 1301 · 2311 · 3037 | **no** |
| 65 | 1941211286859256920630460801 | 27.29 | order 2 |  | 31 · 37 · 41 · 43 · 89 · 101 · 151 · 199 · 307 · 463 · 2089 · 11969 | A175531 only |
| 66 | 2119047331560739293908113921 | 27.33 | order 2 |  | 17 · 37 · 43 · 47 · 79 · 89 · 113 · 127 · 571 · 911 · 3541 · 8969 | A175531 only |
| 67 | 2142752298785201165308646401 | 27.33 | order 2 |  | 23 · 37 · 83 · 113 · 163 · 191 · 601 · 701 · 911 · 3079 · 7297 | A175531 only |
| 68 | 2325041445996414342573536161 | 27.37 | order 2 |  | 19 · 29 · 47 · 71 · 79 · 137 · 557 · 619 · 2729 · 10711 · 11593 | A175531 only |
| 69 | 2981071306952233928836603201 | 27.47 | Chebyshev only | 449 | 17 · 41 · 181 · 199 · 349 · 449 · 587 · 599 · 881 · 1171 · 2089 | **no** |
| 70 | 3002549563607572248383836801 | 27.48 | Chebyshev only | 127 | 13 · 29 · 43 · 89 · 109 · 127 · 263 · 353 · 461 · 827 · 1049 · 4049 | **no** |
| 71 | 3055408335216475232299905601 | 27.49 | Chebyshev only | 449 | 23 · 89 · 101 · 103 · 113 · 131 · 151 · 241 · 449 · 571 · 727 · 1429 | **no** |
| 72 | 3184712715668896364421268801 | 27.50 | Chebyshev only | 191, 1217 | 31 · 37 · 41 · 71 · 79 · 131 · 191 · 199 · 571 · 661 · 1217 · 5279 | **no** |
| 73 | 3213322593860118229475166721 | 27.51 | order 2 |  | 37 · 61 · 67 · 71 · 419 · 433 · 617 · 1103 · 11593 · 209089 | A175531 only |
| 74 | 4291812303515083594987740001 | 27.63 | Chebyshev only | 223, 8287 | 43 · 47 · 73 · 113 · 151 · 223 · 461 · 571 · 599 · 5851 · 8287 | **no** |
| 75 | 4383862422930048259296295201 | 27.64 | Chebyshev only | 97 | 37 · 53 · 71 · 97 · 163 · 379 · 419 · 491 · 701 · 1709 · 21319 | **no** |
| 76 | 4497699707671000342005093601 | 27.65 | Chebyshev only | 9631, 15137 | 19 · 59 · 89 · 233 · 431 · 601 · 701 · 7309 · 9631 · 15137 | **no** |
| 77 | 4635427415991948819511107841 | 27.67 | order 2 |  | 23 · 29 · 37 · 53 · 71 · 89 · 113 · 127 · 191 · 271 · 379 · 647 · 3079 | A175531 only |
| 78 | 4955815709824370817666240001 | 27.70 | Chebyshev only | 73 | 41 · 67 · 71 · 73 · 103 · 131 · 199 · 239 · 271 · 701 · 1091 · 2617 | **no** |
| 79 | 5466953848346666426169619201 | 27.74 | order 2 |  | 37 · 59 · 79 · 109 · 113 · 151 · 229 · 1217 · 2311 · 4523 · 5851 | A175531 only |
| 80 | 6037031106243073961934109201 | 27.78 | order 2 |  | 23 · 37 · 89 · 109 · 131 · 151 · 181 · 211 · 281 · 397 · 1483 · 5851 | A175531 only |
| 81 | 6473975735726053723736568001 | 27.81 | order 2 |  | 23 · 31 · 53 · 71 · 79 · 97 · 131 · 151 · 181 · 239 · 419 · 593 · 1481 | A175531 only |
| 82 | 6689253573790144737930673201 | 27.83 | Chebyshev only | 47, 239 | 13 · 47 · 67 · 149 · 239 · 307 · 919 · 3673 · 9323 · 474949 | **no** |
| 83 | 6901344518427089880041692801 | 27.84 | Chebyshev only | 127, 3457 | 29 · 37 · 41 · 43 · 71 · 101 · 127 · 151 · 701 · 1871 · 3457 · 5851 | **no** |
| 84 | 7006270310872326698183179201 | 27.85 | order 2 |  | 41 · 71 · 89 · 103 · 199 · 211 · 5851 · 6359 · 8161 · 20593 | A175531 only |
| 85 | 8601689148505906566116203201 | 27.93 | order 2 |  | 59 · 71 · 109 · 241 · 349 · 521 · 701 · 2053 · 2843 · 105071 | A175531 only |
| 86 | 8838800136403254764954638201 | 27.95 | Chebyshev only | 71, 151, 919, 3079 | 29 · 43 · 67 · 71 · 101 · 109 · 139 · 151 · 919 · 1427 · 1597 · 3079 | **no** |
| 87 | 9799274291299994931676646401 | 27.99 | order 2 |  | 31 · 41 · 53 · 71 · 101 · 103 · 199 · 239 · 379 · 449 · 4159 · 5851 | A175531 only |

**By decade:**

| decade | 14 | 16 | 17 | 18 | 19 | 20 | 21 | 23 | 24 | 25 | 26 | 27 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| terms | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 12 | 13 | 19 | 29 |

The census also shows:
- **No term is divisible by 5 or 7.**
- **The largest prime factor of any term is 474,949**, in a(82). Among the order-2 terms the largest is 209,089.
- **Halfway primes:** of the 42 Chebyshev-only terms, 20 are halfway at one prime, 13 at two, 5 at three, 3 at four and 1 at five.

## How the search works

Every Chebyshev–Carmichael $n < X$, with primes $p_1 < \dots < p_k$, falls into one of three parts. Each part has its own engine and its own completeness theorem. The two proofs are written for both moduli, $g(p) = (p^2-1)/D$ with $D = 1$ (order 2) or $D = 2$ (Chebyshev). The engines run in Chebyshev mode with `CN2X_MODE=cheb`.

| part | which $n$ | engine | why it misses nothing |
|---|---|---|---|
| capped | $p_{k-1} \le T$ | `cn2xh.c`: depth-first search over the primes up to $T$, with LASTCALC | [LASTCALC proof](docs/CN2_LastCalc_Coverage_Proof.md) |
| pair tail | $p_{k-1} > T$, $p_k \le q^*$ | `cn2pair.c`: one residue class per prime pair $T < p < q \le q^*$ | [tail proof](docs/CN2_Tail_Coverage_Proof.md), Lemma B |
| $(q, a)$ tail | a prime above $q^*$ | `cn2tail.c`: $n = q(q + a\thinspace g(q))$ or $q(1 + a\thinspace g(q))$ | [tail proof](docs/CN2_Tail_Coverage_Proof.md), Lemma A |

Below $10^{28}$ the split used $T = 15{,}000$ and $q^* = 27{,}500{,}000$. The run took about 40 hours on 30 threads: 20.6 h capped, 12.6 h pair tail and 6.8 h $(q,a)$ tail. Every candidate from every engine is factorised and checked against the definition, and each find is classed as order 2 or Chebyshev only against the full modulus $p^2-1$.

## Checking it

```bash
pip install -r requirements.txt
python3 tests/check_cheb_terms.py results/b299799.txt     # every term against the definition, standard library only
python3 cn2_results_table.py --dir results/cert_1e28 --oeis results/A299799_oeis.json \
        --reference results/cert_1e28/reference_cheb_1e28.json   # the wide table, from the run's own result.json
```

`check_cheb_terms.py` factorises each term afresh by trial division and checks:
- that the term is odd, composite and squarefree;
- that it is a Carmichael number;
- the $(p^2-1)/2$ condition;
- the $\pm 1$ criterion separately.

It also reports which terms are of order 2.

The run records in `results/cert_1e28/` (and `results/cert_1e25/`) include:
- parameters (`split.json`);
- engine hashes (`ENGINES.sha256`);
- the completion records and shard logs of all three runs;
- the tail's raw survivors;
- the verified result (`result.json`, `verify.log`);
- the shard replay (`replay.log`).

The capped runs' raw survivor files (272 MB and 27 MB) are not included. The certificate §6 gives the commands to reproduce the run. `cn2_replay_run.py` replays sampled shards of a full run directory, built with the engines in `cn2x/`.

## Layout

| path | contents |
|---|---|
| `cn2x/` | the three engines (C), identical to those of the order-2 certificate |
| `cn2_split_campaign.py` | driver for the capped search (`init`, `run`, `verify`); in Chebyshev mode it classes each find as order 2 or Chebyshev only |
| `cn2_tail_verify.py`, `cn2_capped_peek.py` | verifiers for the tail and for a capped run in progress |
| `cn2_results_table.py` | the wide one-line-per-term table |
| `cn2_replay_run.py` | re-runs sampled production shards alone on one thread |
| `cn2_order2_defs.py` | the definitions (rigid, Howe, Chebyshev) and the candidate verifier |
| `docs/` | the two certificates ($10^{28}$, $10^{25}$) and the two proofs |
| `results/` | the terms (`b299799.txt`) and the run records |
| `tests/check_cheb_terms.py` | standalone check of a b-file |

## Licence

MIT; see `LICENSE`.
