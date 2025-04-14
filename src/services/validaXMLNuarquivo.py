import xml.etree.ElementTree as ET

def checkValidacoes(xml: str) -> str:
    root = ET.fromstring(xml)
    
    key = root.find('.//msg')
    
    if key is not None:
        return key.text

    return None