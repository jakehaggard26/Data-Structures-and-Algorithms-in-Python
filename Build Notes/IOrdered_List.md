# IOrdered_List

## Role

`IOrdered_List` extends the base list contract with one public operation for inserting nodes while preserving an ordering rule.

## Inheritance chain

```text
IOrdered_List
└── IList_ADT
    └── ABC
```

## Abstract operation

- `add(node)` inserts a node according to the implementation's ordering direction.

## Implementation

`Ordered_List` implements this interface and accepts an `ascending` flag. The private helpers `__add_ascending` and `__add_descending` contain the direction-specific algorithms.
