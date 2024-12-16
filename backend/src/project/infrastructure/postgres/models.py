from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, BigInteger, Date, String, PrimaryKeyConstraint

from project.infrastructure.postgres.database import Base


class User(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(nullable=False, primary_key=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    avatar: Mapped[str] = mapped_column(nullable=True)
    isadmin: Mapped[bool] = mapped_column(default=False)


class Professor(Base):
    __tablename__ = "professor"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    start_contract: Mapped[date] = mapped_column(Date, nullable=False)
    end_contract: Mapped[date] = mapped_column(Date, nullable=False)
    birthday: Mapped[date] = mapped_column(Date, nullable=False)
    salary: Mapped[int] = mapped_column(BigInteger, nullable=False)


class Faculte(Base):
    __tablename__ = "faculte"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    decan: Mapped[int] = mapped_column(BigInteger, ForeignKey("professor.id"), nullable=False)


class Kafedra(Base):
    __tablename__ = "kafedra"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    faculte: Mapped[int] = mapped_column(BigInteger, ForeignKey("faculte.id"), nullable=True)


class Direction(Base):
    __tablename__ = "direction"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    kafedra: Mapped[int] = mapped_column(BigInteger, ForeignKey("kafedra.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)


class Grop(Base):
    __tablename__ = "grop"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    direction: Mapped[int] = mapped_column(BigInteger, ForeignKey("direction.id"), nullable=True)


class StudyPlan(Base):
    __tablename__ = "study_plan"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    start: Mapped[date] = mapped_column(nullable=False)
    end: Mapped[date] = mapped_column(nullable=False)
    direction: Mapped[int] = mapped_column(BigInteger, ForeignKey("direction.id"), nullable=True)


class Subject(Base):
    __tablename__ = "subject"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    passport: Mapped[int] = mapped_column(BigInteger, nullable=True)
    grop_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("grop.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    start_education: Mapped[date] = mapped_column(nullable=False)
    end_education: Mapped[date] = mapped_column(nullable=False)
    birthday: Mapped[date] = mapped_column(nullable=False)


class Nagruzka(Base):
    __tablename__ = "nagruzka"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    professor: Mapped[int] = mapped_column(BigInteger, ForeignKey("professor.id"), nullable=False)
    subject: Mapped[int] = mapped_column(BigInteger, ForeignKey("subject.id"), nullable=False)
    semester: Mapped[int] = mapped_column(Integer, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)



class Exam(Base):
    __tablename__ = "exam"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    exam_date: Mapped[date] = mapped_column(nullable=False)
    audience: Mapped[int] = mapped_column(BigInteger, nullable=False)
    subject: Mapped[int] = mapped_column(BigInteger, ForeignKey("subject.id"), nullable=True)
    professor: Mapped[int] = mapped_column(BigInteger, ForeignKey("professor.id"), nullable=True)


class Grade(Base):
    __tablename__ = "grade"

    student: Mapped[int] = mapped_column(BigInteger, ForeignKey("student.id"), nullable=False)
    exam: Mapped[int] = mapped_column(BigInteger, ForeignKey("exam.id"), nullable=False)
    grade: Mapped[int] = mapped_column(Integer, nullable=False)
    try_: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('student', 'exam'),
    )



class SubjectInStudy(Base):
    __tablename__ = "subject_in_study"

    study_plan: Mapped[int] = mapped_column(BigInteger, ForeignKey("study_plan.id"), nullable=False)
    subject: Mapped[int] = mapped_column(BigInteger, ForeignKey("subject.id"), nullable=False)
    hours: Mapped[int] = mapped_column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('study_plan', 'subject'),
    )
