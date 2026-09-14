# List_ADT

## Role

`List_ADT` is the shared concrete base for the project's linear and ordered lists. It stores the linked-list state and implements common linear-list operations.

## Inheritance chain

```text
List_ADT
└── IList_ADT
    └── ABC
```

## Stored state

- `_head` references the first node.
- `_tail` references the last node.
- `_count` stores the number of nodes.

A normal linear list ends with `_tail.next == None`.

## Implemented methods

- `first()` and `last()` expose the boundary nodes.
- `is_empty()` and `size()` inspect state.
- `to_string()` traverses until `None`.
- `contains(node)` searches by element value.
- `remove(node)` removes the first matching element.
- `remove_first()` removes the head.
- `remove_last()` removes the tail.

## Important limitation

These implementations assume a linear list whose final `next` reference is `None`. `Circular_List` must override traversal and removal methods because a circular list never reaches `None` during normal traversal.
