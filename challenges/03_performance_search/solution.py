def find_common_elements(list_a: list[int], list_b: list[int]) -> list[int]:
    """Return sorted common elements (current version is intentionally inefficient)."""
    common: list[int] = []
    for item in list_a:
        if item in list_b:  # O(n*m)
            common.append(item)
    return sorted(common)

# --- START YOUR SOLUTION HERE ---
# Optimize the function so it scales efficiently with large inputs.
def find_common_elements_optimized(list_a: list[int], list_b: list[int]) -> list[int]:
    """Return sorted common elements."""
    set_list_b = set(list_b)
    common = [item for item in list_a if item in set_list_b]
    return sorted(common)

# --- END OF YOUR SOLUTION ---
