import xml.etree.ElementTree as ET

def checkXml(xml: str):
    tree = ET.parse(xml)
    root = tree.getroot()

    print(root)

    if root.validacoesCte.validacoesCteVinculoNota.msg in root:
        print("aaa")


checkXml("./test.xml")