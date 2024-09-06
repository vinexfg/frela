# Ler dados da planilha
# inserir casa élula de cada linha em um campo do sistema
import openpyxl

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
sheet_produtos = workbook['vendas']


for linha in sheet_produtos.iter_rows(min_row=2):
    print(linha[0].value)
    print(linha[1].value)
    print(linha[2].value)
    print(linha[3].value)