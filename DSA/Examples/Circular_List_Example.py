from DSA.Collections.Lists.Circular_List import Circular_List
from DSA.Node.LinearNode import LinearNode


def josephus(participants: list[str], step: int) -> tuple[list[str], str]:
    """Return the Josephus elimination order and final survivor."""
    if not participants:
        raise ValueError("participants must not be empty")
    if step < 1:
        raise ValueError("step must be at least 1")

    circle = Circular_List()
    for participant in participants:
        circle.add(LinearNode(participant))

    eliminated = []
    current = circle.first()

    while circle.size() > 1:
        for _ in range(step - 1):
            current = current.get_next()

        next_node = current.get_next()
        removed = circle.remove(current)
        eliminated.append(removed.get_element())
        current = next_node

    return eliminated, circle.first().get_element()


def main() -> None:
    participants = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace"]
    step = 3

    eliminated, survivor = josephus(participants, step)

    print(f"Participants: {', '.join(participants)}")
    print(f"Eliminate every {step}rd participant")
    print(f"Elimination order: {' -> '.join(eliminated)}")
    print(f"Survivor: {survivor}")


if __name__ == "__main__":
    main()
