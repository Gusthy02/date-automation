import pandas as pd
import re

# Nome do arquivo
arquivo = "Contagem.xlsx"
sheet_name = "RESFRIADO"


df = pd.read_excel(arquivo, sheet_name=sheet_name)

# Função para formatar a data
def formatar_data(data):
    match = re.search(r"(\d{2})\.(\d{2})", str(data))  # padrão XX.XX
    if match:
        return match.group(1) + match.group(2) + str("2025") # formato XXYY
    return data 

# Nome da coluna
coluna_datas = "Datas"

# Aplicar a formatação à coluna
df[coluna_datas] = df[coluna_datas].apply(formatar_data)

# Salvar a planilha
df.to_excel("datas_formatadas.xlsx", index=False)

print("✅✅✅ As datas foram formatadas e salvas! ✅✅✅")
