from DSA.Collections.Lists.List_ADT import List
from DSA.Node.LinearNode import LinearNode


"""
    Example use case: a warehouse fulfillment workflow.

    A linked list is useful here because work items are frequently added to the
    front or back of the workflow, inserted beside related work, and removed
    when completed.
"""
def main() -> None:
    workflow = List()

    # Add regular fulfillment tasks in processing order.
    receive_order = LinearNode("Receive order")
    pick_items = LinearNode("Pick items")
    pack_order = LinearNode("Pack order")

    workflow.add_to_back(receive_order)
    workflow.add_to_back(pick_items)
    workflow.add_to_back(pack_order)

    print(f"Initial workflow: {workflow.to_string()}")
    print(f"Tasks in workflow: {workflow.size()}")
    print(f"First task: {workflow.first().get_element()}")
    print(f"Last task: {workflow.last().get_element()}")

    # Add a quality check directly after packing and before shipping.
    quality_check = LinearNode("Quality check")
    workflow.add_after(pack_order, quality_check)
    print(f"After adding quality check: {workflow.to_string()}")

    # An urgent order is placed at the front of the workflow.
    urgent_order = LinearNode("Handle urgent order")
    workflow.add_to_front(urgent_order)
    print(f"After adding urgent work: {workflow.to_string()}")

    # Check whether a task is still waiting to be completed.
    shipping_task = LinearNode("Ship order")
    print(f"Shipping task queued: {workflow.contains(shipping_task)}")

    # Add shipping after the quality check once the order is approved.
    workflow.add_after(quality_check, shipping_task)
    print(f"After adding shipping: {workflow.to_string()}")

    # Remove completed work while preserving the rest of the workflow.
    completed_task = workflow.remove(receive_order)
    print(f"Completed: {completed_task.get_element()}")
    print(f"Remaining workflow: {workflow.to_string()}")

    # The first urgent task is now ready to process.
    completed_task = workflow.remove_first()
    print(f"Completed first task: {completed_task.get_element()}")
    print(f"Remaining workflow: {workflow.to_string()}")

    # The final task can be removed from the back after the shipment leaves.
    completed_task = workflow.remove_last()
    print(f"Completed last task: {completed_task.get_element()}")
    print(f"Final workflow: {workflow.to_string()}")
    print(f"Workflow empty: {workflow.is_empty()}")


if __name__ == "__main__":
    main()
