from functools import total_ordering

from DSA.Collections.Lists.Ordered_List import Ordered_List
from DSA.Node.LinearNode import LinearNode


@total_ordering
class DispatchTicket:
    """A dispatch ticket ordered by its numeric severity or wait time."""

    def __init__(self, ticket_id: str, description: str, priority: int):
        self.ticket_id = ticket_id
        self.description = description
        self.priority = priority

    def __eq__(self, other):
        if not isinstance(other, DispatchTicket):
            return NotImplemented
        return self.priority == other.priority

    def __lt__(self, other):
        if not isinstance(other, DispatchTicket):
            return NotImplemented
        return self.priority < other.priority

    def __str__(self):
        return f"{self.ticket_id}: {self.description} (priority {self.priority})"


def main() -> None:
    # Dispatchers handle the highest-severity emergency first.
    emergency_queue = Ordered_List(ascending=False)
    emergencies = (
        DispatchTicket("E-101", "Building fire", 5),
        DispatchTicket("E-102", "Medical emergency", 4),
        DispatchTicket("E-103", "Traffic collision", 3),
        DispatchTicket("E-104", "Gas leak", 5),
    )

    for ticket in emergencies:
        emergency_queue.add(LinearNode(ticket))

    print("Emergency queue, highest severity first:")
    print(emergency_queue.to_string())
    print(f"Tickets waiting: {emergency_queue.size()}")
    print(f"Next response: {emergency_queue.first().get_element()}")
    print()

    # The first dispatch removes the highest-priority ticket.
    dispatched = emergency_queue.remove_first()
    print(f"Dispatched: {dispatched.get_element()}")
    print(f"Queue after dispatch: {emergency_queue.to_string()}")
    print()

    # A lower numeric value can represent shorter wait time in an ascending view.
    wait_time_queue = Ordered_List(ascending=True)
    waiting_tickets = (
        DispatchTicket("E-201", "Noise complaint", 18),
        DispatchTicket("E-202", "Road obstruction", 7),
        DispatchTicket("E-203", "Welfare check", 12),
        DispatchTicket("E-203", "Super High Priority Tik Tok Recording Session", 21),
        DispatchTicket("E-202", "Super Low Priority Jam Session", 15),
    )

    for ticket in waiting_tickets:
        wait_time_queue.add(LinearNode(ticket))

    print("Callback queue, shortest wait first:")
    print(wait_time_queue.to_string())
    print(f"Next callback: {wait_time_queue.first().get_element()}")
    print(f"Last callback: {wait_time_queue.last().get_element()}")


if __name__ == "__main__":
    main()
