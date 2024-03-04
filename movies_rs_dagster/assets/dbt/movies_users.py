from pathlib import Path
import pandas as pd
from dagster import AssetExecutionContext, asset, Output
from dagster_dbt import DbtCliResource, dbt_assets, get_asset_key_for_model


@dbt_assets(manifest=Path("C:/Users/fla_4/Documents/mlops/mlops-ecosystem/db_postgres").joinpath("target", "manifest.json"))
def dbt_transformation_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


@asset(
        deps=get_asset_key_for_model([dbt_transformation_assets], "scores_peliculas_usuarios")
)
def get_training_data() -> Output[pd.DataFrame]:
    import psycopg2
    import pandas as pd

    conn = psycopg2.connect(database = "mlops", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "mysecretpassword",
                        port = 5432)
    cursor = conn.cursor()
    query = "SELECT * FROM target.scores_peliculas_usuarios"
    try:
        cursor.execute(query)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}" )
    
    tuples_list = cursor.fetchall()
    cursor.close()
    column_names = [desc[0] for desc in cursor.description] 
    df = pd.DataFrame(tuples_list, columns=column_names)
    return Output(
        df,
        metadata={
            "Total rows": len(df),
        },
    )