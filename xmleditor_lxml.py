__author__ = 'lena'

# xmlfile = open("project.xml")
# for aline in xmlfile:
#     values = aline.split()
#     print(values)
# xmlfile.close()

# from xml.dom import minidom
# xmldoc = minidom.parse('project.xml')
# itemlist = xmldoc.getElementsByTagName("Values")
# print(len(itemlist))
# # print((itemlist))
# print(itemlist[0].attributes['Name'].value)
# print(xmldoc.childNodes[0].nodeValue)
# print(xmldoc.childNodes.length)
# print("hello", xmldoc.nodeValue)
# # print(itemlist[0])
# # for s in itemlist:
# #     print(s.attributes['Name'].value)
# print(xmldoc.hasChildNodes())

# from xml.dom.minidom import parse
# dom = parse("project.xml")
# print(dom.toxml())  # prints the entire xml document
# print(dom)
# print(dom.childNodes[0])
#
# project_node = dom.childNodes[0]
# subsystems_node = project_node.childNodes[1]
# values_node = subsystems_node.childNodes[1]
# test = values_node.childNodes[1]
# test.attributes["Value"].value = "12"
# print(test.attributes["Value"].value)
# print(values_node.toxml())

from lxml import etree

doc = etree.parse("project.xml")
# subsystems = doc.find('Subsystems')
# print(len(subsystems))
# print(doc.findall("Subsystems"))
# print(subsystems.findall("Values"))
#
# Player = subsystems[0]
# print(len(Player))
# print(Player.items())
# print(Player[0:2])
#
# SpawnPosition = Player[0]
# print(len(SpawnPosition))
# print(SpawnPosition.items())
# print(SpawnPosition.tag)

# for elt in doc.getiterator():
#     print(elt.tag)


# for elt in doc.getiterator('Value'):
#     if elt.attrib.has_key('Value'):
#         print(elt.get('Name'))
#
# from lxml import etree
# from io import StringIO

# ----------------------------------------------------------------------


from lxml import etree

response = """
<response version="1.0">
  <code>200</code>
  <id>50</id>
</response>"""

try:
    doc = etree.XML(response.strip())
    code = doc.findtext('code')
    print(code)
except etree.XMLSyntaxError:
    print('XML parsing error.')









# Prints the entire xml document by node
# for node in dom.getElementsByTagName('Values'):  # visit every node <Values />
#     print(node.toxml())



