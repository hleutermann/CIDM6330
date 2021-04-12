"""
does this correlate to the baseapi.py of the first_refactor?
I see that the same import is used however I don't see any @abstractmethods in this refactor
It seems like the functions are completing different tasks but I think that's because of the structure
"""

_future__ import annotations
from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from barkylib import config
from barkylib.adapters import repository


class AbstractUnitOfWork(ABC):
    bookmarks: repository.AbstractBookmarkRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for bookmark in self.bookmarks.seen:
            while bookmark.events:
                yield bookmark.events.pop(0)

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_sqlite_memory_uri(),
        isolation_level="SERIALIZABLE",
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.bookmarks = repository.SqlAlchemyBookmarkRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()


class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.bookmarks = repository.FakeBookmarkRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass