import unittest


from htmlnode import ParentNode
from htmlnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_initialization(self):
        children = [LeafNode("b", "Bold text"), LeafNode("i", "Italic text")]
        node = ParentNode(tag="p", children=children, props={"class": "text"})

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, {"class": "text"})

    def test_to_html_correct_output(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_html = (
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_attributes(self):
        node = ParentNode(
            "div",
            [LeafNode("span", "Hello"), LeafNode(None, " World")],
            props={"class": "container"},
        )
        expected_html = '<div class="container"><span>Hello</span> World</div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_raises_error_when_no_tag(self):
        children = [LeafNode("b", "Bold text")]
        with self.assertRaises(ValueError):
            ParentNode(None, children).to_html()

    def test_to_html_raises_error_when_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", []).to_html()

    def test_to_html_nested_structure(self):
        node = ParentNode(
            "div",
            [
                ParentNode("p", [LeafNode(None, "First paragraph")]),
                ParentNode("p", [LeafNode(None, "Second paragraph")]),
            ],
        )
        expected_html = "<div><p>First paragraph</p><p>Second paragraph</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
