import argparse


def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 1 or n == 0:
        return n        

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the nth fibonacci number.")
    parser.add_argument(
        "n", type=int, help="The position of the fibonacci sequence to calculate"
    )

    args = parser.parse_args()

    result = fibonacci(args.n)

    print(f"Fibonacci number at position {args.n} is {result}")
