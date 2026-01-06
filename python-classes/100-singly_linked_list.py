cat > 100-singly_linked_list.py <<'EOF'
#!/usr/bin/python3
"""Defines a Node and SinglyLinkedList."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get node data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set node data with validation."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node with validation."""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a sorted singly linked list."""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position."""
        new = Node(value)

        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        cur = self.__head
        while cur.next_node is not None and cur.next_node.data <= value:
            cur = cur.next_node

        new.next_node = cur.next_node
        cur.next_node = new

    def __str__(self):
        """Print the list one number per line."""
        lines = []
        cur = self.__head
        while cur is not None:
            lines.append(str(cur.data))
            cur = cur.next_node
        return "\n".join(lines)
EOF
