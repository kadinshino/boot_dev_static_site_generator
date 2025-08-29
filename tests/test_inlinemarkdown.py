import unittest
from inline_markdown import split_nodes_delimiter, TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_single_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_single_bold_block(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT),
        ])

    def test_single_italic_block(self):
        node = TextNode("This is text with an *italicized word*.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italicized word", TextType.ITALIC),
            TextNode(".", TextType.TEXT),
        ])

    def test_multiple_code_blocks(self):
        node = TextNode("This is `code 1` and then `code 2`.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code 1", TextType.CODE),
            TextNode(" and then ", TextType.TEXT),
            TextNode("code 2", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ])

    def test_non_text_node(self):
        node = TextNode("This is text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text", TextType.BOLD)])

    def test_no_closing_delimiter(self):
        node = TextNode("This is `code block", TextType.TEXT)
        with self.assertRaisesRegex(ValueError, "Unmatched delimiter"):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("", TextType.TEXT)])

    def test_multiple_delimiters(self):
      node = TextNode("This is **bold** and `code`.", TextType.TEXT)
      new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
      new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)

      self.assertEqual(new_nodes, [
          TextNode("This is ", TextType.TEXT),
          TextNode("bold", TextType.BOLD),
          TextNode(" and ", TextType.TEXT),
          TextNode("code", TextType.CODE),
          TextNode(".", TextType.TEXT)
      ])

if __name__ == '__main__':
    unittest.main()