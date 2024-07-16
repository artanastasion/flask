from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from . db_session import SqlAlchemyBase
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, orm


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', foreign_keys=[user_id])
    job = Column(String, nullable=True)
    work_size = Column(Integer, nullable=True)
    collaborators = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    is_finished = Column(Boolean, nullable=True)

    def __repr__(self):
        return f"<Job> {self.id} {self.job} {self.user}"
