# Challenge 5: The Incomplete Version Parser

## Context
We need a function to parse software version strings (e.g., "2.1.10"). The current implementation, parse_version, works for the happy path but is fragile and crashes abruptly when the input doesn't have the expected format. A robust function is essential to prevent unexpected crashes in production.

## Your Task
Harden the parse_version function in solution.py to make it resilient. It must correctly handle edge cases and invalid formats (e.g., "1.2", "1.a.3", empty strings) by raising a ValueError instead of crashing uncontrollably. You should not use external libraries.

> Note: The starter implementation performs no validation and is intentionally incomplete.

## How to Test
Run:
```bash
python toolkit.py test 05_version_parser
```
