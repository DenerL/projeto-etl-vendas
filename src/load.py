def salvar_csv(df):
    caminho = "data/saida/superstore_tratado.csv"

    df.to_csv(
        caminho,
        index=False
    )

    print("\nCSV tratado salvo com sucesso!")