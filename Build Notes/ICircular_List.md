# ICircular_List

## Role

`ICircular_List` defines the boundary-node contract for a circular list while inheriting the general list operations from `IList`.

## Inheritance chain

```text
ICircular_List
└── IList
    └── IList_ADT
        └── ABC
```

## Abstract operations

- `first()` returns the circular list head.
- `last()` returns the circular list tail.

The inherited `IList` and `IList_ADT` contracts describe insertion, search, string conversion, and removal operations.

## Circular invariant

For every non-empty implementation:

```text
last().get_next() is first()
```

Unlike a linear list, a circular list must stop traversal when it reaches `_head` again rather than waiting for `None`.
