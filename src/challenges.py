"""Week 5 homework: Midnight Mail Train.

Complete the required functions and classes.
Use recursion only where the instructions require recursion.
"""

from __future__ import annotations


class TrainCarNode:
    """A node in a doubly linked list of train cars."""

    def __init__(self, car_id: str) -> None:
        self.car_id = car_id
        self.prev: TrainCarNode | None = None
        self.next: TrainCarNode | None = None


class MidnightMailDLL:
    """A doubly linked list for train cars."""

    def __init__(self) -> None:
        self.head: TrainCarNode | None = None
        self.tail: TrainCarNode | None = None

    def append_car(self, car_id: str) -> None:
        """Add a train car to the end of the list."""
        raise NotImplementedError

    def detach_last_car(self) -> str | None:
        """Remove the last train car and return its ID.

        Return None if the list is empty.
        """
        raise NotImplementedError

    def to_reverse_list(self) -> list[str]:
        """Return all train car IDs from tail to head."""
        raise NotImplementedError


def is_valid_ticket_code(code: str) -> bool:
    """Return True only if the code starts with 'MM-' and ends with exactly 4 digits."""
    raise NotImplementedError



def count_priority_labels(labels: list[str], target: str) -> int:
    """Recursively count how many times target appears in labels."""
    raise NotImplementedError



def clean_radio_message(message: str) -> str:
    """Recursively return a new string with all spaces removed."""
    raise NotImplementedError


# Optional stretch

def count_priority_labels_iterative(labels: list[str], target: str) -> int:
    """Optional stretch: iterative version of count_priority_labels."""
    raise NotImplementedError



def clean_radio_message_iterative(message: str) -> str:
    """Optional stretch: iterative version of clean_radio_message."""
    raise NotImplementedError