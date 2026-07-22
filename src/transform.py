import pandas as pd

def transformar_dados(df):
    #Tratar valores vazios
    df["Postal Code"] = df["Postal Code"].fillna(0)

    #Converter datas
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        dayfirst=True
    )

    #Criar novas colunas 
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month

    df["Delivery Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    return df