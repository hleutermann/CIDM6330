import sys
from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(ABC):
    pass


@dataclass
class AddBookmarkCommand(Command):
    id: int
    title: str
    url: str
    # data["date_added"] = datetime.utcnow().isoformat()
    date_added: str
    date_edited: str
    notes: Optional[str] = None


@dataclass
class ListBookmarksCommand(Command):
    order_by: str
    order: str


@dataclass
class DeleteBookmarkCommand(Command):
    id: int


@dataclass
class EditBookmarkCommand(Command):
    id: int
    title: str
    url: str
    # data["date_added"] = datetime.utcnow().isoformat()
    date_added: str
    date_edited: str
    notes: Optional[str] = None