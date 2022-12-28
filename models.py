from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DATE
from datetime import datetime

Base = declarative_base()

class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(30), nullable=False)
    students = relationship('Students', back_populates='group')

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(150), nullable=False)
    id_group = Column(Integer, ForeignKey(Groups.id))
    group = relationship('Groups', back_populates='students')
    grade = relationship('Gradebook', back_populates='student')

class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(150), nullable=False)
    subjects = relationship('Subjects', back_populates='teacher')

class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(150), nullable=False)
    id_teacher = Column(Integer, ForeignKey(Teachers.id))
    teacher = relationship('Teachers', back_populates='subjects')
    grade = relationship('Gradebook', back_populates='subject')

class Gradebook(Base):
    __tablename__ = "gradebook"
    id_student = Column(Integer, ForeignKey(Students.id, ondelete='CASCADE'), primary_key=True)
    id_subject = Column(Integer, ForeignKey(Subjects.id, ondelete='CASCADE'), primary_key=True)
    grade = Column(Integer, default=0)
    createdAt = Column(DATE, default=datetime.now().strftime('%Y-%m-%d'), primary_key=True)
    student = relationship('Students', back_populates='grade')
    subject = relationship('Subjects', back_populates='grade')
