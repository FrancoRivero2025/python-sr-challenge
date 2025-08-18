from .constants import Constants
import os
import subprocess
import difflib

def get_challenges() -> list:
    """Get a list of all challenges in the challenges directory."""

    try:
        return sorted([
            d for d in os.listdir(Constants.CHALLENGES_DIR)
            if os.path.isdir(os.path.join(Constants.CHALLENGES_DIR, d)) and not d.startswith("__")
        ])
    except FileNotFoundError:
        print(f"Error: The challenges directory '{Constants.CHALLENGES_DIR}' does not exist.")
        return []

def get_readme(name: str) -> str | None:
    """Get the content of the README.md file for a specific challenge."""

    readme_path = os.path.join(Constants.CHALLENGES_DIR, name, "README.md")
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: README.md file for challenge '{name}' not found at '{readme_path}'.")
        return None
    except Exception as e:
        print(f"Error reading README.md for challenge '{name}': {e}")
        return None

def run_solution(name: str) -> tuple[str, int]:
    """Run the test suite (pytest) for a specific challenge and return output + exit code."""
    challenge_dir = os.path.join(Constants.CHALLENGES_DIR, name)
    test_file = os.path.join(challenge_dir, "test_solution.py")
    if not os.path.exists(test_file):
        return f"Error: test file for challenge '{name}' not found at '{test_file}'.", 2

    # Run pytest directly so assertions execute (instead of running the file as a plain script).
    # We keep full output (no -q) to show details on failure; success output stays concise by default.
    cmd = ["pytest", test_file]
    result = subprocess.run(cmd, capture_output=True, text=True)
    output = (result.stdout or "") + ("\n" if result.stdout and result.stderr else "") + (result.stderr or "")
    return output.strip(), result.returncode

def get_solution_diff(name: str) -> tuple[str, int]:
    """Return unified diff between challenge solution and answer solution.

    Exit codes semantics:
      0 -> No differences (identical or answer exists and match)
      1 -> Differences found
      2 -> Answer file missing
      3 -> Challenge solution file missing
    """
    challenge_solution = os.path.join(Constants.BASE_DIR, "challenges", name, "solution.py")
    answer_solution = os.path.join(Constants.BASE_DIR, "answers", name, "solution.py")

    if not os.path.exists(answer_solution):
        return f"Answer solution not found at {answer_solution}", 2
    if not os.path.exists(challenge_solution):
        return f"Challenge solution not found at {challenge_solution}", 3

    with open(challenge_solution, 'r', encoding='utf-8') as f:
        challenge_lines = f.readlines()
    with open(answer_solution, 'r', encoding='utf-8') as f:
        answer_lines = f.readlines()

    diff_lines = list(difflib.unified_diff(
        challenge_lines,
        answer_lines,
        fromfile=challenge_solution,
        tofile=answer_solution
    ))
    if not diff_lines:
        return "No differences.", 0
    return ''.join(diff_lines), 1
