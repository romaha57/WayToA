from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from config import HOST, PASSWORD, DB_NAME, USER

engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")

session = scoped_session(sessionmaker(bind=engine, autoflush=False))
Base = declarative_base()
Base.query = session.query_property()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True, name='номер')
    name = Column(String, name='название задачи')
    complexity = Column(Integer, name='сложность')
    count_solution = Column(Integer, name='количество решений')
    categories_id = relationship('Category', secondary='category_task', backref='tasks')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, name='название категории', unique=True)


class CategoryTask(Base):
    __tablename__ = 'category_task'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))


# Создание таблиц в БД
Base.metadata.create_all(engine)
