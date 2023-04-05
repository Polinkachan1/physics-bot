import sqlalchemy
from .db_session import SqlAlchemyBase


class Formula(SqlAlchemyBase):
    __tablename__ = 'formulas'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    grade = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    topic = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    formula_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    formula = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    explanation = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    details = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
