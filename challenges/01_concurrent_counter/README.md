# Challenge 1: The Concurrent Counter

## Context

In our application, we have a metrics counter that is accessed simultaneously by multiple threads. We've noticed that under high load, the counter misses some increments and reports an incorrect final value. This suggests the presence of a race condition.

## Your Task

Your mission is to debug and fix the counter implementation in solution.py to make it thread-safe. The counter must handle concurrent increments without losing operations.

The ideal solution is concise and demonstrates a clear understanding of synchronization primitives.

> Note: The starter implementation (`Counter`) is intentionally not thread-safe.

## How to Test
Run:
```bash
python toolkit.py test 01_concurrent_counter
```
