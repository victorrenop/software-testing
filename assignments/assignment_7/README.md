# Assignment 7

## Description

Find five code examples that break the FIRST principles learned in class. If you can't find one, just create them.

## Solution

### Fast Principle

Using a bubble sorte code, for example, if the first test was the following:

```python
def test_bubble_sort(self):
    unordered_list = self.get_unordered_list()
    assert self.equals(bubble_sort(unordered_list), self.get_ordered_list())
```

Assuming that the method `get_unordered_list` returns a fixed and big list of unordered elements and that the method `get_ordered_list` returns the same list but corretly ordered, this test would be too slow for big arrays, since bubble sort has a quadratic complexity and the assert requires another pass through the arrays to confirm that the are equal.

To respect the Fast principle, the developer must declare only small fixed arrays to test the cases, assuming that for big arrays the result would be the same, which should be.

### Isolated Principle

An example that breaks this principle is seen in this repo, at the `assignment_5` tests folder. The first version of this tests declared the `game` object as a class object, using it in every test. The problem was that the tests where not isolated from each other, as the `game` object was modified in every test, the subsequent test gave a different result than expected.

The fix to comply with the Isolated principle was to the create the `game` object at the start of every test and not share it with the test class.

### Repeatable Principle

Using the `assignment_5` tests again, depending on the order that the tests where being executed, the results where different each time because of the shared `game` object. Since this object calculated the score and never reverted it to zero, each test would increment the score on a different way, returning a different result for each order of execution of the test.

Again, the solution was to isolate the `game` object creation.

### Self-Validating Principle

Using the following code as an exemple:

```python
def test_file(self):
    with open('test.txt', 'w') as file:
        file.write('Test')
```

The developer needs to check the file to see if the write is successful. This should not happen, an assert is necessary to yield an automatic test.

```python
def test_file(self):
    with open('test.txt', 'w') as file:
        file.write('Test')
    
    contents
    with open('test.txt', 'r') as file:
        contents = file.read()

    assert contents = "Test"
```

### Timely

Writing a production code first and than writing a test that fails, for exemple:

```python
def test_sum_arrays_null(self):
    assert self.sum_arrays([1,2], None) == [1, 2] 
```

Assuming the production code did not expect `None` being passed, a big refactor is necessary to pass this test. If the test was writen before, the refactoring work would be much less expensive.

