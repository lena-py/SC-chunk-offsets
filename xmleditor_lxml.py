__author__ = 'lena'

# From http://lxml.de/tutorial.html

try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")

tree = etree.parse("example.xml")
s = tree.findtext("codes")
print(s)

elem = tree.getroot()
print("elem is", elem)
print("elem tag is", elem.tag)
print("length of elem is", len(elem))

nodes = elem[:]
print("second node is:", nodes[1].tag)
for node in elem:
    print("node is", node.tag)

node = list(elem)
print(node[0].tag)
