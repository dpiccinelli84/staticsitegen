from enum import Enum

class TextType(Enum):
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"
    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.url = url  
        self.text = text
        self.text_type = TextType(text_type)
        
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"Text: {self.text}, Type: {self.text_type.value}, URL: {self.url}"