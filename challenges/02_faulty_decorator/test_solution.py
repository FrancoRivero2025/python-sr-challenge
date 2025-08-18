import pytest
import asyncio
from solution import limit_calls

def test_decorator_limits_calls_correctly_for_one_function():
    """Checks that the decorator works for a single function."""
    @limit_calls(3)
    def limited_func_a():
        return "A"

    assert limited_func_a() == "A"
    assert limited_func_a() == "A"
    assert limited_func_a() == "A"
    with pytest.raises(ValueError):
        limited_func_a()

def test_decorator_maintains_separate_state_for_multiple_functions():
    """
    This test is key. It checks that two functions decorated with `limit_calls`
    have independent counters. The original code will fail here.
    """
    @limit_calls(2)
    def limited_func_b():
        return "B"

    @limit_calls(1)
    def limited_func_c():
        return "C"

    # Calls to function B
    assert limited_func_b() == "B"
    assert limited_func_b() == "B"
    with pytest.raises(ValueError, match="Limit of 2 calls exceeded"):
        limited_func_b()

    # Call to function C, should work independently of B
    try:
        assert limited_func_c() == "C"
    except ValueError:
        pytest.fail("The call to limited_func_c failed. The decorator state seems to be shared.")

    # The next call to C should fail
    with pytest.raises(ValueError, match="Limit of 1 calls exceeded"):
        limited_func_c()

def test_decorator_independent_when_reusing_factory():
    """Even reusing the same decorator factory instance, each wrapped function should track its own calls."""
    decor = limit_calls(2)

    @decor
    def f1():
        return "X"

    @decor
    def f2():
        return "Y"

    # Exhaust f1
    assert f1() == "X"
    assert f1() == "X"
    with pytest.raises(ValueError, match="Limit of 2 calls exceeded"):
        f1()

    # f2 should still have full quota
    assert f2() == "Y"
    assert f2() == "Y"
    with pytest.raises(ValueError, match="Limit of 2 calls exceeded"):
        f2()

def test_method_independence_between_instances():
    class Service:
        def __init__(self, name):
            self.name = name

        @limit_calls(2)
        def ping(self):
            return f"pong:{self.name}"

    a = Service("A")
    b = Service("B")

    assert a.ping() == "pong:A"
    assert a.ping() == "pong:A"
    # a exhausted
    with pytest.raises(ValueError):
        a.ping()

    # b still fresh (should not be affected by a)
    assert b.ping() == "pong:B"
    assert b.ping() == "pong:B"
    with pytest.raises(ValueError):
        b.ping()

@pytest.mark.asyncio
async def test_async_function_limit():
    @limit_calls(2)
    async def do_async():
        await asyncio.sleep(0)
        return 42

    assert await do_async() == 42
    assert await do_async() == 42
    with pytest.raises(ValueError):
        await do_async()
