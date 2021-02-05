import pytest

from stack import Stack

# Test cases for an empty stack


def test_empty_stack_cannot_be_popped():
    stack = Stack()

    with pytest.raises(ValueError):
        stack.pop()


def test_empty_stack_has_no_top():
    stack = Stack()

    with pytest.raises(ValueError):
        top = stack.top


def test_empty_stack_has_depth_0():
    assert Stack().depth == 0


def test_empty_stack_acquires_depth_1_when_element_is_pushed():
    stack = Stack()

    stack.push(3)

    assert stack.depth == 1


def test_empty_stack_retains_pushed_element_as_its_top():
    stack = Stack()

    stack.push("test")

    assert stack.top == "test"


def test_stack_created_from_iterable_has_depth_equal_to_the_depth_of_this_iterable():
    stack = Stack(["John", "Marry", "Jane"])

    assert stack.depth == 3


def test_stack_created_from_iterable_has_top_equal_to_last_element_of_iterable():
    stack = Stack("abcde")

    assert stack.top == "e"


def test_popping_elements_from_stack_created_from_an_iterable_returns_them_in_reversed_order():
    stack = Stack((1, 2, 3))

    assert [stack.pop() for _ in range(3)] == [3, 2, 1]


def test_pushing_element_to_nonempty_stack_increases_depth_and_sets_this_element_as_top():
    stack = Stack([4, 2, 0])

    stack.push(-1)

    assert stack.depth == 4
    assert stack.top == -1


@pytest.mark.parametrize(
    "initial_stack, expected_element",
    [
        (Stack([1, 2, 3]), 3),
        (Stack([0]), 0)
    ]
)
def test_popping_element_from_nonempty_stack_decreases_depth_and_returns_last_element(
    initial_stack, expected_element
):
    initial_depth = initial_stack.depth
    assert initial_stack.pop() == expected_element
    assert initial_stack.depth == initial_depth - 1