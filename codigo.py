import os
from datetime import datetime
import pandas as pd
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Agora pega as variáveis do ambiente
email_remetente = os.getenv("EMAIL_REMITENTE")
senha_app = os.getenv("SENHA_APP")
email_destinatario = "felipoboleslau@gmail.com"

if not email_remetente or not senha_app:
    raise Exception("Variáveis de ambiente EMAIL_REMITENTE e SENHA_APP precisam estar definidas no .env!")

# Caminho da pasta com os arquivos CSV
caminho = "bases"
arquivos = [arq for arq in os.listdir(caminho) if arq.endswith('.csv')]

tabela_consolidada = pd.DataFrame()

for nome_arquivo in arquivos:
    try:
        tabela_vendas = pd.read_csv(os.path.join(caminho, nome_arquivo))
        tabela_vendas["Data de Venda"] = pd.to_datetime("01/01/1900") + pd.to_timedelta(tabela_vendas["Data de Venda"], unit="d")
        tabela_consolidada = pd.concat([tabela_consolidada, tabela_vendas])
    except Exception as e:
        print(f"Erro ao processar {nome_arquivo}: {e}")

tabela_consolidada = tabela_consolidada.sort_values(by="Data de Venda").reset_index(drop=True)
arquivo_excel = "Vendas.xlsx"
tabela_consolidada.to_excel(arquivo_excel, index=False)

data_hoje = datetime.today().strftime("%d/%m/%Y")

mensagem = EmailMessage()
mensagem["Subject"] = f"Relatório de Vendas {data_hoje}"
mensagem["From"] = email_remetente
mensagem["To"] = email_destinatario
mensagem.set_content(f"""
Prezados,

Segue em anexo o Relatório de Vendas de {data_hoje} atualizado.
Qualquer coisa estou à disposição.

Abs,
Fe
""")

with open(arquivo_excel, "rb") as f:
    conteudo = f.read()
    mensagem.add_attachment(conteudo, maintype="application",
                            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            filename=arquivo_excel)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_remetente, senha_app)
        smtp.send_message(mensagem)
        print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
