def analisar_dataframe(dataframe: pd.DataFrame) -> dict:
    linhas, colunas = dataframe.shape
    nulos = dataframe.isna().sum().to_dict()
    duplicados = int(dataframe.duplicated().sum())
    numericas = dataframe.select_dtypes(include="number")

    if numericas.empty:
        estatisticas = {}
    else:
        estatisticas = (
            numericas.describe().to_dict()
        )

    return {
        "total_registros": linhas,
        "total_colunas": colunas,
        "nulos_por_coluna": nulos,
        "duplicados": duplicados,
        "estatisticas": estatisticas
    }
