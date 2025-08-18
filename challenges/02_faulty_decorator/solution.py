from functools import wraps

# --- START YOUR SOLUTION HERE ---
# Implement a decorator factory `limit_calls(max_calls)`.
# Each decorated function must enforce its own call limit.
# Placeholder (incorrect): shared counter.

def limit_calls(max_calls: int):
    calls = 0
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise ValueError(f"Limit of {max_calls} calls exceeded for {func.__name__}")
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
# --- END OF YOUR SOLUTION ---
