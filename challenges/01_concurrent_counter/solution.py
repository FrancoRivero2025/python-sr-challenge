import time
import threading

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
class ThreadSafeCounter(Counter):
    """
    Counter with safe-thread increment in multithreaded environments.
    """

    def __init__(self):
        """
        Initialize a new ThreadSafeCounter instance.
        """
        super().__init__()
        self._lock = threading.Lock()
    
    def increment(self):
        """
        Increase counter safely.
        """
        with self._lock:
            super().increment()
# --- END OF YOUR SOLUTION ---
