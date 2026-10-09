"""O script lê dados de auditoria de um .txt e gera um .csv formatado pra abrir no Excel/LibreOffice."""

from csv import writer

ARQUIVO_AUDITORIA = "dados_auditoria.txt"
ARQUIVO_SAIDA = "relatorio_auditoria.csv"

#Funções
def ler_dados(arquivo):
    dados = []
    with open (arquivo, "r", encoding="utf-8") as lista:
        for linha in lista:
            dados.append(linha.strip())
    return dados

def organizar_dados(dados):
    organizar = [linha.split(";") for linha in dados]
    return organizar

def escrever_dados(dados, arquivo):
    with open (arquivo, "w", encoding="utf-8") as arquivo:
        escrever = writer(arquivo)
        for linha in dados:
            escrever.writerow(linha)

#Programa principal
if __name__ == "__main__":
    ler = ler_dados(ARQUIVO_AUDITORIA)
    organizar = organizar_dados(ler)
    escrever = escrever_dados(organizar, ARQUIVO_SAIDA)
    print("Relatório exportado com sucesso!")
