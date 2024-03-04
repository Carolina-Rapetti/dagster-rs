from dagster import Definitions, define_asset_job, AssetSelection, ScheduleDefinition, FilesystemIOManager
from dagster_mlflow import mlflow_tracking
from .resources import RESOURCES_LOCAL
from .assets import (recommender_assets, airbyte_assets, dbt_assets)

all_assets = [*recommender_assets, *airbyte_assets, *dbt_assets]

mlflow_resources = {
    'mlflow': {
        'config': {
            'experiment_name': 'recommender_system',
            'mlflow_tracking_uri': 'http://localhost:8002'
        }            
    },
}
# data_ops_config = {
#     'movies': {
#         'config': {
#             'uri': 'https://raw.githubusercontent.com/mlops-itba/Datos-RS/main/data/peliculas_0.csv'
#             }
#     }
# }

training_config = {
    'keras_dot_product_model': {
        'config': {
            'batch_size': 128,
            'epochs': 10,
            'learning_rate': 1e-3,
            'embeddings_dim': 5
        }
    }
}

job_data_config = {
    'resources': {
        **mlflow_resources
    },
    # 'ops': {
    #     **data_ops_config,
    # }
}

job_training_config = {
    'resources': {
        **mlflow_resources
    },
    'ops': {
        **training_config
    }
}

job_all_config = {
    'resources': {
        **mlflow_resources
    },
    'ops': {
        # **data_ops_config,
        **training_config
    }
}

get_data_job = define_asset_job(
    name='get_data',
    # selection=['movies', 'users', 'scores2', 'training_data'],
    selection=['recommender_system_raw/peliculas', 
               'recommender_system_raw/usuarios',
               'recommender_system_raw/scores', 
               'scores_peliculas_usuarios', 
               'peliculas', 
               'usuarios', 
               'scores', 
               'get_training_data'],
    # config=job_data_config
)

get_data_schedule = ScheduleDefinition(
    job=get_data_job,
    cron_schedule="0 * * * *",  # every hour
)

io_manager = FilesystemIOManager(
    base_dir="data",  # Path is built relative to where `dagster dev` is run
)

defs = Definitions(
    assets=all_assets,
    jobs=[
        get_data_job,
        define_asset_job("full_process", config=job_all_config),
        define_asset_job(
            "only_training",
            # selection=['preprocessed_training_data', 'user2Idx', 'movie2Idx'],
            selection=AssetSelection.groups('recommender'),
            config=job_training_config
        )
    ],
    resources={
        # 'mlflow': mlflow_tracking,
        "io_manager": io_manager,
        "dbt": RESOURCES_LOCAL['dbt'],
        # "airbyte": RESOURCES_LOCAL['airbyte']
    },
    schedules=[get_data_schedule],
    # sensors=all_sensors,
)
