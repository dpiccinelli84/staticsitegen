from textnode import TextNode

def main():
    text_node = TextNode("Hello", "bold", "https://www.google.com") 
    print(f"TextNode({text_node.text}, {text_node.text_type.value}, {text_node.url})")
    return
    
main()
# Compare this snippet from github.com/dpiccinelli84/staticsitegen/src/textnode.py:
    
    