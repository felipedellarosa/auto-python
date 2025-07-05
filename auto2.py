#AUTOMATIZAÇÃO DE ARQUIVOS (Renomeação e Oraganização)

import os

def orgazinar_arquivos():
    pasta = "./arquivos"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    arquivos_pasta_atual =os.listdir(".")

    for arquivo in arquivos_pasta_atual:
        if ".text" in arquivo:
            os.rename(arquivo,f "{pasta}/{arquivo}")
    print("Arquivos organizados")

orgazinar_arquivos()