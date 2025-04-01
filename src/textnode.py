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
    
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
    
    
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
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) > 0:
            for image in images:
                new_nodes.append(TextNode(image[0], TextType.IMAGE_TEXT, image[1]))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) > 0:
            for link in links:
                new_nodes.append(TextNode(link[0], TextType.LINK_TEXT, link[1]))
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    
    nodes = []
    if len(text) == 0:
        return nodes
    
    nodes.append(TextNode(text, TextType.TEXT))
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC_TEXT)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes

def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n")
    
    for line in lines:
        if len(line) == 0:
            continue
        blocks.append(text_to_textnodes(line))
    
    return blocks

def block_to_block_type(block):
    if block[0].text_type == TextType.TEXT:
        return BlockType.PARAGRAPH
    elif block[0].text_type == TextType.BOLD_TEXT:
        return BlockType.HEADING
    elif block[0].text_type == TextType.CODE_TEXT:
        return BlockType.CODE
    elif block[0].text_type == TextType.IMAGE_TEXT:
        return BlockType.QUOTE
    elif block[0].text_type == TextType.LINK_TEXT:
        return BlockType.UNORDERED_LIST
    else:
        return BlockType.ORDERED_LIST
    
def recursive


