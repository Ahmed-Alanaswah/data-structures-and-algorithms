# Data Structures and Algorithms

## Language: `Python`

### Folder and Challenge Setup

Each type of code challenge has slightly different instructions. Please refer to the notes and examples below for instructions for each DS&A assignment type.

### Data Structure: New Implementation

- Create a new folder under the `python` level, with the name of the data structure and complete your implementation there
  - i.e. `linked_list`
- Implementation (the data structure "class")
  - The implementation of the data structure should match package name
    - i.e. `linked_list/linked_list.py`
  - Follow Python [naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

    ```python
    class LinkedList:
      def __init__(self):
        # ... initialization code

      def method_name(self):
        # method body
    ```

- Tests
  - Within folder `tests` create a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Your tests will then need to require the data structure you're testing
      - i.e. `from linked_list.linked_list import LinkedList`

### Data Structure: Extending an implementation

- Work within the existing data structure implementation
- Create a new method within the class that solves the code challenge
  - Remember, you'll have access to `self` within your class methods
- Tests
  - You will have folder named `tests` and within it, a test file called `test_[data_structure].py`
    - i.e. `tests/test_linked_list.py`
    - Add to the tests written for this data structure to cover your new method(s)

### Code Challenge / Algorithm

Code challenges should be completed within a folder named `code_challenges` under the `python` level

- Daily Setup:
  - Create a new folder under the `python` level, with the name of the code challenge
    - Each code challenge assignment identifies the branch name to use, for example 'find-maximum-value'
    - For clarity, create your folder with the same name, ensuring that it's `snake_cased`
    - i.e. For a challenge named 'find_maximum_value', create the folder:`code_challenges/find_maximum_value`
  - Code Challenge Implementation
    - Each code challenge requires a function be written, for example "find maximum value"
    - Name the actual challenge file with the name of the challenge, in `snake_case`
      - i.e. `find_maximum_value.py`
    - Reminder: Your challenge file will then need to require the data structure you're using to implement
      - i.e. `from linked_list.linked_list import LinkedList`
    - Your challenge function name is up to you, but name something sensible that communicates the function's purpose. Obvious is better than clever
      - i.e. `find_maximum_value(linked_list)`
  - Tests
    - Ensure there is a `tests` folder at the root of project.
      - i.e. a sibling of this document.
    - within it, a test file called `test_[challenge].py`
      - i.e. `tests/find_maximum_value.py`
      - Your test file would require the challenge file found in the directory above, which has your exported function
        - i.e. `from code_challenges.find_maximum_value import find_maximum_value`

## Running Tests

If you setup your folders according to the above guidelines, running tests becomes a matter of deciding which tests you want to execute.  Jest does a good job at finding the test files that match what you specify in the test command

From the root of the `data-structures-and-algorithms/python` folder, execute the following commands:

- **Run every possible test** - `pytest`
- **Run filtered tests** - `pytest -k some_filter_text`
- **Run in watch mode** - `ptw` or `pytest-watch`


## code_chalenges:
1. **de1_reverse_Array:**[reverse_Array](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/reverse_linked_list/README.md)
2. **e2_array-insert-shift**:[array-insert-shift](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/array-insert-shift/README.md)
3. **printNthFromLast**:[printNthFromLast]( https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/linked_list)
4. **zip functiont**:[zip function](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/linked_list_zip)
5. **stack-queue-pseudo:**[*stack-queue-pseudo](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/stack-queue-pseudo#readme)
6. **stack-queue-animal-shelter**:[stack-queue-animal-shelter](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/stack-queue-animal-shelter)
7. **stack-queue-brackets**:[stack-queue-brackets](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/stack-queue-brackets#readme)
8. **Tree**:[Tree](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/trees)
9. **max tree value**:[max tree value](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/tree-max)
10. **tree breadth first**: [tree breadth first](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/tree-breadth-first)
11. **fizz buzz function**:[fizz-buzz-function](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/tree-fizz-buzz#readme)
12. **sort array and verfiying code (code 26)** :[sort array and verfiying code (code 26)](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/sort-list/BLOG.md)
13. **MERGE SORTED ARRAY**:[MERGE SORTED ARRAY](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/merge-sorted-list/BLOG.md)
14. **quick sort**:[quick sort algorithms](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/QuickSort/BLOG.md)
15. **hash map repeated first word**: [hash map repeated first word](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/hashmap-repeated-word/README.md)
16. **tree interaction**: [tree interaction](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/tree/main/python/tree-intersection#readme)
17. **left join**:[left join ](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/hashmap-left-join/README.md)
18. **graph**:[graph](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/pull/58)
19. **bfs**:[bfs](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/graph/README.md)
20. **buisniss trip**:[buisniss trip](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/pull/60)
21. **deep first method**:[deep first method](https://github.com/Ahmed-Alanaswah/data-structures-and-algorithms/blob/main/python/graph/README2.md)
