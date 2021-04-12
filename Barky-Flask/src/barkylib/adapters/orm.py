import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)

from sqlalchemy.orm import registry, mapper, relationship

from barkylib.domain.models import Bookmark

mapper_registry = registry()
Base = mapper_registry.generate_base()

logger = logging.getLogger(__name__)
metadata = MetaData()

"""
Pure domain bookmark:
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL
date_edited TEXT NOT NULL
"""
bookmarks = Table(
    "bookmarks",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(255), unique=True),
    Column("url", String(255)),
    Column("notes", Text),
    Column("date_added", Text),
    Column("date_edited", Text),
)

def start_mappers():
    
    logger.info("starting mappers")
    # mapper_registry.map_imperatively(Bookmark, bookmarks)
    mapper(Bookmark, bookmarks)