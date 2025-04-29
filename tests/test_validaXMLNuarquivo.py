import unittest
from xml.etree.ElementTree import Element, tostring
from ..src.services.validaXMLNuarquivo import checkChaveReferenciada

class TestCheckChaveReferenciada(unittest.TestCase):

    def test_valid_input(self):
        xml = """
        <root>
            <validacoesCteVinculoNota>
                <nota CHAVENFE="123456789" NUNOTASELECIONADA="987654" />
                <nota CHAVENFE="111222333" NUNOTASELECIONADA="000111" />
            </validacoesCteVinculoNota>
        </root>
        """
        expected = [
            {'CHAVENFE': '123456789', 'NUNOTASELECIONADA': '987654'},
            {'CHAVENFE': '111222333', 'NUNOTASELECIONADA': '000111'}
        ]
        result = checkChaveReferenciada(xml)
        self.assertEqual(result, expected)

    def test_missing_tag(self):
        xml = "<root><otherTag/></root>"
        result = checkChaveReferenciada(xml)
        self.assertIsNone(result)

    def test_empty_string(self):
        result = checkChaveReferenciada("")
        self.assertIsNone(result)

    def test_none_input(self):
        result = checkChaveReferenciada(None)
        self.assertIsNone(result)

    def test_empty_validacoes_tag(self):
        xml = "<root><validacoesCteVinculoNota></validacoesCteVinculoNota></root>"
        result = checkChaveReferenciada(xml)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()