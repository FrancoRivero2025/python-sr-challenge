def parse_version(version_string: str) -> tuple[int, int, int]:
    """Parse 'MAJOR.MINOR.PATCH' into a tuple of ints (current version not robust)."""
    parts = version_string.split('.')
    return int(parts[0]), int(parts[1]), int(parts[2])  # Fails on invalid formats

# --- START YOUR SOLUTION HERE ---
# Validate format and raise ValueError when invalid.
# --- END OF YOUR SOLUTION ---
