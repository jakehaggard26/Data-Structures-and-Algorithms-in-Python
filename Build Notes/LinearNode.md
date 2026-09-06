# LinearNode Multiple Inheritance

Use multiple inheritance by listing both classes:

```python
from DSA.Node.Node import Node
from DSA.Node.ILinearNode import ILinearNode


class LinearNode(Node, ILinearNode):

    def __init__(self, data, next=None):
        super().__init__(data)
        self._next = next

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node
```

The order matters:

```python
class LinearNode(Node, ILinearNode):
```

Because `Node` comes first, `super().__init__(data)` calls `Node.__init__`, which sets:

```python
self._data = data
```

The inheritance chain is:

```text
LinearNode
├── Node
│   └── INode
└── ILinearNode
    └── INode
```

`Node` supplies the data behavior, while `ILinearNode` identifies the class as a linear node and defines the `next` interface. `LinearNode` then supplies the actual `next` implementation.
