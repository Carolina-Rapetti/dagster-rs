from dagster_airbyte import airbyte_resource, AirbyteResource, build_airbyte_assets, load_assets_from_airbyte_instance
from . import AIRBYTE_CONFIG

def connection_to_group_airbyte(name: str) -> str:
    return 'airbyte_dbt'

# quisiera definir el airbyte_resource en la carpeta resources pero no lo puedo acceder desde aca
airbyte_instance = airbyte_resource.configured(AIRBYTE_CONFIG)
airbyte_assets = load_assets_from_airbyte_instance(airbyte_instance,
                                                   key_prefix=["recommender_system_raw"],
                                                   connection_to_group_fn=connection_to_group_airbyte
                                                   )
