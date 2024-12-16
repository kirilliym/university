from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.instances.university_db_instances import (
    ProfessorInstance, ProfessorCreateUpdateInstance,
    FaculteInstance, FaculteCreateUpdateInstance,
    KafedraInstance, KafedraCreateUpdateInstance,
    DirectionInstance, DirectionCreateUpdateInstance,
    GropInstance, GropCreateUpdateInstance,
    StudyPlanInstance, StudyPlanCreateUpdateInstance,
    SubjectInstance, SubjectCreateUpdateInstance,
    StudentInstance, StudentCreateUpdateInstance,
    NagruzkaInstance, NagruzkaCreateUpdateInstance,
    ExamInstance, ExamCreateUpdateInstance,
    GradeInstance, GradeCreateUpdateInstance,
    SubjectInStudyInstance, SubjectInStudyCreateUpdateInstance
)
from project.infrastructure.postgres.models import (
    Professor, Faculte, Kafedra, Direction, Grop, StudyPlan, Subject, Student, Nagruzka, Exam, Grade, SubjectInStudy
)
from project.core.university_db_exeptions import (
    ProfessorNotFound, ProfessorAlreadyExists,
    FaculteNotFound, FaculteAlreadyExists,
    KafedraNotFound, KafedraAlreadyExists,
    DirectionNotFound, DirectionAlreadyExists,
    GropNotFound, GropAlreadyExists,
    StudyPlanNotFound, StudyPlanAlreadyExists,
    SubjectNotFound, SubjectAlreadyExists,
    StudentNotFound, StudentAlreadyExists,
    NagruzkaNotFound, NagruzkaAlreadyExists,
    ExamNotFound, ExamAlreadyExists,
    GradeNotFound, GradeAlreadyExists,
    SubjectInStudyNotFound, SubjectInStudyAlreadyExists
)


