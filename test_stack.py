import pytest
from stack import Stack


def test_an_empty_stack_has_depth_equals_to_zero():
    stack = Stack()
    assert stack._depth == 0


def test_an_empty_stack_cannot_be_popped():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.pop()


def test_an_empty_stack_has_no_top():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.top()


def test_pushing_an_element_on_stack_results_in_increased_depth():
    stack = Stack(1)
    stack.push("a")
    assert stack._depth == 2


def test_pushing_an_element_on_stack_sets_this_element_as_top():
    stack = Stack(1)
    stack.push("a")
    assert stack.top == "a"


def test_popping_an_element_results_in_put_at_the_top_the_previous_one():
    stack = Stack(1, 2, 3)
    stack.pop()
    stack.pop()
    assert stack.top == 1


@pytest.mark.parametrize(
    "initial_stack, expected_element",
    [
        (Stack(1, 2, 3), 3),
        (Stack("c"), "c")
    ]
)
def test_popping_element_from_nonempty_stack_decreases_depth_and_returns_last_element(
    initial_stack, expected_element
):
    initial_depth = initial_stack._depth
    assert initial_stack.pop() == expected_element
    assert initial_stack._depth == initial_depth - 1


