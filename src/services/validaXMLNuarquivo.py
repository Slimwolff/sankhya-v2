import xml.etree.ElementTree as ET

def checkMsgNroUnico(xml: str) -> str:

    if not xml:
        return None
    else:
        root = ET.fromstring(xml)
        
        key = root.find('.//msg')
        
        if key is not None:
            return key.text

def checkChaveReferenciada(xml: str):
    """
        Retorna uma lista com as chaves referenciadas

        :return List:
    """
    if not xml:
        return None
    else: 
        root = ET.fromstring(xml)

        key = root.find('.//validacoesCteVinculoNota')

        if key is not None:
            return [k.attrib for k in key if k.tag == "chaveNFe"]
                        
    return None