from src.challenges import (
    MidnightMailDLL,
    clean_radio_message,
    count_priority_labels,
    is_valid_ticket_code,
)


# Problem 1: DLL

def test_append_and_reverse_list_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    train.append_car("C3")
    assert train.to_reverse_list() == ["C3", "B2", "A1"]



def test_detach_last_car_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    assert train.detach_last_car() == "B2"
    assert train.to_reverse_list() == ["A1"]



def test_detach_last_car_empty() -> None:
    train = MidnightMailDLL()
    assert train.detach_last_car() is None


# Problem 2: ticket code
# Add at least 4 tests total:
# - 1 valid case
# - 2 invalid cases
# - 1 edge case


def test_ticket_code_valid_example() -> None:
    assert is_valid_ticket_code("MM-1234") is True


# TODO: add more tests for Problem 2


# Problem 3: recursion on a list

def test_count_priority_labels_basic() -> None:
    labels = ["PRIORITY", "NORMAL", "PRIORITY", "LATE"]
    assert count_priority_labels(labels, "PRIORITY") == 2



def test_count_priority_labels_empty() -> None:
    assert count_priority_labels([], "PRIORITY") == 0


# Problem 4: recursion on a string

def test_clean_radio_message_basic() -> None:
    assert clean_radio_message("go now") == "gonow"



def test_clean_radio_message_empty() -> None:
    assert clean_radio_message("") == ""