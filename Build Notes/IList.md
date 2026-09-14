# IList

## Role

`IList` extends the base `IList_ADT` contract with insertion operations used by a standard linear list.

## Inheritance chain

```text
IList
└── IList_ADT
    └── ABC
```

## Additional abstract operations

- `add_to_back(node)` appends a node.
- `add_to_front(node)` prepends a node.
- `add_after(target, node)` inserts a node after a matching target.

The inherited `IList_ADT` methods cover inspection, searching, and removal.

## Implementations

The primary concrete implementation is `List`, which inherits from both `List_ADT` and `IList`.

```text
List
├── List_ADT
│   └── IList_ADT
└── IList
    └── IList_ADT
```

`List_ADT` supplies shared concrete behavior while `List` implements the insertion methods required by `IList`.
