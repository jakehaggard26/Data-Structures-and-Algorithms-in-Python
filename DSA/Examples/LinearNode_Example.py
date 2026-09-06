from DSA.Node.LinearNode import LinearNode

if __name__ == "__main__":
        # Example usage of LinearNode with integer elements.
    third_node = LinearNode(3)
    second_node = LinearNode(2, third_node)
    first_node = LinearNode(1, second_node)

    print(first_node.get_element())
    print(first_node.get_next().get_element())
    print(first_node.get_next().get_next().get_element())

    print(
        f"First node ({first_node.get_element()}) is less than "
        f"second node ({second_node.get_element()}): "
        f"{first_node < second_node}"
    )
    print(repr(first_node))

    # Example usage of LinearNode with string elements.
    first_node.set_element("abc")
    second_node.set_element("xyz")

    print(first_node.get_element())
    print(first_node.get_next().get_element())
    print(
        f"First node ({first_node.get_element()}) is less than "
        f"second node ({second_node.get_element()}): "
        f"{first_node < second_node}"
    )
