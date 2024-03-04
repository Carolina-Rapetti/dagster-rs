from dagster import EnvVar



AIRBYTE_CONFIG = {
    "host":"localhost",
    "port":"8000",
    # If using basic auth, include username and password:
    "username":"airbyte",
    "password": {"env": "AIRBYTE_PASSWORD"}
}