# Python Senior Challenge

Welcome to the **Python Senior Challenge** repository! This project is designed to test and improve your advanced Python skills, with a strong focus on debugging and developing simple yet effective strategies for complex problems.

## What is this?

This repository contains a series of challenges aimed at senior Python developers. Each challenge is crafted to:

- Assess your debugging abilities.
- Encourage you to find simple, innovative solutions to tricky problems.
- Help you practice and demonstrate your expertise in Python.

## Environment & Dependency Management

We use [Poetry](https://python-poetry.org/docs/#installation) for dependency management and virtual environments. If you don't have Poetry installed, please follow the [official installation guide](https://python-poetry.org/docs/#installation).

## Toolkit CLI

The `toolkit.py` script provides a set of helpful commands to interact with the challenges:

- **List all challenges:**

  ```bash
  python toolkit.py list
  ```

- **Show documentation for a specific challenge:**

  ```bash
  python toolkit.py show <challenge_name>
  ```

- **Run the tests for a challenge (start here):**

  ```bash
  python toolkit.py test <challenge_name>
  ```

- **Run tests for ALL challenges (summary):**

  ```bash
  python toolkit.py test_all
  ```

- **Show diff vs reference answer for one challenge (if answers/ presente localmente):**

  ```bash
  python toolkit.py diff <challenge_name>
  ```

- **Show diffs for ALL challenges (only those con diferencias):**

  ```bash
  python toolkit.py diff_all
  ```

Notas:

- La carpeta `answers/` (ignorada por git) contiene soluciones de referencia para uso interno de reclutadores.
- Los comandos `diff` y `diff_all` comparan `challenges/<name>/solution.py` contra `answers/<name>/solution.py`.

## Tips

- Start by running the test for a challenge to understand the failure and current issues.
- Read the provided documentation for each challenge in its README.
- Favor clear, minimal, y robust solutions.
- Usa `test_all` al final para confirmar que no rompiste otros challenges.

Happy hacking!
