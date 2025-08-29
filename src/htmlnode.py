class HTMLNode:
    """Base class for all HTML nodes."""
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes an HTML node.

        Args:
            tag (str, optional): The HTML tag name. Defaults to None.
            value (str, optional): The text content of the node. Defaults to None.
            children (list, optional): A list of child nodes. Defaults to [].
            props (dict, optional): A dictionary of attributes/properties for the node. Defaults to {}.
        """
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        """
        Abstract method to generate HTML representation. Must be implemented by subclasses.
        Raises NotImplementedError if called directly.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    def props_to_html(self):
        """
        Generates a string representing the attributes of the node.

        Returns:
            str: A string containing the HTML attributes, e.g., "key1="value1" key2="value2"".
        """
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        """
        String representation of the object for debugging purposes.
        """
        return (f"HTMLNode(tag={self.tag!r}, "
                f"value={self.value!r}, "
                f"children={self.children!r}, "
                f"props={self.props!r})")

class LeafNode(HTMLNode):
    """Represents a leaf node in the HTML tree (no children)."""
    def __init__(self, tag=None, value=None, props=None):
        """
        Initializes a LeafNode.

        Args:
            tag (str, optional): The HTML tag name. Defaults to None.
            value (str, optional): The text content of the node. Defaults to None.
            props (dict, optional): A dictionary of attributes/properties for the node. Defaults to {}.

        Raises:
            ValueError: If value is not provided.
        """
        if value is None:
            raise ValueError("Value must be provided for a LeafNode.")
        
        super().__init__(tag, value, None, props)
        self.children = []  # Ensure no children are allowed

    def to_html(self):
        """
        Generates the HTML representation of the leaf node.

        Returns:
            str: The HTML string representing the leaf node.
        """
        if self.value is None:
            raise ValueError("LeafNode must have a value.")
            
        if self.tag is None:
            return self.value
        
        attrs_str = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        if attrs_str:
            attrs_str = ' ' + attrs_str
        return f"<{self.tag}{attrs_str}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    """Represents a parent node in the HTML tree (with children)."""
    def __init__(self, tag, children, props=None):
        """
        Initializes a ParentNode.

        Args:
            tag (str): The HTML tag name.
            children (list): A list of child nodes.
            props (dict, optional): A dictionary of attributes/properties for the node. Defaults to None.

        Raises:
            TypeError: If tag is not a string or children is not a list.
            ValueError: If children is an empty list.
        """
        if not isinstance(tag, str):
            raise TypeError("Tag must be a string.")
        if not isinstance(children, list):
            raise TypeError("Children must be a list.")
        if not children:
            raise ValueError("Children cannot be an empty list.")

        super().__init__(tag, None, children, props)

    def to_html(self):
        """
        Generates the HTML representation of the parent node and its children recursively.

        Returns:
            str: The HTML string representing the parent node and its children.
        """
        attrs_str = ' '.join(f'{key}="{value}"' for key, value in self.props.items())
        if attrs_str:
            attrs_str = ' ' + attrs_str
        opening_tag = f"<{self.tag}{attrs_str}>"
        closing_tag = f"</{self.tag}>"
        children_html = "".join(child.to_html() for child in self.children)
        return f"{opening_tag}{children_html}{closing_tag}"
