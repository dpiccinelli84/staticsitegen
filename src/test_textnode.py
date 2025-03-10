import unittest

from textnode import *


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
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        print(matches)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube","https://www.youtube.com/@bootdotdev" )], matches)        
        
             
        
        

if __name__ == "__main__":
    unittest.main()