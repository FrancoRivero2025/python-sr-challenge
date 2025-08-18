# Challenge 4: The Broken Context Manager

## Context
To safely manage resources like files or network connections, we use context managers (the with statement). We developed a TempFileManager class to handle temporary files, but it has a serious flaw: if an exception occurs inside the with block, the resource is not released, leaving orphaned files on the system.

## Your Task
Fix the TempFileManager class in solution.py. You must ensure that the __exit__ method guarantees the resource is cleaned up always, whether the operation succeeded or an exception occurred.

> Note: The starter implementation only cleans up when no exception occurs.

## How to Test
Run:
```bash
python toolkit.py test 04_broken_context_manager
```