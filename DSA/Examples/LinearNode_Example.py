from DSA.Node.LinearNode import LinearNode

if __name__ == "__main__":
        # Example usage of LinearNode with integer data.
    third_node = LinearNode(3)
    second_node = LinearNode(2, third_node)
    first_node = LinearNode(1, second_node)

    print(first_node.get_data())
    print(first_node.get_next().get_data())
    print(first_node.get_next().get_next().get_data())

    print(
        f"First node ({first_node.get_data()}) is less than "
        f"second node ({second_node.get_data()}): "
        f"{first_node < second_node}"
    )
    print(repr(first_node))

    # Example usage of LinearNode with string data.
    first_node.set_data("abc")
    second_node.set_data("xyz")

    print(first_node.get_data())
    print(first_node.get_next().get_data())
    print(
        f"First node ({first_node.get_data()}) is less than "
        f"second node ({second_node.get_data()}): "
        f"{first_node < second_node}"
    )
