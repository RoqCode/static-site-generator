import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        node = LeafNode(tag="span", value="Hello", props={"class": "highlight"})
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "highlight"})

    def test_to_html_with_tag_and_value(self):
        node = LeafNode(tag="p", value="This is a paragraph.", props={"id": "para1"})
        expected_html = '<p id="para1">This is a paragraph.</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_tag(self):
        node = LeafNode(tag=None, value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_to_html_raises_error_when_value_is_none(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_props_to_html_with_multiple_attributes(self):
        node = LeafNode(
            tag="button", value="Click me", props={"class": "btn", "disabled": "true"}
        )
        expected_html = '<button class="btn" disabled="true">Click me</button>'
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
