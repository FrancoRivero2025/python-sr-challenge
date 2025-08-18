import os

class Constants:
    """
    Constants for the challenge toolkit.
    """

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CHALLENGES_DIR = os.path.join(BASE_DIR, "challenges")