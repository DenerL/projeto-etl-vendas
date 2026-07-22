from src.extract import ler_csv
from src.transform import transformar_dados
from src.load import salvar_csv
from src.analysis import analisar_vendas
from src.report import gerar_relatorio

arquivo = "data/entrada/superstore.csv"

df = ler_csv(arquivo)

df = transformar_dados(df)

salvar_csv(df)

resultado = analisar_vendas(df)

gerar_relatorio(resultado)
