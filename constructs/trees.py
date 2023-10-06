from abc import ABC, abstractmethod
from typing import TypeVar, Optional

T = TypeVar("T")

class AbstractNode[T](ABC):
    """
    Abstract class for a node in a tree.
    
    Attributes:
        parent: The parent of the node.
        content: The content of the node.
        children: The children of the node.
    """

    def __init__(self, 
                 parent: "AbstractNode[T]" | None = None,
                 content: T | None = None,
                 children: list["AbstractNode[T]"] = [], 
                 ):
        """
        Initializes the node.
        """
        self.parent = parent
        self.content = content
        self.children = children
        
    def get_parent(self) -> "AbstractNode[T]":
        """
        Returns the parent of the node.
        """
        return self.parent
    
    def set_parent(self, parent: "AbstractNode[T]") -> None:
        """
        Sets the parent of the node.
        """
        self.parent = parent

    def has_parent(self) -> bool:
        """
        Returns whether the node has a parent.
        """
        return self.parent is not None

    def get_content(self) -> T:
        return self.content
    
    def set_content(self, content: T):
        self.content = content

    def is_empty(self) -> bool:
        """
        Returns whether the node is empty.
        """
        return self.content is None

    def get_children(self) -> list["AbstractNode[T]"]:
        """
        Returns the children of the node.
        """
        return self.children
    
    def set_children(self, children: list["AbstractNode[T]"]) -> None:
        """
        Sets the children of the node.
        """
        self.children = children

    def has_children(self) -> bool:
        """
        Returns whether the node has children.
        """
        return len(self.children) > 0

    def add_child(self, child: "AbstractNode[T]") -> None:
        """
        Adds a child to the node.
        """
        self.children.append(child)

    def remove_child(self, child: "AbstractNode[T]") -> None:
        """
        Removes a child from the node.
        """
        self.children.remove(child)

    def is_leaf(self) -> bool:
        """
        Returns whether the node is a leaf.
        """
        return len(self.children) == 0
    
    def is_root(self) -> bool:
        """
        Returns whether the node is the root.
        """
        return self.parent is None
    
    def get_depth(self) -> int:
        """
        Returns the depth of the node.
        """
        if self.is_root():
            return 0
        return self.parent.get_depth() + 1
    
    def get_height(self) -> int:
        """
        Returns the height of the node.
        """
        if self.is_leaf():
            return 0
        return max([child.get_height() for child in self.children]) + 1
    
    def get_size(self) -> int:
        """
        Returns the size of the node.
        """
        return sum([child.get_size() for child in self.children]) + 1
    
    def get_ancestors(self) -> list["AbstractNode[T]"]:
        """
        Returns the ancestors of the node.
        """
        if self.is_root():
            return []
        return [self.parent] + self.parent.get_ancestors()
    
    def get_descendants(self) -> list["AbstractNode[T]"]:
        """
        Returns the descendants of the node.
        """
        if self.is_leaf():
            return []
        return self.children + [child.get_descendants() for child in self.children]
    
    def get_siblings(self) -> list["AbstractNode[T]"]:
        """
        Returns the siblings of the node.
        """
        if self.is_root():
            return []
        return [child for child in self.parent.get_children() if child != self]
    
    def get_leaves(self) -> list["AbstractNode[T]"]:
        """
        Returns the leaves of the node.
        """
        if self.is_leaf():
            return [self]
        return [leaf for child in self.children for leaf in child.get_leaves()]
    
    

    


class AbstractTree[T](ABC):
    """
    Abstract class for a tree.

    Attributes:
        root: The root of the tree.
    """
    def __init__(self, root: AbstractNode[T] | None = None):
        """
        Initializes the tree.
        """
        self.root = root

    def get_root(self) -> AbstractNode[T]:
        """
        Returns the root of the tree.
        """
        return self.root
    
    def set_root(self, root: AbstractNode[T]) -> None:
        """
        Sets the root of the tree.
        """
        self.root = root

    def is_empty(self) -> bool:
        """
        Returns whether the tree is empty.
        """
        return self.root is None


    def get_leaves(self) -> list[AbstractNode[T]]:
        """
        Returns the leaves of the tree.
        """
        return self.root.get_leaves()
    
    def get_size(self) -> int:
        """
        Returns the size of the tree.
        """
        return self.root.get_size()
    
    def get_height(self) -> int:
        """
        Returns the height of the tree.
        """
        return self.root.get_height()
    
    def get_depth(self) -> int:
        """
        Returns the depth of the tree.
        """
        return self.root.get_depth()
    


    

