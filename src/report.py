def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")


def gerar_relatorio(resultado):

    relatorio = ""
    relatorio += "=" * 50 + "\n"
    relatorio += "RELATÓRIO DE VENDAS\n"
    relatorio += "=" * 50 + "\n\n"

    relatorio += (
        f"Faturamento Total: "
        f"{formatar_moeda(resultado['total_vendas'])}\n\n"
    )

    relatorio += "Categoria com maior faturamento:\n"
    relatorio += (
        f"{resultado['categoria_top']}: "
        f"{formatar_moeda(resultado['valor_categoria_top'])}\n\n"
    )

    relatorio += "Top 10 Produtos:\n\n"

    for i, (produto, valor) in enumerate(
        resultado["top_produtos"].items(),
        start=1
    ):
        relatorio += (
            f"{i}. {produto}\n"
            f"   {formatar_moeda(valor)}\n\n"
        )

    print(relatorio)

    with open(
        "data/saida/relatorio_vendas.txt",
        "w",
        encoding="utf-8"
    ) as arquivo:
        arquivo.write(relatorio)

    print("Relatório salvo com sucesso!")