class ProfessorRepository:
    _collection: Type[Professor] = Professor

    async def get_all_professors(self, session: AsyncSession) -> list[ProfessorInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [ProfessorInstance.model_validate(obj=professor) for professor in result.all()]

    async def get_professor_by_id(self, session: AsyncSession, professor_id: int) -> ProfessorInstance:
        query = select(self._collection).where(self._collection.id == professor_id)
        professor = await session.scalar(query)
        if not professor:
            raise ProfessorNotFound(_id=professor_id)
        return ProfessorInstance.model_validate(obj=professor)

    async def create_professor(self, session: AsyncSession, professor: ProfessorCreateUpdateInstance) -> ProfessorInstance:
        query = insert(self._collection).values(professor.model_dump()).returning(self._collection)
        try:
            created_professor = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise ProfessorAlreadyExists(name=professor.name)
        return ProfessorInstance.model_validate(obj=created_professor)

    async def update_professor(self, session: AsyncSession, professor_id: int, professor: ProfessorCreateUpdateInstance) -> ProfessorInstance:
        query = update(self._collection).where(self._collection.id == professor_id).values(professor.model_dump()).returning(self._collection)
        updated_professor = await session.scalar(query)
        if not updated_professor:
            raise ProfessorNotFound(_id=professor_id)
        return ProfessorInstance.model_validate(obj=updated_professor)

    async def delete_professor(self, session: AsyncSession, professor_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == professor_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise ProfessorNotFound(_id=professor_id)


class FaculteRepository:
    _collection: Type[Faculte] = Faculte

    async def get_all_facultes(self, session: AsyncSession) -> list[FaculteInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [FaculteInstance.model_validate(obj=faculte) for faculte in result.all()]

    async def get_faculte_by_id(self, session: AsyncSession, faculte_id: int) -> FaculteInstance:
        query = select(self._collection).where(self._collection.id == faculte_id)
        faculte = await session.scalar(query)
        if not faculte:
            raise FaculteNotFound(_id=faculte_id)
        return FaculteInstance.model_validate(obj=faculte)

    async def create_faculte(self, session: AsyncSession, faculte: FaculteCreateUpdateInstance) -> FaculteInstance:
        query = insert(self._collection).values(faculte.model_dump()).returning(self._collection)
        try:
            created_faculte = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise FaculteAlreadyExists(name=faculte.name)
        return FaculteInstance.model_validate(obj=created_faculte)

    async def update_faculte(self, session: AsyncSession, faculte_id: int, faculte: FaculteCreateUpdateInstance) -> FaculteInstance:
        query = update(self._collection).where(self._collection.id == faculte_id).values(faculte.model_dump()).returning(self._collection)
        updated_faculte = await session.scalar(query)
        if not updated_faculte:
            raise FaculteNotFound(_id=faculte_id)
        return FaculteInstance.model_validate(obj=updated_faculte)

    async def delete_faculte(self, session: AsyncSession, faculte_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == faculte_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise FaculteNotFound(_id=faculte_id)


class KafedraRepository:
    _collection: Type[Kafedra] = Kafedra

    async def get_all_kafedras(self, session: AsyncSession) -> list[KafedraInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [KafedraInstance.model_validate(obj=kafedra) for kafedra in result.all()]

    async def get_kafedra_by_id(self, session: AsyncSession, kafedra_id: int) -> KafedraInstance:
        query = select(self._collection).where(self._collection.id == kafedra_id)
        kafedra = await session.scalar(query)
        if not kafedra:
            raise KafedraNotFound(_id=kafedra_id)
        return KafedraInstance.model_validate(obj=kafedra)

    async def create_kafedra(self, session: AsyncSession, kafedra: KafedraCreateUpdateInstance) -> KafedraInstance:
        query = insert(self._collection).values(kafedra.model_dump()).returning(self._collection)
        try:
            created_kafedra = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise KafedraAlreadyExists(name=kafedra.name)
        return KafedraInstance.model_validate(obj=created_kafedra)

    async def update_kafedra(self, session: AsyncSession, kafedra_id: int, kafedra: KafedraCreateUpdateInstance) -> KafedraInstance:
        query = update(self._collection).where(self._collection.id == kafedra_id).values(kafedra.model_dump()).returning(self._collection)
        updated_kafedra = await session.scalar(query)
        if not updated_kafedra:
            raise KafedraNotFound(_id=kafedra_id)
        return KafedraInstance.model_validate(obj=updated_kafedra)

    async def delete_kafedra(self, session: AsyncSession, kafedra_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == kafedra_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise KafedraNotFound(_id=kafedra_id)


class DirectionRepository:
    _collection: Type[Direction] = Direction

    async def get_all_directions(self, session: AsyncSession) -> list[DirectionInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [DirectionInstance.model_validate(obj=direction) for direction in result.all()]

    async def get_direction_by_id(self, session: AsyncSession, direction_id: int) -> DirectionInstance:
        query = select(self._collection).where(self._collection.id == direction_id)
        direction = await session.scalar(query)
        if not direction:
            raise DirectionNotFound(_id=direction_id)
        return DirectionInstance.model_validate(obj=direction)

    async def create_direction(self, session: AsyncSession, direction: DirectionCreateUpdateInstance) -> DirectionInstance:
        query = insert(self._collection).values(direction.model_dump()).returning(self._collection)
        try:
            created_direction = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise DirectionAlreadyExists(name=direction.name)
        return DirectionInstance.model_validate(obj=created_direction)

    async def update_direction(self, session: AsyncSession, direction_id: int, direction: DirectionCreateUpdateInstance) -> DirectionInstance:
        query = update(self._collection).where(self._collection.id == direction_id).values(direction.model_dump()).returning(self._collection)
        updated_direction = await session.scalar(query)
        if not updated_direction:
            raise DirectionNotFound(_id=direction_id)
        return DirectionInstance.model_validate(obj=updated_direction)

    async def delete_direction(self, session: AsyncSession, direction_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == direction_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise DirectionNotFound(_id=direction_id)


class GropRepository:
    _collection: Type[Grop] = Grop

    async def get_all_groups(self, session: AsyncSession) -> list[GropInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [GropInstance.model_validate(obj=grop) for grop in result.all()]

    async def get_group_by_id(self, session: AsyncSession, group_id: int) -> GropInstance:
        query = select(self._collection).where(self._collection.id == group_id)
        grop = await session.scalar(query)
        if not grop:
            raise GropNotFound(_id=group_id)
        return GropInstance.model_validate(obj=grop)

    async def create_group(self, session: AsyncSession, grop: GropCreateUpdateInstance) -> GropInstance:
        query = insert(self._collection).values(grop.model_dump()).returning(self._collection)
        try:
            created_grop = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise GropAlreadyExists(name=grop.name)
        return GropInstance.model_validate(obj=created_grop)

    async def update_group(self, session: AsyncSession, group_id: int, grop: GropCreateUpdateInstance) -> GropInstance:
        query = update(self._collection).where(self._collection.id == group_id).values(grop.model_dump()).returning(self._collection)
        updated_grop = await session.scalar(query)
        if not updated_grop:
            raise GropNotFound(_id=group_id)
        return GropInstance.model_validate(obj=updated_grop)

    async def delete_group(self, session: AsyncSession, group_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == group_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise GropNotFound(_id=group_id)


class StudyPlanRepository:
    _collection: Type[StudyPlan] = StudyPlan

    async def get_all_study_plans(self, session: AsyncSession) -> list[StudyPlanInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [StudyPlanInstance.model_validate(obj=study_plan) for study_plan in result.all()]

    async def get_study_plan_by_id(self, session: AsyncSession, study_plan_id: int) -> StudyPlanInstance:
        query = select(self._collection).where(self._collection.id == study_plan_id)
        study_plan = await session.scalar(query)
        if not study_plan:
            raise StudyPlanNotFound(_id=study_plan_id)
        return StudyPlanInstance.model_validate(obj=study_plan)

    async def create_study_plan(self, session: AsyncSession, study_plan: StudyPlanCreateUpdateInstance) -> StudyPlanInstance:
        query = insert(self._collection).values(study_plan.model_dump()).returning(self._collection)
        try:
            created_study_plan = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise StudyPlanAlreadyExists(name=study_plan.name)
        return StudyPlanInstance.model_validate(obj=created_study_plan)

    async def update_study_plan(self, session: AsyncSession, study_plan_id: int, study_plan: StudyPlanCreateUpdateInstance) -> StudyPlanInstance:
        query = update(self._collection).where(self._collection.id == study_plan_id).values(study_plan.model_dump()).returning(self._collection)
        updated_study_plan = await session.scalar(query)
        if not updated_study_plan:
            raise StudyPlanNotFound(_id=study_plan_id)
        return StudyPlanInstance.model_validate(obj=updated_study_plan)

    async def delete_study_plan(self, session: AsyncSession, study_plan_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == study_plan_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise StudyPlanNotFound(_id=study_plan_id)


class SubjectRepository:
    _collection: Type[Subject] = Subject

    async def get_all_subjects(self, session: AsyncSession) -> list[SubjectInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [SubjectInstance.model_validate(obj=subject) for subject in result.all()]

    async def get_subject_by_id(self, session: AsyncSession, subject_id: int) -> SubjectInstance:
        query = select(self._collection).where(self._collection.id == subject_id)
        subject = await session.scalar(query)
        if not subject:
            raise SubjectNotFound(_id=subject_id)
        return SubjectInstance.model_validate(obj=subject)

    async def create_subject(self, session: AsyncSession, subject: SubjectCreateUpdateInstance) -> SubjectInstance:
        query = insert(self._collection).values(subject.model_dump()).returning(self._collection)
        try:
            created_subject = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise SubjectAlreadyExists(name=subject.name)
        return SubjectInstance.model_validate(obj=created_subject)

    async def update_subject(self, session: AsyncSession, subject_id: int, subject: SubjectCreateUpdateInstance) -> SubjectInstance:
        query = update(self._collection).where(self._collection.id == subject_id).values(subject.model_dump()).returning(self._collection)
        updated_subject = await session.scalar(query)
        if not updated_subject:
            raise SubjectNotFound(_id=subject_id)
        return SubjectInstance.model_validate(obj=updated_subject)

    async def delete_subject(self, session: AsyncSession, subject_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == subject_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise SubjectNotFound(_id=subject_id)


class StudentRepository:
    _collection: Type[Student] = Student

    async def get_all_students(self, session: AsyncSession) -> list[StudentInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [StudentInstance.model_validate(obj=student) for student in result.all()]

    async def get_student_by_id(self, session: AsyncSession, student_id: int) -> StudentInstance:
        query = select(self._collection).where(self._collection.id == student_id)
        student = await session.scalar(query)
        if not student:
            raise StudentNotFound(_id=student_id)
        return StudentInstance.model_validate(obj=student)

    async def create_student(self, session: AsyncSession, student: StudentCreateUpdateInstance) -> StudentInstance:
        query = insert(self._collection).values(student.model_dump()).returning(self._collection)
        try:
            created_student = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise StudentAlreadyExists(name=student.name)
        return StudentInstance.model_validate(obj=created_student)

    async def update_student(self, session: AsyncSession, student_id: int, student: StudentCreateUpdateInstance) -> StudentInstance:
        query = update(self._collection).where(self._collection.id == student_id).values(student.model_dump()).returning(self._collection)
        updated_student = await session.scalar(query)
        if not updated_student:
            raise StudentNotFound(_id=student_id)
        return StudentInstance.model_validate(obj=updated_student)

    async def delete_student(self, session: AsyncSession, student_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == student_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise StudentNotFound(_id=student_id)


class NagruzkaRepository:
    _collection: Type[Nagruzka] = Nagruzka

    async def get_all_nagruzka(self, session: AsyncSession) -> list[NagruzkaInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [NagruzkaInstance.model_validate(obj=nagruzka) for nagruzka in result.all()]

    async def get_nagruzka_by_id(self, session: AsyncSession, nagruzka_id: int) -> NagruzkaInstance:
        query = select(self._collection).where(self._collection.id == nagruzka_id)
        nagruzka = await session.scalar(query)
        if not nagruzka:
            raise NagruzkaNotFound(_id=nagruzka_id)
        return NagruzkaInstance.model_validate(obj=nagruzka)

    async def create_nagruzka(self, session: AsyncSession, nagruzka: NagruzkaCreateUpdateInstance) -> NagruzkaInstance:
        query = insert(self._collection).values(nagruzka.model_dump()).returning(self._collection)
        try:
            created_nagruzka = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise NagruzkaAlreadyExists(subject=nagruzka.subject)
        return NagruzkaInstance.model_validate(obj=created_nagruzka)

    async def update_nagruzka(self, session: AsyncSession, nagruzka_id: int, nagruzka: NagruzkaCreateUpdateInstance) -> NagruzkaInstance:
        query = update(self._collection).where(self._collection.id == nagruzka_id).values(nagruzka.model_dump()).returning(self._collection)
        updated_nagruzka = await session.scalar(query)
        if not updated_nagruzka:
            raise NagruzkaNotFound(_id=nagruzka_id)
        return NagruzkaInstance.model_validate(obj=updated_nagruzka)

    async def delete_nagruzka(self, session: AsyncSession, nagruzka_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == nagruzka_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise NagruzkaNotFound(_id=nagruzka_id)


class ExamRepository:
    _collection: Type[Exam] = Exam

    async def get_all_exams(self, session: AsyncSession) -> list[ExamInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [ExamInstance.model_validate(obj=exam) for exam in result.all()]

    async def get_exam_by_id(self, session: AsyncSession, exam_id: int) -> ExamInstance:
        query = select(self._collection).where(self._collection.id == exam_id)
        exam = await session.scalar(query)
        if not exam:
            raise ExamNotFound(_id=exam_id)
        return ExamInstance.model_validate(obj=exam)

    async def create_exam(self, session: AsyncSession, exam: ExamCreateUpdateInstance) -> ExamInstance:
        query = insert(self._collection).values(exam.model_dump()).returning(self._collection)
        try:
            created_exam = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise ExamAlreadyExists(name=exam.name)
        return ExamInstance.model_validate(obj=created_exam)

    async def update_exam(self, session: AsyncSession, exam_id: int, exam: ExamCreateUpdateInstance) -> ExamInstance:
        query = update(self._collection).where(self._collection.id == exam_id).values(exam.model_dump()).returning(self._collection)
        updated_exam = await session.scalar(query)
        if not updated_exam:
            raise ExamNotFound(_id=exam_id)
        return ExamInstance.model_validate(obj=updated_exam)

    async def delete_exam(self, session: AsyncSession, exam_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == exam_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise ExamNotFound(_id=exam_id)


class GradeRepository:
    _collection: Type[Grade] = Grade

    async def get_all_grades(self, session: AsyncSession) -> list[GradeInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [GradeInstance.model_validate(obj=grade) for grade in result.all()]

    async def get_grade_by_id(self, session: AsyncSession, grade_id: int) -> GradeInstance:
        query = select(self._collection).where(self._collection.id == grade_id)
        grade = await session.scalar(query)
        if not grade:
            raise GradeNotFound(_id=grade_id)
        return GradeInstance.model_validate(obj=grade)

    async def create_grade(self, session: AsyncSession, grade: GradeCreateUpdateInstance) -> GradeInstance:
        query = insert(self._collection).values(grade.model_dump()).returning(self._collection)
        try:
            created_grade = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise GradeAlreadyExists(student=grade.student, exam=grade.exam)
        return GradeInstance.model_validate(obj=created_grade)

    async def update_grade(self, session: AsyncSession, grade_id: int, grade: GradeCreateUpdateInstance) -> GradeInstance:
        query = update(self._collection).where(self._collection.id == grade_id).values(grade.model_dump()).returning(self._collection)
        updated_grade = await session.scalar(query)
        if not updated_grade:
            raise GradeNotFound(_id=grade_id)
        return GradeInstance.model_validate(obj=updated_grade)

    async def delete_grade(self, session: AsyncSession, grade_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == grade_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise GradeNotFound(_id=grade_id)


class SubjectInStudyRepository:
    _collection: Type[SubjectInStudy] = SubjectInStudy

    async def get_all_subject_in_study(self, session: AsyncSession) -> list[SubjectInStudyInstance]:
        query = select(self._collection)
        result = await session.scalars(query)
        return [SubjectInStudyInstance.model_validate(obj=subject_in_study) for subject_in_study in result.all()]

    async def get_subject_in_study_by_id(self, session: AsyncSession, subject_in_study_id: int) -> SubjectInStudyInstance:
        query = select(self._collection).where(self._collection.id == subject_in_study_id)
        subject_in_study = await session.scalar(query)
        if not subject_in_study:
            raise SubjectInStudyNotFound(_id=subject_in_study_id)
        return SubjectInStudyInstance.model_validate(obj=subject_in_study)

    async def create_subject_in_study(self, session: AsyncSession, subject_in_study: SubjectInStudyCreateUpdateInstance) -> SubjectInStudyInstance:
        query = insert(self._collection).values(subject_in_study.model_dump()).returning(self._collection)
        try:
            created_subject_in_study = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise SubjectInStudyAlreadyExists(study_plan=subject_in_study.study_plan, subject=subject_in_study.subject)
        return SubjectInStudyInstance.model_validate(obj=created_subject_in_study)

    async def update_subject_in_study(self, session: AsyncSession, subject_in_study_id: int, subject_in_study: SubjectInStudyCreateUpdateInstance) -> SubjectInStudyInstance:
        query = update(self._collection).where(self._collection.id == subject_in_study_id).values(subject_in_study.model_dump()).returning(self._collection)
        updated_subject_in_study = await session.scalar(query)
        if not updated_subject_in_study:
            raise SubjectInStudyNotFound(_id=subject_in_study_id)
        return SubjectInStudyInstance.model_validate(obj=updated_subject_in_study)

    async def delete_subject_in_study(self, session: AsyncSession, subject_in_study_id: int) -> None:
        query = delete(self._collection).where(self._collection.id == subject_in_study_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise SubjectInStudyNotFound(_id=subject_in_study_id)
