import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def test_eq(self):
        node = HTMLNode("div", "This is a text node")
        node2 = HTMLNode("div", "This is a text node")
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = HTMLNode("div", "This is a text node", children=[HTMLNode("span", "This is a span node")], props={"href": "http://www.google.com"})
        node2 = HTMLNode("div", "This is a text node", children=[HTMLNode("span", "This is a span node")], props={"href": "http://www.ansa.com"})
        self.assertNotEqual(node, node2)
        
    def test_repr2(self):
        node = HTMLNode("div", "This is a text node", children=[HTMLNode("span", "This is a span node")], props={"href": "http://www.google.com", "target": "_blank"})
        node2 = HTMLNode("div", "This is a text node", children=[HTMLNode("span", "This is a span node")], props={"href": "http://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
        
    def test_repr3(self):
        node = HTMLNode("div", "This is a text node", children=[HTMLNode("span", "This is a span node"), HTMLNode("test", "This is a test node")])
        node2 = HTMLNode("div", "This is a text node", children=[HTMLNode("span", "This is a span node"), HTMLNode("test", "This is a test node")])
        self.assertEqual(node, node2)

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_repr(self):
        node = LeafNode("div", "This is a text node", props={"href": "http://www.google.com"})
        node2 = LeafNode("div", "This is a text node", props={"href": "http://www.ansa.com"})
        self.assertNotEqual(node, node2)
        
    def test_repr2(self):
        node = LeafNode("div", "This is a text node",  props={"href": "http://www.google.com", "target": "_blank"})
        node2 = LeafNode("div", "This is a text node",  props={"href": "http://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
        
    def test_repr3(self):
        node = LeafNode("div", "This is a text node")
        node2 = LeafNode("div", "This is a text node")
        self.assertEqual(node, node2)
        
class TestParentNode(unittest.TestCase):
    
    def test_parent_to_html(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!"), LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p><p>Hello, world!</p></div>")
        
    def test_repr(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], props={"href": "http://www.google.com"})
        node2 = ParentNode("div", [LeafNode("p", "Hello, world!")], props={"href": "http://www.ansa.com"})
        self.assertNotEqual(node, node2)
        
    def test_repr2(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], props={"href": "http://www.google.com", "target": "_blank"})
        node2 = ParentNode("div", [LeafNode("p", "Hello, world!")], props={"href": "http://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)
        
    def test_repr3(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        node2 = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node, node2)
    
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
        "<div><span><b>grandchild</b></span></div>",)