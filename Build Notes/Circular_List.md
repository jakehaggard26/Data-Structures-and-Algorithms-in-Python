# Circular_List

## Role

`Circular_List` is an unordered singly linked circular list. It preserves insertion order while maintaining a link from the tail back to the head.

## Inheritance chain

```text
Circular_List
├── ICircular_List
│   └── IList
│       └── IList_ADT
│           └── ABC
└── List
    ├── List_ADT
    │   └── IList_ADT
    └── IList
        └── IList_ADT
```

`ICircular_List` supplies the circular-list interface, while `List` supplies compatible list behavior and insertion-related structure. Circular traversal methods are overridden where linear `None` termination would be unsafe.

## Implemented methods

- `add(node)` appends a node to the circular sequence.
- `remove_first()` removes the head and reconnects the tail to the new head.
- `remove_last()` removes the tail and reconnects the new tail to the head.
- `remove(node)` removes the first matching element value.
- `to_string()` visits exactly `_count` nodes.
- `contains(node)` searches at most `_count` nodes.
- `first()` and `last()` return the boundary nodes.

## Circular invariants

- Empty list: `_head is None`, `_tail is None`, `_count == 0`.
- Singleton list: `_head is _tail` and the node points to itself.
- Non-empty list: `_tail.get_next() is _head`.
- `_count` equals the number of reachable nodes.
- Removed nodes are detached by setting their `next` reference to `None`.

## Important implementation note

Methods inherited from a linear list cannot be used unchanged if they loop until `None`. Every circular traversal must stop after `_count` nodes or when it returns to `_head`.
