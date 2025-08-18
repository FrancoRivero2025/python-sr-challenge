import threading
import random
import time

from solution import Counter


def increment_counter_n_times(counter, n):
    """Function to be executed by each thread."""
    for _ in range(n):
        counter.increment()


def test_counter_is_thread_safe():
    """
    This test creates multiple threads to increment the counter simultaneously.
    If the counter is not thread-safe, the final value will be less than expected
    due to race conditions.
    The test is repeated several times to increase the chance of catching race conditions.
    """
    num_threads = 10
    increments_per_thread = 20
    expected_count = num_threads * increments_per_thread
    repetitions = 5
    for i in range(repetitions):
        counter = Counter()
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=increment_counter_n_times, args=(counter, increments_per_thread))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        assert counter.count == expected_count, \
            f"[Iteration {i+1}] The counter ended at {counter.count}, but {expected_count} was expected. This indicates a race condition."


def test_counter_high_contention():
    threads = 25
    increments_per_thread = 40
    expected = threads * increments_per_thread
    counter = Counter()

    def worker():
        for _ in range(increments_per_thread):
            # Pequeño jitter para variar interleaving
            if random.random() < 0.2:
                time.sleep(0.0005)
            counter.increment()

    t_list = [threading.Thread(target=worker) for _ in range(threads)]
    for t in t_list: t.start()
    for t in t_list: t.join()

    assert counter.count == expected, f"High contention test lost increments: {counter.count} != {expected}"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
