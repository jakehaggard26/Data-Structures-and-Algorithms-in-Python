# IList_ADT

## Role

`IList_ADT` is the root abstract contract for list-like data structures. It inherits from Python's `ABC` and defines the common operations that every list implementation must provide.

## Inheritance chain

```text
IList_ADT
└── ABC
```

## Abstract operations

- `__init__()` initializes an implementation.
- `first()` returns the first node.
- `last()` returns the last node.
- `is_empty()` reports whether the structure has no nodes.
- `size()` returns the node count.
- `to_string()` returns a representation of the nodes.
- `contains(node)` searches for a matching element.
- `remove(node)` removes and returns a matching node.
- `remove_first()` removes and returns the first node.
- `remove_last()` removes and returns the last node.

## Design note

This class defines behavior only. Concrete classes such as `List_ADT`, `List`, `Ordered_List`, and `Circular_List` provide the implementations.
