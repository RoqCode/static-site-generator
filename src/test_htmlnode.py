import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode(
            tag="div", value="Hello", children=[], props={"class": "container"}
        )
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})

    def test_repr_output(self):
        node = HTMLNode(tag="p", value="Test", children=None, props={"id": "para1"})
        expected_repr = "tag: p, value: Test, children: None, props: {'id': 'para1'}"
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html_valid(self):
        node = HTMLNode(props={"class": "btn", "disabled": "true"})
        self.assertEqual(node.props_to_html(), ' class="btn" disabled="true"')

    def test_props_to_html_invalid(self):
        node = HTMLNode(props="invalid_props")
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()

