import logging.config
import os.path
from pathlib import Path

import sqlalchemy

from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from src.Services import *
from src.Services.FilesService.FilesService import FilesService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(
        yaml_files=[Path(os.path.sep.join(Path(os.path.realpath(__file__)).parts[:-3]))])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    database_engine = providers.Singleton(
        create_engine, "sqlite://db.sqlite"
    )

    files_db_service = providers.Factory(
        FilesService, database_engine
    )

