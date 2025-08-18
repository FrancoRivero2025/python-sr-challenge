# Challenge 2: The Faulty State Decorator

## Context
We created a @limit_calls decorator intending to restrict how many times a function can be executed. However, when applying it to multiple functions, we discovered a critical bug: the call count state is shared across all decorated functions, instead of each function having its own limit.

## Your Task
You must fix the @limit_calls decorator in solution.py. The goal is for each decorated function to maintain its own call counter independently. You cannot use global variables to store the counters.

This challenge assesses your mastery of decorators, closures, and state management in Python.

> Note: The starter implementation shares state intentionally and is incorrect.

## How to Test
Run:
```bash
python toolkit.py test 02_faulty_decorator
```
