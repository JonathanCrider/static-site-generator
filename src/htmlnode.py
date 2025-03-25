from enum import Enum


class TagType(Enum):
  A = 'a'
  P = 'p'
  DIV = 'div'
  H1 = 'h1'
  H2 = 'h2'
  H3 = 'h3'
  H4 = 'h4'
  H5 = 'h5'
  H6 = 'h6'


class HTMLNode():
  def __init__(self, tag:TagType=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError('to_html method not implemented')
  
  def props_to_html(self):
    html_string = ''
    if not self.props:
      return html_string
    for prop in self.props:
      html_string += f'{prop}="{self.props[prop]}" '
    return html_string
  
  def __repr__(self):
    return f'HTMLNode({self.tag.value if not self.tag == None else self.tag}, {self.value}, {self.children}, {self.props})'
