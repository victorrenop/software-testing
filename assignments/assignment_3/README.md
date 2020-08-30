# Assignment 3

## Definition

Define equivalence classes and a set of suitable test cases for the equivalence criteria for equivalence classes for the program with the following description:

The program must determine whether an identifier is valid or not in Silly Pascal (a variant of Pascal). A valid identifier must << start with a letter and contain only letters or digits >>. In addition, << must be a minimum of one character and a maximum of six characters in length >>.

Implement the isValid (string): boolean function that takes a string and returns true if the string can be a Silly Pascal identifier and false otherwise. Create the tests for this function.

## Equivalence Classes and Test Cases

| Input Condition | Valid Classes | Invalid Classes |
| ------ | ------ | ------ |
| Starts with letter | Yes(1) | No (2) |
| Contains only letters and digits | Yes(3) | No (4) |
| String is null | No(5) | Yes (6) |
| String len | 1 <= len(string) <= 6 (7) | len(string) < 1 (8) <br> len(string) > 6 (9) |

| Test Case | Classes Covered | Limits Covered |
| ------ | ------ | ------ |
| ("a12", True) | {1, 3, 5, 7} |  |
| ("a", True) | {1, 3, 5, 7} | len(string) = 1 |
| ("abcde1", True) | {1, 3, 5, 7} | len(string) = 6 |
| ("12", False) | {2} |  |
| ("a12#", False) | {4} |  |
| (None, False) | {6} |  |
| ("", False) | {8} |  |
| ("abcdef1", False) | {9} | len(string) = 7 |