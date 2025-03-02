import unittest

from htmlnode import HTMLNode, LeafNode

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