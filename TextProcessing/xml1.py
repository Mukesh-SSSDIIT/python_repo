import xml.etree.ElementTree as ET
tree = ET.parse('samplexml.xml')
root = tree.getroot()
print(root.tag)
print(root.text)
for child in root:
    print(child.tag,child.attrib)
    for subchild in child:
        print(subchild.tag,subchild.text)
