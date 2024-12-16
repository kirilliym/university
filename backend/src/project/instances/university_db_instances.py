from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional


class ProfessorCreateUpdateInstance(BaseModel):
    name: str
    start_contract: date
    end_contract: date
    birthday: date
    salary: int


class ProfessorInstance(ProfessorCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class FaculteCreateUpdateInstance(BaseModel):
    name: str
    decan: int


class FaculteInstance(FaculteCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class KafedraCreateUpdateInstance(BaseModel):
    name: str
    faculte: Optional[int]


class KafedraInstance(KafedraCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class DirectionCreateUpdateInstance(BaseModel):
    kafedra: Optional[int]
    name: str


class DirectionInstance(DirectionCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class GropCreateUpdateInstance(BaseModel):
    name: Optional[str]
    direction: Optional[int]


class GropInstance(GropCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class StudyPlanCreateUpdateInstance(BaseModel):
    start: date
    end: date
    direction: Optional[int]


class StudyPlanInstance(StudyPlanCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class SubjectCreateUpdateInstance(BaseModel):
    name: str


class SubjectInstance(SubjectCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class StudentCreateUpdateInstance(BaseModel):
    passport: Optional[int]
    grop_id: Optional[int]
    name: str
    start_education: date
    end_education: date
    birthday: date


class StudentInstance(StudentCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class NagruzkaCreateUpdateInstance(BaseModel):
    professor: int
    subject: int
    semester: int
    year: int


class NagruzkaInstance(NagruzkaCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)


class ExamCreateUpdateInstance(BaseModel):
    name: str
    exam_date: date
    audience: int
    subject: Optional[int]
    professor: Optional[int]


class ExamInstance(ExamCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
    id: int


class GradeCreateUpdateInstance(BaseModel):
    student: int
    exam: int
    grade: int
    try_: int


class GradeInstance(GradeCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)


class SubjectInStudyCreateUpdateInstance(BaseModel):
    study_plan: int
    subject: int
    hours: int


class SubjectInStudyInstance(SubjectInStudyCreateUpdateInstance):
    model_config = ConfigDict(from_attributes=True)
