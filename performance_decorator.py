from time import time

# Decorator to measure performance
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} seconds')
        return result
    return wrapper

@performance
def long_time():
    """Benchmarking function to test performance."""
    for _ in range(10_000_000):
        pass  # Empty loop for benchmarking the decorator

# Execute the benchmark
long_time()
