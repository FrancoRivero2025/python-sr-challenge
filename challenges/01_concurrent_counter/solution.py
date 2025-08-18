import time

DELAY_SECONDS = 0.002

class Counter:
    """Non thread-safe counter (starter implementation)."""
    def __init__(self):
        self.count = 0

    def increment(self):
        current = self.count
        time.sleep(DELAY_SECONDS)
        self.count = current + 1

# --- START YOUR SOLUTION HERE ---
# Make this counter thread-safe without changing its public API.
# --- END OF YOUR SOLUTION ---
