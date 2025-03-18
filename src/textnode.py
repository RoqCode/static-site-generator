from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url


def __eq__(text_node_1, text_node_2):
    return text_node_1 == text_node_2


def __repr__(text, text_type, url):
    return f"TextNode({text}, {text_type.value}, {url}"
