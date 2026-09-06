from DSA.Node.LinearNode import LinearNode
from DSA.Stack.Stack import Stack


def main() -> None:
    stack = Stack()
    nodes = [LinearNode(element) for element in (1, 2, 3)]

    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Stack size: {stack.size()}")

    for node in nodes:
        stack.push(node)
        print(f"Pushed: {node.get_element()}")

    print(f"Stack size after pushing: {stack.size()}")
    print(f"Top element: {stack.peek().get_element()}")
    print(f"Stack size after peeking: {stack.size()}")
    print(f"Stack: {stack.to_string()}")

    print("Popping elements:")
    while not stack.is_empty():
        print(stack.pop().get_element())

    print(f"Stack is empty: {stack.is_empty()}")
    print(f"Stack size after popping: {stack.size()}")
    print(f"Stack: {stack.to_string()}")

    try:
        stack.peek()
    except Exception as error:
        print(f"Empty stack error: {error}")


if __name__ == "__main__":
    main()
