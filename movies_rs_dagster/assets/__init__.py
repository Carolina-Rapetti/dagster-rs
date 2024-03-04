from dagster import load_assets_from_package_module
# from . import core
from . import recommender
from . import airbyte
from . import dbt

# core_assets = load_assets_from_package_module(
#     package_module=core, group_name='core',
    
# )
recommender_assets = load_assets_from_package_module(
    package_module=recommender, group_name='recommender'
)

airbyte_assets = all_assets = load_assets_from_package_module(
    package_module=airbyte
)

dbt_assets = all_assets = load_assets_from_package_module(
    package_module=dbt, group_name='airbyte_dbt',
)

