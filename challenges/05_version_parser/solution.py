def parse_version(version_string: str) -> tuple[int, int, int]:
    """Parse 'MAJOR.MINOR.PATCH' into a tuple of ints (current version not robust)."""
    parts = version_string.split('.')
    return int(parts[0]), int(parts[1]), int(parts[2])  # Fails on invalid formats

# --- START YOUR SOLUTION HERE ---
# Validate format and raise ValueError when invalid.
def parse_version_fixed(version_string: str) -> tuple[int, int, int]:
    """Parse 'MAJOR.MINOR.PATCH' into a tuple of ints with robust error handling."""
    
    if not version_string or version_string.strip() == '':
        raise ValueError("Invalid version format")
    
    version_parts = version_string.strip().split('.')

    if len(version_parts) != 3:
        raise ValueError("Invalid version format")
    
    for part in version_parts:
        if not part or not part.isdigit() or (len(part) > 1 and part.startswith('0')) or len(part) > 10:
            raise ValueError("Invalid version format")
       
    try:
        major = int(version_parts[0])
        minor = int(version_parts[1])
        patch = int(version_parts[2])
    except ValueError:
        raise ValueError("Invalid version format")
    
    if major < 0 or minor < 0 or patch < 0:
        raise ValueError("Invalid version format")
    
    return major, minor, patch
# --- END OF YOUR SOLUTION ---
