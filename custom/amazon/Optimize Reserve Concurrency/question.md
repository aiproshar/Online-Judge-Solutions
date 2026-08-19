# Code Question 2 — Optimize Reserved Concurrency

You're the on-call SDE for a serverless production stack. The architecture includes `n` AWS Lambda functions, and each function `i` currently has a reserved-concurrency limit of `conc[i]`. Because burst load on one function can starve others, your principal engineer asks that every function end up with a **distinct** concurrency limit.

- In one operation you may raise function `i`'s limit by exactly **1**, incurring a cost of `price[i]` (the cost reflects additional provisioned-concurrency dollars).

Limits may only be **raised**, never lowered. There is no upper bound on how high a limit may go.

## Example

```
n     = 5
conc  = [5, 2, 5, 3, 3]
price = [3, 7, 8, 6, 9]
```

An optimal sequence:

- Bump function 0 (`conc[0]`) from 5 → 6 (cost 3).
- Bump function 3 (`conc[3]`) from 3 → 4 (cost 6).

The final limits `[6, 2, 5, 4, 3]` are all different; total cost = 3 + 6 = **9**, which is minimal.

## Function Description

Complete the function `optimizeReservedConcurrency` below.

`optimizeReservedConcurrency` takes the following inputs:

- `int conc[n]`: the current reserved-concurrency for each lambda
- `int price[n]`: cost to increase that lambda's limit by 1

### Returns

- `long`: the minimum dollars required to make all `conc` values unique

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ conc[i] ≤ 10^9
- 1 ≤ price[i] ≤ 10^5

## Input Format for Custom Testing

```
line 1        : n            (size of conc[])
lines 2..n+1  : conc[i]
line n+2      : n            (size of price[])
lines n+3..   : price[i]
```

## Sample Case 0

**Sample Input**

```
3
8
6
8
3
9
5
7
```

**Sample Output**

```
7
```

**Explanation**

Increase the third function once (8 → 9) for cost 7; the limits `[8, 6, 9]` are now unique.

## Sample Case 1

**Sample Input**

```
5
5
2
5
3
3
5
3
7
8
6
9
```

**Sample Output**

```
9
```

**Explanation**

Bump function 0 from 5 → 6 (cost 3) and function 3 from 3 → 4 (cost 6). Total = 9.

---

## Additional Test Cases

Use these to check your implementation. All outputs verified against exhaustive search on the small cases.

| # | `conc` | `price` | Expected | What it tests |
|---|--------|---------|----------|---------------|
| 1 | `[1]` | `[100000]` | `0` | n = 1, already unique |
| 2 | `[1,2,3,4,5]` | `[9,9,9,9,9]` | `0` | already distinct, no work |
| 3 | `[4,4,4,4]` | `[1,2,3,4]` | `10` | full collision, cheap ones pushed furthest |
| 4 | `[1,1,1,1,1]` | `[5,4,3,2,1]` | `20` | prices strictly decreasing |
| 5 | `[2,2,3,3,4,4]` | `[10,1,10,1,10,1]` | `9` | cascading collisions into occupied slots |
| 6 | `[7,3,7,3,7]` | `[2,9,4,1,8]` | `9` | interleaved duplicates, unsorted prices |
| 7 | `[10,10,9,9,8,8,7,7]` | `[1,2,3,4,5,6,7,8]` | `50` | descending input, chained displacement |
| 8 | `[1000000000,1000000000]` | `[100000,100000]` | `100000` | max value bound, no overflow of slot space |

### Traps to watch for

- **Return type.** Worst case is on the order of 10^15 — a 32-bit accumulator overflows. Use 64-bit.
- **Don't index by value.** `conc[i]` reaches 10^9, so any counting array or bucket sweep over the value range blows memory and time. Everything must scale with `n`, not with `max(conc)`.
- **Ties in price.** When two eligible functions share the same price, either may take the slot — the total is the same. Don't let a tiebreak assumption sneak into your correctness argument.
- **Case 5 is the discriminator.** A solution that only looks at duplicate groups in isolation, without accounting for a bumped value colliding with an already-occupied slot further up, will get this one wrong.

---

## Stress-Test Harness

If you want to check yourself against exhaustive search, this brute force is correct but exponential — keep `n ≤ 4` and values small.

```python
import itertools

def brute(conc, price):
    n = len(conc)
    hi = max(conc) + n + 1
    best = None
    for combo in itertools.product(range(min(conc), hi), repeat=n):
        if len(set(combo)) != n:
            continue
        if any(combo[i] < conc[i] for i in range(n)):
            continue
        c = sum(price[i] * (combo[i] - conc[i]) for i in range(n))
        if best is None or c < best:
            best = c
    return best
```

Generate random `conc` in `[1,5]` and `price` in `[1,9]` with `n` in `[1,4]`, and compare against your solution over a few thousand trials.