from enum import Enum

# Define the TextType enum to categorize different types of text content
class TextType(Enum):
    """
    Enumeration of all possible text types in our markdown parser.
    Each type represents how the text should be rendered in the final output.
    """
    # Basic text types for inline markdown parsing
    TEXT = "text"           # Plain text content (default/unformatted)
    BOLD = "bold"           # Bold formatted text (**bold**)
    ITALIC = "italic"       # Italic formatted text (*italic*)
    CODE = "code"           # Inline code text (`code`)
    
    # Block-level and special content types
    PLAIN = 'PLAIN'         # Plain text blocks (legacy/alternative to TEXT)
    LINK = 'LINK'           # Hyperlink text with URL
    IMAGE = 'IMAGE'         # Image references with alt text and URL
    

# Implement the TextNode class to represent a piece of text with its formatting type
class TextNode:
    """
    Represents a single piece of text with its associated formatting type.
    
    This is the fundamental building block of our markdown parser - every piece
    of content gets converted into TextNode objects that can later be rendered
    into HTML or other formats.
    """
    
    def __init__(self, text, text_type, url=None):
        """
        Initialize a new TextNode.
        
        Args:
            text (str): The actual text content
            text_type (TextType): How this text should be formatted (from TextType enum)
            url (str, optional): URL for links and images. Only used with LINK/IMAGE types.
            
        Examples:
            TextNode("Hello world", TextType.TEXT)           # Plain text
            TextNode("bold text", TextType.BOLD)             # Bold formatting
            TextNode("Click here", TextType.LINK, "https://example.com")  # Link
        """
        self.text = text           # The actual content
        self.text_type = text_type # How to format it (TEXT, BOLD, ITALIC, etc.)
        self.url = url            # Optional URL for links/images

    def __eq__(self, other):
        """
        Compare two TextNode objects for equality.
        
        Two TextNodes are equal if they have the same text content,
        text type, and URL. This is essential for testing.
        
        Args:
            other: Another object to compare against
            
        Returns:
            bool: True if both TextNodes are identical, False otherwise
        """
        # First check if the other object is even a TextNode
        if not isinstance(other, TextNode):
            return False
            
        # Check all three attributes for equality
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        """
        Return a string representation of the TextNode for debugging.
        
        This creates a string that shows exactly how to recreate this TextNode,
        which is very helpful for debugging and testing.
        
        Returns:
            str: A string like "TextNode('hello', TextType.BOLD, None)"
        """
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"

# Usage Examples:
#
# Basic text node:
# node1 = TextNode("Hello world", TextType.TEXT)
# 
# Formatted text:
# node2 = TextNode("important", TextType.BOLD)
# node3 = TextNode("emphasized", TextType.ITALIC)
# node4 = TextNode("console.log()", TextType.CODE)
#
# Links and images:
# node5 = TextNode("Click here", TextType.LINK, "https://example.com")
# node6 = TextNode("Alt text", TextType.IMAGE, "image.jpg")
#
# Testing equality:
# node7 = TextNode("test", TextType.TEXT)
# node8 = TextNode("test", TextType.TEXT)
# print(node7 == node8)  # True - same content and type
#
# Debugging output:
# print(repr(node1))  # TextNode('Hello world', <TextType.TEXT: 'text'>, None)

from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    """
    Convert a TextNode into an HTMLNode (LeafNode).
    
    Args:
        text_node (TextNode): The TextNode to convert
        
    Returns:
        LeafNode: An HTML node representing the text_node
        
    Raises:
        ValueError: If the text_node has an invalid text_type
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")