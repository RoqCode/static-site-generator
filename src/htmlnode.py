class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not isinstance(self.props, dict):
            return ""
        attributes = ""
        for key, value in self.props.items():
            attributes = attributes + f' {key}="{value}"'
        return attributes

    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return str(self.value)

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
