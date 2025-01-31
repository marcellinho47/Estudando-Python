import os
from lxml import etree


def extract_info_from_xml(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()

    # cpf_trab = root.find('.//esocial:cpfTrab', namespaces=namespaces)
    cpf_trab = root.xpath('.//*[local-name()="cpfTrab"]')
    ide_dmdev_list = root.xpath('//*[local-name()="ideDmDev"]')

    # ide_dmdev_list = root.findall('.//esocial:ideDmDev', namespaces=namespaces)

    if cpf_trab is not None:
        cpf_trab_text = cpf_trab[0].text
    else:
        cpf_trab_text = 'Tag cpfTrab não encontrada'

    ide_dmdev_values = [ide_dmdev.text for ide_dmdev in ide_dmdev_list]
    print(ide_dmdev_values)

    return cpf_trab_text, ide_dmdev_values


if __name__ == '__main__':
    folder_path = os.getcwd()

    # Listar todos os arquivos XML na pasta
    for file_name in os.listdir(folder_path):

        if file_name.endswith('.xml'):
            # valor = True
            file_path = os.path.join(folder_path, file_name)
            cpf_trab, ide_dmdev_values = extract_info_from_xml(file_path)

            print(file_path)

            print(f"Arquivo: {file_name}")
            print(f"  CPF do Trabalhador: {cpf_trab}")
            print("  IDs de ideDmDev:")
            for ide_dmdev in ide_dmdev_values:
                print(f"{ide_dmdev}")

            with open(f"{folder_path}\\resultado.txt", "a") as f:
                f.write(cpf_trab)
                for ide_dmdev in ide_dmdev_values:
                    f.write("\t" + ide_dmdev)
                f.write("\n")
