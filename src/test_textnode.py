import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "http://www.google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT, "http://www.google.com")
        self.assertNotEqual(node, node2)

    def test_repr2(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT, "http://www.google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT, "http://www.google.com")
        self.assertEqual(node, node2)
 
    def test_repr3(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT, "http://www.google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT, "http://www.ansa.it")
        self.assertNotEqual(node, node2)        
        
        

if __name__ == "__main__":
    unittest.main()