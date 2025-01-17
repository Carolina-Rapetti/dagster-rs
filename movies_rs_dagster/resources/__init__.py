import os
from pathlib import Path

from dagster._utils import file_relative_path
from dagster import EnvVar
# from dagster_aws.s3 import S3Resource
# from dagster_aws.s3.io_manager import S3PickleIOManager
from dagster_dbt import DbtCliResource
# from dagster_pyspark import pyspark_resource

# from .duckdb_parquet_io_manager import DuckDBPartitionedParquetIOManager
# from .hn_resource import HNAPIClient, HNAPISubsampleClient
# from .parquet_io_manager import (
#     LocalPartitionedParquetIOManager,
#     S3PartitionedParquetIOManager,
# )
# from .snowflake_io_manager import SnowflakeIOManager

# AIRBYTE_CONFIG = {
#     "host":"localhost",
#     "port":"8000",
#     # If using basic auth, include username and password:
#     "username":"airbyte",
#     "password":"password",
# }

# airbyte_instance = AirbyteResource(
#     host="localhost",
#     port="8000",
#     # If using basic auth, include username and password:
#     username="airbyte",
#     password=EnvVar("AIRBYTE_PASSWORD"),
# )

DBT_PROJECT_DIR = file_relative_path(__file__, "../../../mlops-ecosystem/db_postgres")
DBT_PROFILES_DIR = "C:/Users/fla_4/.dbt"

dbt_local_resource = DbtCliResource(
    project_dir="C:/Users/fla_4/Documents/mlops/mlops-ecosystem/db_postgres",
    profiles_dir="C:/Users/fla_4/.dbt/"
)
# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at runtime.
# Otherwise, we expect a manifest to be present in the project's target directory.
# if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
#     dbt_parse_invocation = dbt_local_resource.cli(["parse"], manifest={}).wait()
#     dbt_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
# else:
#     dbt_manifest_path = Path(DBT_PROJECT_DIR).joinpath("target", "manifest.json")

# dbt_staging_resource = DbtCliResource(
#     project_dir=DBT_PROJECT_DIR,
#     target="staging",
# )
# dbt_prod_resource = DbtCliResource(
#     project_dir=DBT_PROJECT_DIR,
#     target="prod",
# )


# configured_pyspark = pyspark_resource.configured(
#     {
#         "spark_conf": {
#             "spark.jars.packages": ",".join(
#                 [
#                     "net.snowflake:snowflake-jdbc:3.8.0",
#                     "net.snowflake:spark-snowflake_2.12:2.8.2-spark_3.0",
#                     "com.amazonaws:aws-java-sdk:1.7.4,org.apache.hadoop:hadoop-aws:2.7.7",
#                 ]
#             ),
#             "spark.hadoop.fs.s3.impl": "org.apache.hadoop.fs.s3native.NativeS3FileSystem",
#             "spark.hadoop.fs.s3.awsAccessKeyId": os.getenv("AWS_ACCESS_KEY_ID", ""),
#             "spark.hadoop.fs.s3.awsSecretAccessKey": os.getenv("AWS_SECRET_ACCESS_KEY", ""),
#             "spark.hadoop.fs.s3.buffer.dir": "/tmp",
#         }
#     }
# )

# SHARED_SNOWFLAKE_CONF = {
#     "account": os.getenv("SNOWFLAKE_ACCOUNT", ""),
#     "user": os.getenv("SNOWFLAKE_USER", ""),
#     "password": os.getenv("SNOWFLAKE_PASSWORD", ""),
#     "warehouse": "TINY_WAREHOUSE",
# }

# RESOURCES_PROD = {
#     "io_manager": S3PickleIOManager(
#         s3_resource=S3Resource.configure_at_launch(),
#         s3_bucket="hackernews-elementl-prod",
#     ),
#     "parquet_io_manager": S3PartitionedParquetIOManager(
#         pyspark=configured_pyspark, s3_bucket="hackernews-elementl-dev"
#     ),
#     "warehouse_io_manager": SnowflakeIOManager(database="DEMO_DB", **SHARED_SNOWFLAKE_CONF),
#     "hn_client": HNAPISubsampleClient(subsample_rate=10),
#     "dbt": dbt_prod_resource,
# }


# RESOURCES_STAGING = {
#     "io_manager": S3PickleIOManager(
#         s3_resource=S3Resource.configure_at_launch(),
#         s3_bucket="hackernews-elementl-dev",
#     ),
#     "parquet_io_manager": S3PartitionedParquetIOManager(
#         pyspark=configured_pyspark, s3_bucket="hackernews-elementl-dev"
#     ),
#     "warehouse_io_manager": SnowflakeIOManager(database="DEMO_DB_STAGING", **SHARED_SNOWFLAKE_CONF),
#     "hn_client": HNAPISubsampleClient(subsample_rate=10),
#     "dbt": dbt_staging_resource,
# }


RESOURCES_LOCAL = {
    # "parquet_io_manager": LocalPartitionedParquetIOManager(pyspark=configured_pyspark),
    # "warehouse_io_manager": DuckDBPartitionedParquetIOManager(
    #     pyspark=configured_pyspark,
    #     duckdb_path=os.path.join(DBT_PROJECT_DIR, "hackernews.duckdb"),
    # ),
    # "hn_client": HNAPIClient(),
    "dbt": dbt_local_resource,
    # "airbyte": airbyte_instance
}
