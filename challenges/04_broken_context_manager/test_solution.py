import pytest
from solution import TempFileManager

def test_context_manager_cleans_up_on_success():
    """Checks that the file is cleaned up if there are no errors."""
    manager = TempFileManager("test.txt")
    with manager:
        assert manager.file_is_open is True
    assert manager.file_is_open is False

def test_context_manager_cleans_up_on_exception():
    """
    This test is key. It checks that the resource is cleaned up
    even when an exception occurs inside the `with` block.
    The original implementation will fail this assertion.
    """
    manager = TempFileManager("error_test.txt")
    try:
        with manager:
            assert manager.file_is_open is True
            raise ValueError("Simulating an error in the operation")
    except ValueError:
        # The error is expected, now we check the manager's state.
        pass

    assert manager.file_is_open is False, \
        "The context manager did not clean up the resource after an exception."

def test_nested_contexts_independent_cleanup():
    outer = TempFileManager("outer.txt")
    inner = TempFileManager("inner.txt")
    with outer:
        assert outer.file_is_open is True
        with inner:
            assert inner.file_is_open is True
        # inner must be closed after its block
        assert inner.file_is_open is False
    # outer closed after exiting outer block
    assert outer.file_is_open is False
