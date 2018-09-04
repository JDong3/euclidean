import lxml.etree as ET

tree = ET.parse('assets/freesample.svg')
root = tree.getroot()

print(ET.tostring(root, method='html', pretty_print=True))
print()
