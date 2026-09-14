# Ordered_List

## Role

`Ordered_List` is a singly linked list that inserts every node in ascending or descending order. It uses element comparison operators supplied by the stored values.

## Inheritance chain

```text
Ordered_List
├── List_ADT
│   └── IList_ADT
│       └── ABC
└── IOrdered_List
    └── IList_ADT
```

## Configuration

```python
Ordered_List(ascending=True)
Ordered_List(ascending=False)
```

The `_ascending` flag selects the insertion algorithm.

## Implemented methods

- `__add_ascending(node)` inserts before smaller values, between values, or at the tail.
- `__add_descending(node)` mirrors the ascending algorithm for descending order.
- `add(node)` delegates to the selected private helper.

The inherited `List_ADT` methods provide inspection and linear removal behavior.

## Ordering behavior

Equal values are traversed past before insertion, so duplicate nodes retain insertion order.

## Invariants

- The list remains linear: `_tail.next == None`.
- `_count` increases once for each successful insertion.
- `_head` and `_tail` are updated when insertion occurs at either boundary.
- Values must be mutually comparable for the chosen ordering.
