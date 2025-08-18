import time
import pytest
from solution import find_common_elements  # changed import


def test_find_common_elements_correctness():
    """Checks that the function returns the correct result."""
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    expected = [4, 5]
    assert find_common_elements(list_a, list_b) == expected

    list_c = [1, 2, 3]
    list_d = [4, 5, 6]
    assert find_common_elements(list_c, list_d) == []


def test_performance_on_large_lists():
    """
    This test checks performance. The original implementation
    will be too slow and will not pass the test (timeout).
    """
    # Create two large lists with no common elements for the worst case.
    large_list_a = list(range(50_000))
    large_list_b = list(range(50_000, 100_000))

    start_time = time.time()
    find_common_elements(large_list_a, large_list_b)
    duration = time.time() - start_time

    # An efficient solution (O(n+m)) should take much less than 0.1 seconds.
    # The inefficient solution (O(n*m)) would take minutes.
    assert duration < 0.1, f"The function is too slow ({duration:.4f}s). Check the algorithm's complexity."


def test_performance_larger_overlap():
    """Performance when there is a large overlap—should also be fast."""
    large_list_a = list(range(100_000))
    large_list_b = list(range(50_000, 150_000))  # 50k overlap
    start = time.time()
    result = find_common_elements(large_list_a, large_list_b)
    duration = time.time() - start
    # Expect 50k common elements
    assert len(result) == 50_000
    assert duration < 0.2, f"Large-overlap performance too slow: {duration:.4f}s"


def test_duplicates_preserved_from_first_list():
    list_a = [1, 2, 2, 3, 4, 4, 4]
    list_b = [2, 4]
    # Esperamos conservar duplicados tal como aparecen en list_a
    assert find_common_elements(list_a, list_b) == [2, 2, 4, 4, 4]
