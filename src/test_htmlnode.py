import unittest
from htmlnode import HTMLNode, TagType

# (tag=None, value=None, children=None, props=None)

class TestHTMLtNode(unittest.TestCase):
  def test_props_to_html(self):
    node_with_props = HTMLNode(tag=TagType.A, value='test url', props={
      "href": "https://www.google.com",
      "target": "_blank",
    })
    self.assertEqual(node_with_props.props_to_html(), 'href="https://www.google.com" target="_blank" ')

    node_no_props = HTMLNode(value='test paragraph')
    self.assertEqual(node_no_props.props_to_html(), '')

    node_empty_props = HTMLNode(value='test paragraph', props={})
    self.assertEqual(node_empty_props.props_to_html(), '')

  def test_values(self):
    node = HTMLNode(TagType.DIV, 'I am a div')
    self.assertEqual(node.tag.value, TagType.DIV.value)
    self.assertEqual(node.value, 'I am a div')
    self.assertEqual(node.children, None)
    self.assertEqual(node.props, None)

  def test_repr(self):
    node = HTMLNode(TagType.A, 'this is a link', None, { "href": "www.url.com" })
    self.assertEqual(node.__repr__(), "HTMLNode(a, this is a link, None, {'href': 'www.url.com'})")


if __name__ == '__main__':
  unittest.main()
