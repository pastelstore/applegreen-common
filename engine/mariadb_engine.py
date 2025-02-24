import logging

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from constant.constant import AG_DB, AG_DB_URI


class ConnectionManager:
    def __init__(self):
        self._session = None
        self._engine = None

    def create_session(self, app: FastAPI):
        self._engine = create_engine(AG_DB_URI, echo=True, pool_recycle=100)
        self._session = sessionmaker(bind=self._engine)

        @app.on_event("startup")
        def startup():
            self._engine.connect()
            logging.info(f"connected database {AG_DB}")

        @app.on_event("shutdown")
        def shutdown():
            self._session.close_all()
            self._engine.dispose()
            logging.info(f"disconnected database {AG_DB}")

    def get_db(self):
        if self._session is None:
            raise Exception("must be called 'create_session'")
        db_session = None
        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    @property
    def session(self):
        return self.get_db

    @property
    def engine(self):
        return self._engine


# define database
database = ConnectionManager()
