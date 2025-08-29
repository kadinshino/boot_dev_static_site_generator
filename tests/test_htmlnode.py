import unittest
from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), 'href="https://www.google.com" target="_blank"')

        node2 = HTMLNode(props={"class": "container", "id": "main"})
        self.assertEqual(node2.props_to_html(), 'class="container" id="main"')

    def test_no_props(self):
        node3 = HTMLNode(tag="p", value="Hello, world!")
        self.assertEqual(node3.props_to_html(), '')

    def test_repr_method(self):
        node4 = HTMLNode(tag="a", value="Google", props={"href": "https://www.google.com"})
        expected_repr = 'HTMLNode(tag=\'a\', value=\'Google\', children=[], props={\'href\': \'https://www.google.com\'})'
        self.assertEqual(repr(node4), expected_repr)

if __name__ == '__main__':
    unittest.main()
