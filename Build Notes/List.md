# List

## Role

`List` is the standard unordered singly linked list implementation. It combines the concrete operations from `List_ADT` with the insertion contract from `IList`.

## Inheritance chain

```text
List
├── List_ADT
│   └── IList_ADT
│       └── ABC
└── IList
    └── IList_ADT
```

`List_ADT` appears first in the base-class order so `super().__init__()` initializes `_head`, `_tail`, and `_count` through the concrete implementation.

## Implemented insertion methods

- `add_to_back(node)` appends a node and clears its previous `next` link.
- `add_to_front(node)` prepends a node.
- `add_after(target, node)` inserts after the first matching target value.

## Inherited behavior

`List` receives `first`, `last`, `is_empty`, `size`, `to_string`, `contains`, `remove`, `remove_first`, and `remove_last` from `List_ADT`.

## Invariants

- Empty list: `_head` and `_tail` are `None`, and `_count` is `0`.
- Non-empty list: `_head` is the first node, `_tail` is the last node, and `_tail.next` is `None`.
- `_count` equals the number of reachable nodes.
