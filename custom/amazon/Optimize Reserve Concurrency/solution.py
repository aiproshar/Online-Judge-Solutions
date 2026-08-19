from typing import List
import itertools
import random


class Solution:
    def optimizeReservedConcurrency(self, conc: List[int], price: List[int]) -> int:
        # TODO: implement
        pass






















































def brute(conc: List[int], price: List[int]) -> int:
    """Exponential reference. Only valid for tiny n and small values."""
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


CASES = [
    # (conc, price, expected, label)
    ([8, 6, 8],                  [9, 5, 7],                7,      "sample 0"),
    ([5, 2, 5, 3, 3],            [3, 7, 8, 6, 9],          9,      "sample 1"),
    ([1],                        [100000],                 0,      "n=1"),
    ([1, 2, 3, 4, 5],            [9, 9, 9, 9, 9],          0,      "already distinct"),
    ([4, 4, 4, 4],               [1, 2, 3, 4],             10,     "full collision"),
    ([1, 1, 1, 1, 1],            [5, 4, 3, 2, 1],          20,     "descending prices"),
    ([2, 2, 3, 3, 4, 4],         [10, 1, 10, 1, 10, 1],    9,      "cascading collisions"),
    ([7, 3, 7, 3, 7],            [2, 9, 4, 1, 8],          9,      "interleaved dups"),
    ([10, 10, 9, 9, 8, 8, 7, 7], [1, 2, 3, 4, 5, 6, 7, 8], 50,     "chained displacement"),
    ([10**9, 10**9],             [100000, 100000],         100000, "max value bound"),
]


def run_cases(sol) -> None:
    for conc, price, expected, label in CASES:
        got = sol.optimizeReservedConcurrency(list(conc), list(price))
        assert got == expected, f"{label}: conc={conc} price={price} expected {expected}, got {got}"
        print(f"  ok  {label}")


def run_stress(sol, trials: int = 2000, seed: int = 7) -> None:
    random.seed(seed)
    for _ in range(trials):
        n = random.randint(1, 4)
        conc = [random.randint(1, 5) for _ in range(n)]
        price = [random.randint(1, 9) for _ in range(n)]
        got = sol.optimizeReservedConcurrency(list(conc), list(price))
        exp = brute(conc, price)
        assert got == exp, f"stress: conc={conc} price={price} expected {exp}, got {got}"
    print(f"  ok  stress ({trials} random cases vs brute force)")


def run_perf(sol) -> None:
    import time
    random.seed(1)
    n = 10**5
    conc = [random.randint(1, 10**9) for _ in range(n)]
    price = [random.randint(1, 10**5) for _ in range(n)]
    t = time.time()
    sol.optimizeReservedConcurrency(conc, price)
    print(f"  ok  perf n={n} in {time.time() - t:.3f}s")

    conc = [500000] * n
    price = [10**5] * n
    t = time.time()
    r = sol.optimizeReservedConcurrency(conc, price)
    print(f"  ok  perf worst-case in {time.time() - t:.3f}s (answer {r}, needs 64-bit)")


if __name__ == "__main__":
    s = Solution()
    print("fixed cases:")
    run_cases(s)
    print("stress test:")
    run_stress(s)
    print("performance:")
    run_perf(s)
    print("\nall passed")