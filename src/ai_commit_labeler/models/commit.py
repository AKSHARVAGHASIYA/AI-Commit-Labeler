"""
Commit data model.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Commit:
    """
    Represents a single GitHub commit to be reviewed.
    """

    repository: str
    sha: str
    commit_message: str
    changed_filenames: str
    file_summary: str
    patch_summary: str
    