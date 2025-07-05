#AUTOMAÇÃO NO EXCEL (Atualizar uma planilha)

import openpyxl

def atualizar_planilha():
    workbook = openpyxl.load_workbook("bases/dados.xlsx")
    aba = workbook.active
    aba.append(["Felipe", 20, "Desenvolvedor"])
    workbook.save("bases/dados.xlsx")
    print("planilha atualizada")

atualizar_planilha()