from functools import wraps

# --- START YOUR SOLUTION HERE ---
# Implement a decorator factory `limit_calls(max_calls)`.
# Each decorated function must enforce its own call limit.
# Placeholder (incorrect): shared counter.

def limit_calls(max_calls: int):
    def decorator(func): # There is a potential issue: memory leak if there are many instances. But you requested a simple fix. 
        call_map = {}
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = args[0] if args and hasattr(args[0], "__class__") else func
            
            if key not in call_map:
                call_map[key] = 0
                
            if call_map[key] >= max_calls:
                raise ValueError(f"Limit of {max_calls} calls exceeded for {func.__name__}")
                
            call_map[key] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
# --- END OF YOUR SOLUTION ---
