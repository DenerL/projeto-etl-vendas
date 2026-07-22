def analisar_vendas(df):

    total_vendas = df["Sales"].sum()

    vendas_categoria = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    categoria_top = vendas_categoria.idxmax()
    valor_categoria_top = vendas_categoria.max()

    top_produtos = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    return {
        "total_vendas": total_vendas,
        "vendas_categoria": vendas_categoria,
        "categoria_top": categoria_top,
        "valor_categoria_top": valor_categoria_top,
        "top_produtos": top_produtos
    }