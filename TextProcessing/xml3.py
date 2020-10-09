import xml.etree.ElementTree as ET

def printxml(element):
    if element.text != '\n':
        print(element.text)
    if element:
        children = element.getchildren();
        if len(children) == 0:
            return 0
        else:
            for child in children:
                printxml(child)

tree = ET.parse('E:\\Python Programs\\python_repo\\TextProcessing\\samplexml.xml')
root = tree.getroot()
printxml(root)