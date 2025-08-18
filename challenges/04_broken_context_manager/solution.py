class TempFileManager:
    """Minimal temp file context manager (current cleanup logic is incorrect)."""

    def __init__(self, filename):
        self._filename = filename
        self._temp_file = None

    def __enter__(self):
        self._temp_file = self._filename
        return self._temp_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Current behavior: only cleans if no exception (bug placeholder)
        if exc_type is None:
            self._temp_file = None

    @property
    def file_is_open(self):
        return self._temp_file is not None

# --- START YOUR SOLUTION HERE ---
# Ensure cleanup always happens and exceptions are not suppressed.
# --- END OF YOUR SOLUTION ---
