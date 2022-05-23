import xml.etree.ElementTree as ET

tree = ET.parse(r'D:\git\PythonRedes\estudos\output.xml')
root = tree.getroot()

for pesquisa in root.iter('stat'):
    result = (pesquisa.attrib.get('fail'))
    if result != '0':
        print('O loop terminou')
        break

if result == "0":
    print('Envia email')
else:
    print('Não envia email')