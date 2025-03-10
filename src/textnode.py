import re
from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"
    TEXT = "text"
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.url = url  
        self.text = text
        self.text_type = TextType(text_type)
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"Text: {self.text}, Type: {self.text_type.value}, URL: {self.url}"
    
def text_node_to_html_node(text_node):
    match text_node:
        case TextType.TEXT:
            return LeafNode("text", text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK_TEXT:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE_TEXT:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_text = node.text.split(delimiter)
        if len(split_text) > 1:
            for text in split_text:
                new_nodes += TextNode(text, text_type)
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    #images = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    #    images.append(match.group(1), match.group(2))
    return matches

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links