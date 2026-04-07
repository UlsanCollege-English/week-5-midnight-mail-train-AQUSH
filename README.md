# Week 5 — Midnight Mail Train

## Summary
This assignment implements a doubly linked list to manage train cars in a "Midnight Mail Train" system. It includes operations to add and remove cars, traverse the train in reverse, validate ticket codes, and process messages. Recursion is used for counting labels and cleaning messages as required.

## Approach
- Problem 1:
  Implemented a doubly linked list with head and tail pointers. Added `append_car` to insert at the end and `detach_last_car` to safely remove the last node.

- Problem 2:
  Traversed the list backwards using the `prev` pointer to return all car IDs from tail to head.

- Problem 3:
  Validated ticket codes by checking if they start with `"MM-"` and end with exactly four digits.

- Problem 4:
  Used recursion to count occurrences of a target label and to remove spaces from a message string.

## Complexity
- append_car:
  Time: O(1)  
  Space: O(1)  
  Reason: Direct insertion at tail without traversal.

- detach_last_car:
  Time: O(1)  
  Space: O(1)  
  Reason: Direct removal using tail pointer.

- to_reverse_list:
  Time: O(n)  
  Space: O(n)  
  Reason: Traverses all nodes once and stores results.

- is_valid_ticket_code:
  Time: O(1)  
  Space: O(1)  
  Reason: Fixed-length checks and string operations.

- count_priority_labels (recursive):
  Time: O(n)  
  Space: O(n)  
  Reason: Processes each element once with recursion stack.

- clean_radio_message (recursive):
  Time: O(n)  
  Space: O(n)  
  Reason: Processes each character with recursion stack.

## Edge-case checklist
- [x] empty train
- [x] one train car
- [x] invalid ticket code
- [x] empty label list
- [x] empty message
- [x] one-character or all-space message

## Assistance & Sources
- AI used? Yes
- What it helped with:
  Helped implement functions, debug logic, and explain recursion clearly.
- Other sources used:
  Lecture notes and course materials