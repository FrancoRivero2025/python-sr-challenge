import pytest
from solution import parse_version_fixed as parse_version

def test_parse_valid_version():
    """Checks that a valid version string is parsed correctly."""
    assert parse_version("2.1.0") == (2, 1, 0)
    assert parse_version("10.0.15") == (10, 0, 15)

def test_parse_invalid_format_too_few_parts():
    """Checks that an error is raised if parts of the version are missing."""
    with pytest.raises(ValueError, match="Invalid version format"):
        parse_version("1.2")

def test_parse_invalid_format_too_many_parts():
    """Checks that an error is raised if there are too many parts in the version."""
    with pytest.raises(ValueError, match="Invalid version format"):
        parse_version("1.2.3.4")

def test_parse_invalid_format_non_numeric():
    """Checks that an error is raised if a part is not numeric."""
    with pytest.raises(ValueError, match="Invalid version format"):
        parse_version("1.a.3")

def test_parse_empty_string():
    """Checks that an empty string is handled correctly."""
    with pytest.raises(ValueError, match="Invalid version format"):
        parse_version("")

def test_whitespace_trimmed():
    """Checks that whitespace around the version string is ignored."""
    assert parse_version(" 2.3.4 ") == (2, 3, 4)

def test_leading_zero_parts_invalid_except_zero():
    """Checks that leading zeros in version parts are not allowed, except for the part '0'."""
    with pytest.raises(ValueError):
        parse_version("01.2.3")
    with pytest.raises(ValueError):
        parse_version("1.02.3")
    with pytest.raises(ValueError):
        parse_version("1.2.03")
    # Single zero is fine
    assert parse_version("0.0.0") == (0, 0, 0)

def test_prerelease_not_supported():
    """Checks that versions with prerelease tags are not supported."""
    with pytest.raises(ValueError):
        parse_version("1.2.3-alpha")

def test_excessive_length_rejected():
    """Checks that versions with excessively long parts are rejected."""
    long_part = "1" * 60
    with pytest.raises(ValueError):
        parse_version(f"{long_part}.2.3")
