from textnode import TextNode, TextType

def main():
  test = TextNode('test text', TextType.LINK, 'www.google.com')
  print(test)



main()