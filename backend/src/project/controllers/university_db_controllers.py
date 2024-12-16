from fastapi import APIRouter, HTTPException, status

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
from project.controllers.depences import (
    database, 
    professor_repo, 
    faculte_repo, 
    kafedra_repo, 
    direction_repo, 
    grop_repo, 
    study_plan_repo, 
    subject_repo, 
    student_repo, 
    nagruzka_repo, 
    exam_repo, 
    grade_repo, 
    subject_in_study_repo
)
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

university_db_router = APIRouter()


@university_db_router.get(
    "/all_professors",
    response_model=list[ProfessorInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_professors() -> list[ProfessorInstance]:
    async with database.session() as session:
        all_professors = await professor_repo.get_all_professors(session=session)

    return all_professors


@university_db_router.get(
    "/professor/{professor_id}",
    response_model=ProfessorInstance,
    status_code=status.HTTP_200_OK,
)
async def get_professor_by_id(
    professor_id: int,
) -> ProfessorInstance:
    try:
        async with database.session() as session:
            professor = await professor_repo.get_professor_by_id(session=session, professor_id=professor_id)
    except ProfessorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return professor


@university_db_router.post(
    "/add_professor",
    response_model=ProfessorInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_professor(
    professor_dto: ProfessorCreateUpdateInstance,
) -> ProfessorInstance:
    try:
        async with database.session() as session:
            new_professor = await professor_repo.create_professor(session=session, professor=professor_dto)
    except ProfessorAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_professor


@university_db_router.put(
    "/update_professor/{professor_id}",
    response_model=ProfessorInstance,
    status_code=status.HTTP_200_OK,
)
async def update_professor(
    professor_id: int,
    professor_dto: ProfessorCreateUpdateInstance,
) -> ProfessorInstance:
    try:
        async with database.session() as session:
            updated_professor = await professor_repo.update_professor(
                session=session,
                professor_id=professor_id,
                professor=professor_dto,
            )
    except ProfessorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_professor


@university_db_router.delete(
    "/delete_professor/{professor_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_professor(
    professor_id: int,
) -> None:
    try:
        async with database.session() as session:
            await professor_repo.delete_professor(session=session, professor_id=professor_id)
    except ProfessorNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Professor deleted successfully"}



@university_db_router.get(
    "/all_facultes",
    response_model=list[FaculteInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_facultes() -> list[FaculteInstance]:
    async with database.session() as session:
        all_facultes = await faculte_repo.get_all_facultes(session=session)

    return all_facultes


@university_db_router.get(
    "/faculte/{faculte_id}",
    response_model=FaculteInstance,
    status_code=status.HTTP_200_OK,
)
async def get_faculte_by_id(
    faculte_id: int,
) -> FaculteInstance:
    try:
        async with database.session() as session:
            faculte = await faculte_repo.get_faculte_by_id(session=session, faculte_id=faculte_id)
    except FaculteNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return faculte


@university_db_router.post(
    "/add_faculte",
    response_model=FaculteInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_faculte(
    faculte_dto: FaculteCreateUpdateInstance,
) -> FaculteInstance:
    try:
        async with database.session() as session:
            new_faculte = await faculte_repo.create_faculte(session=session, faculte=faculte_dto)
    except FaculteAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_faculte


@university_db_router.put(
    "/update_faculte/{faculte_id}",
    response_model=FaculteInstance,
    status_code=status.HTTP_200_OK,
)
async def update_faculte(
    faculte_id: int,
    faculte_dto: FaculteCreateUpdateInstance,
) -> FaculteInstance:
    try:
        async with database.session() as session:
            updated_faculte = await faculte_repo.update_faculte(
                session=session,
                faculte_id=faculte_id,
                faculte=faculte_dto,
            )
    except FaculteNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_faculte


@university_db_router.delete(
    "/delete_faculte/{faculte_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_faculte(
    faculte_id: int,
) -> None:
    try:
        async with database.session() as session:
            await faculte_repo.delete_faculte(session=session, faculte_id=faculte_id)
    except FaculteNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Faculte deleted successfully"}




@university_db_router.get(
    "/all_kafedras",
    response_model=list[KafedraInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_kafedras() -> list[KafedraInstance]:
    async with database.session() as session:
        all_kafedras = await kafedra_repo.get_all_kafedras(session=session)

    return all_kafedras


@university_db_router.get(
    "/kafedra/{kafedra_id}",
    response_model=KafedraInstance,
    status_code=status.HTTP_200_OK,
)
async def get_kafedra_by_id(
    kafedra_id: int,
) -> KafedraInstance:
    try:
        async with database.session() as session:
            kafedra = await kafedra_repo.get_kafedra_by_id(session=session, kafedra_id=kafedra_id)
    except KafedraNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return kafedra


@university_db_router.post(
    "/add_kafedra",
    response_model=KafedraInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_kafedra(
    kafedra_dto: KafedraCreateUpdateInstance,
) -> KafedraInstance:
    try:
        async with database.session() as session:
            new_kafedra = await kafedra_repo.create_kafedra(session=session, kafedra=kafedra_dto)
    except KafedraAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_kafedra


@university_db_router.put(
    "/update_kafedra/{kafedra_id}",
    response_model=KafedraInstance,
    status_code=status.HTTP_200_OK,
)
async def update_kafedra(
    kafedra_id: int,
    kafedra_dto: KafedraCreateUpdateInstance,
) -> KafedraInstance:
    try:
        async with database.session() as session:
            updated_kafedra = await kafedra_repo.update_kafedra(
                session=session,
                kafedra_id=kafedra_id,
                kafedra=kafedra_dto,
            )
    except KafedraNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_kafedra


@university_db_router.delete(
    "/delete_kafedra/{kafedra_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_kafedra(
    kafedra_id: int,
) -> None:
    try:
        async with database.session() as session:
            await kafedra_repo.delete_kafedra(session=session, kafedra_id=kafedra_id)
    except KafedraNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Kafedra deleted successfully"}





@university_db_router.get(
    "/all_directions",
    response_model=list[DirectionInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_directions() -> list[DirectionInstance]:
    async with database.session() as session:
        all_directions = await direction_repo.get_all_directions(session=session)

    return all_directions


@university_db_router.get(
    "/direction/{direction_id}",
    response_model=DirectionInstance,
    status_code=status.HTTP_200_OK,
)
async def get_direction_by_id(
    direction_id: int,
) -> DirectionInstance:
    try:
        async with database.session() as session:
            direction = await direction_repo.get_direction_by_id(session=session, direction_id=direction_id)
    except DirectionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return direction


@university_db_router.post(
    "/add_direction",
    response_model=DirectionInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_direction(
    direction_dto: DirectionCreateUpdateInstance,
) -> DirectionInstance:
    try:
        async with database.session() as session:
            new_direction = await direction_repo.create_direction(session=session, direction=direction_dto)
    except DirectionAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_direction


@university_db_router.put(
    "/update_direction/{direction_id}",
    response_model=DirectionInstance,
    status_code=status.HTTP_200_OK,
)
async def update_direction(
    direction_id: int,
    direction_dto: DirectionCreateUpdateInstance,
) -> DirectionInstance:
    try:
        async with database.session() as session:
            updated_direction = await direction_repo.update_direction(
                session=session,
                direction_id=direction_id,
                direction=direction_dto,
            )
    except DirectionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_direction


@university_db_router.delete(
    "/delete_direction/{direction_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_direction(
    direction_id: int,
) -> None:
    try:
        async with database.session() as session:
            await direction_repo.delete_direction(session=session, direction_id=direction_id)
    except DirectionNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Direction deleted successfully"}





@university_db_router.get(
    "/all_groups",
    response_model=list[GropInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_groups() -> list[GropInstance]:
    async with database.session() as session:
        all_groups = await grop_repo.get_all_groups(session=session)

    return all_groups


@university_db_router.get(
    "/group/{group_id}",
    response_model=GropInstance,
    status_code=status.HTTP_200_OK,
)
async def get_group_by_id(
    group_id: int,
) -> GropInstance:
    try:
        async with database.session() as session:
            grop = await grop_repo.get_group_by_id(session=session, group_id=group_id)
    except GropNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return grop


@university_db_router.post(
    "/add_group",
    response_model=GropInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_group(
    grop_dto: GropCreateUpdateInstance,
) -> GropInstance:
    try:
        async with database.session() as session:
            new_grop = await grop_repo.create_group(session=session, grop=grop_dto)
    except GropAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_grop


@university_db_router.put(
    "/update_group/{group_id}",
    response_model=GropInstance,
    status_code=status.HTTP_200_OK,
)
async def update_group(
    group_id: int,
    grop_dto: GropCreateUpdateInstance,
) -> GropInstance:
    try:
        async with database.session() as session:
            updated_grop = await grop_repo.update_group(
                session=session,
                group_id=group_id,
                grop=grop_dto,
            )
    except GropNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_grop


@university_db_router.delete(
    "/delete_group/{group_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_group(
    group_id: int,
) -> None:
    try:
        async with database.session() as session:
            await grop_repo.delete_group(session=session, group_id=group_id)
    except GropNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Group deleted successfully"}







@university_db_router.get(
    "/all_study_plans",
    response_model=list[StudyPlanInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_study_plans() -> list[StudyPlanInstance]:
    async with database.session() as session:
        all_study_plans = await study_plan_repo.get_all_study_plans(session=session)

    return all_study_plans


@university_db_router.get(
    "/study_plan/{study_plan_id}",
    response_model=StudyPlanInstance,
    status_code=status.HTTP_200_OK,
)
async def get_study_plan_by_id(
    study_plan_id: int,
) -> StudyPlanInstance:
    try:
        async with database.session() as session:
            study_plan = await study_plan_repo.get_study_plan_by_id(session=session, study_plan_id=study_plan_id)
    except StudyPlanNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return study_plan


@university_db_router.post(
    "/add_study_plan",
    response_model=StudyPlanInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_study_plan(
    study_plan_dto: StudyPlanCreateUpdateInstance,
) -> StudyPlanInstance:
    try:
        async with database.session() as session:
            new_study_plan = await study_plan_repo.create_study_plan(session=session, study_plan=study_plan_dto)
    except StudyPlanAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_study_plan


@university_db_router.put(
    "/update_study_plan/{study_plan_id}",
    response_model=StudyPlanInstance,
    status_code=status.HTTP_200_OK,
)
async def update_study_plan(
    study_plan_id: int,
    study_plan_dto: StudyPlanCreateUpdateInstance,
) -> StudyPlanInstance:
    try:
        async with database.session() as session:
            updated_study_plan = await study_plan_repo.update_study_plan(
                session=session,
                study_plan_id=study_plan_id,
                study_plan=study_plan_dto,
            )
    except StudyPlanNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_study_plan


@university_db_router.delete(
    "/delete_study_plan/{study_plan_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_study_plan(
    study_plan_id: int,
) -> None:
    try:
        async with database.session() as session:
            await study_plan_repo.delete_study_plan(session=session, study_plan_id=study_plan_id)
    except StudyPlanNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Study plan deleted successfully"}



@university_db_router.get(
    "/all_subjects",
    response_model=list[SubjectInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_subjects() -> list[SubjectInstance]:
    async with database.session() as session:
        all_subjects = await subject_repo.get_all_subjects(session=session)

    return all_subjects


@university_db_router.get(
    "/subject/{subject_id}",
    response_model=SubjectInstance,
    status_code=status.HTTP_200_OK,
)
async def get_subject_by_id(
    subject_id: int,
) -> SubjectInstance:
    try:
        async with database.session() as session:
            subject = await subject_repo.get_subject_by_id(session=session, subject_id=subject_id)
    except SubjectNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return subject


@university_db_router.post(
    "/add_subject",
    response_model=SubjectInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_subject(
    subject_dto: SubjectCreateUpdateInstance,
) -> SubjectInstance:
    try:
        async with database.session() as session:
            new_subject = await subject_repo.create_subject(session=session, subject=subject_dto)
    except SubjectAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_subject


@university_db_router.put(
    "/update_subject/{subject_id}",
    response_model=SubjectInstance,
    status_code=status.HTTP_200_OK,
)
async def update_subject(
    subject_id: int,
    subject_dto: SubjectCreateUpdateInstance,
) -> SubjectInstance:
    try:
        async with database.session() as session:
            updated_subject = await subject_repo.update_subject(
                session=session,
                subject_id=subject_id,
                subject=subject_dto,
            )
    except SubjectNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_subject


@university_db_router.delete(
    "/delete_subject/{subject_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_subject(
    subject_id: int,
) -> None:
    try:
        async with database.session() as session:
            await subject_repo.delete_subject(session=session, subject_id=subject_id)
    except SubjectNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Subject deleted successfully"}






@university_db_router.get(
    "/all_students",
    response_model=list[StudentInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_students() -> list[StudentInstance]:
    async with database.session() as session:
        all_students = await student_repo.get_all_students(session=session)

    return all_students


@university_db_router.get(
    "/student/{student_id}",
    response_model=StudentInstance,
    status_code=status.HTTP_200_OK,
)
async def get_student_by_id(
    student_id: int,
) -> StudentInstance:
    try:
        async with database.session() as session:
            student = await student_repo.get_student_by_id(session=session, student_id=student_id)
    except StudentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return student


@university_db_router.post(
    "/add_student",
    response_model=StudentInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_student(
    student_dto: StudentCreateUpdateInstance,
) -> StudentInstance:
    try:
        async with database.session() as session:
            new_student = await student_repo.create_student(session=session, student=student_dto)
    except StudentAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_student


@university_db_router.put(
    "/update_student/{student_id}",
    response_model=StudentInstance,
    status_code=status.HTTP_200_OK,
)
async def update_student(
    student_id: int,
    student_dto: StudentCreateUpdateInstance,
) -> StudentInstance:
    try:
        async with database.session() as session:
            updated_student = await student_repo.update_student(
                session=session,
                student_id=student_id,
                student=student_dto,
            )
    except StudentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_student


@university_db_router.delete(
    "/delete_student/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student(
    student_id: int,
) -> None:
    try:
        async with database.session() as session:
            await student_repo.delete_student(session=session, student_id=student_id)
    except StudentNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Student deleted successfully"}







@university_db_router.get(
    "/all_nagruzka",
    response_model=list[NagruzkaInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_nagruzka() -> list[NagruzkaInstance]:
    async with database.session() as session:
        all_nagruzka = await nagruzka_repo.get_all_nagruzka(session=session)

    return all_nagruzka


@university_db_router.get(
    "/nagruzka/{nagruzka_id}",
    response_model=NagruzkaInstance,
    status_code=status.HTTP_200_OK,
)
async def get_nagruzka_by_id(
    nagruzka_id: int,
) -> NagruzkaInstance:
    try:
        async with database.session() as session:
            nagruzka = await nagruzka_repo.get_nagruzka_by_id(session=session, nagruzka_id=nagruzka_id)
    except NagruzkaNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return nagruzka


@university_db_router.post(
    "/add_nagruzka",
    response_model=NagruzkaInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_nagruzka(
    nagruzka_dto: NagruzkaCreateUpdateInstance,
) -> NagruzkaInstance:
    try:
        async with database.session() as session:
            new_nagruzka = await nagruzka_repo.create_nagruzka(session=session, nagruzka=nagruzka_dto)
    except NagruzkaAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_nagruzka


@university_db_router.put(
    "/update_nagruzka/{nagruzka_id}",
    response_model=NagruzkaInstance,
    status_code=status.HTTP_200_OK,
)
async def update_nagruzka(
    nagruzka_id: int,
    nagruzka_dto: NagruzkaCreateUpdateInstance,
) -> NagruzkaInstance:
    try:
        async with database.session() as session:
            updated_nagruzka = await nagruzka_repo.update_nagruzka(
                session=session,
                nagruzka_id=nagruzka_id,
                nagruzka=nagruzka_dto,
            )
    except NagruzkaNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_nagruzka


@university_db_router.delete(
    "/delete_nagruzka/{nagruzka_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_nagruzka(
    nagruzka_id: int,
) -> None:
    try:
        async with database.session() as session:
            await nagruzka_repo.delete_nagruzka(session=session, nagruzka_id=nagruzka_id)
    except NagruzkaNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Nagruzka deleted successfully"}





@university_db_router.get(
    "/all_exams",
    response_model=list[ExamInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_exams() -> list[ExamInstance]:
    async with database.session() as session:
        all_exams = await exam_repo.get_all_exams(session=session)

    return all_exams


@university_db_router.get(
    "/exam/{exam_id}",
    response_model=ExamInstance,
    status_code=status.HTTP_200_OK,
)
async def get_exam_by_id(
    exam_id: int,
) -> ExamInstance:
    try:
        async with database.session() as session:
            exam = await exam_repo.get_exam_by_id(session=session, exam_id=exam_id)
    except ExamNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return exam


@university_db_router.post(
    "/add_exam",
    response_model=ExamInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_exam(
    exam_dto: ExamCreateUpdateInstance,
) -> ExamInstance:
    try:
        async with database.session() as session:
            new_exam = await exam_repo.create_exam(session=session, exam=exam_dto)
    except ExamAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_exam


@university_db_router.put(
    "/update_exam/{exam_id}",
    response_model=ExamInstance,
    status_code=status.HTTP_200_OK,
)
async def update_exam(
    exam_id: int,
    exam_dto: ExamCreateUpdateInstance,
) -> ExamInstance:
    try:
        async with database.session() as session:
            updated_exam = await exam_repo.update_exam(
                session=session,
                exam_id=exam_id,
                exam=exam_dto,
            )
    except ExamNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_exam


@university_db_router.delete(
    "/delete_exam/{exam_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_exam(
    exam_id: int,
) -> None:
    try:
        async with database.session() as session:
            await exam_repo.delete_exam(session=session, exam_id=exam_id)
    except ExamNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Exam deleted successfully"}




@university_db_router.get(
    "/all_grades",
    response_model=list[GradeInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_grades() -> list[GradeInstance]:
    async with database.session() as session:
        all_grades = await grade_repo.get_all_grades(session=session)

    return all_grades


@university_db_router.get(
    "/grade/{grade_id}",
    response_model=GradeInstance,
    status_code=status.HTTP_200_OK,
)
async def get_grade_by_id(
    grade_id: int,
) -> GradeInstance:
    try:
        async with database.session() as session:
            grade = await grade_repo.get_grade_by_id(session=session, grade_id=grade_id)
    except GradeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return grade


@university_db_router.post(
    "/add_grade",
    response_model=GradeInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_grade(
    grade_dto: GradeCreateUpdateInstance,
) -> GradeInstance:
    try:
        async with database.session() as session:
            new_grade = await grade_repo.create_grade(session=session, grade=grade_dto)
    except GradeAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_grade


@university_db_router.put(
    "/update_grade/{grade_id}",
    response_model=GradeInstance,
    status_code=status.HTTP_200_OK,
)
async def update_grade(
    grade_id: int,
    grade_dto: GradeCreateUpdateInstance,
) -> GradeInstance:
    try:
        async with database.session() as session:
            updated_grade = await grade_repo.update_grade(
                session=session,
                grade_id=grade_id,
                grade=grade_dto,
            )
    except GradeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_grade


@university_db_router.delete(
    "/delete_grade/{grade_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_grade(
    grade_id: int,
) -> None:
    try:
        async with database.session() as session:
            await grade_repo.delete_grade(session=session, grade_id=grade_id)
    except GradeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "Grade deleted successfully"}





@university_db_router.get(
    "/all_subject_in_study",
    response_model=list[SubjectInStudyInstance],
    status_code=status.HTTP_200_OK,
)
async def get_all_subject_in_study() -> list[SubjectInStudyInstance]:
    async with database.session() as session:
        all_subject_in_study = await subject_in_study_repo.get_all_subject_in_study(session=session)

    return all_subject_in_study


@university_db_router.get(
    "/subject_in_study/{subject_in_study_id}",
    response_model=SubjectInStudyInstance,
    status_code=status.HTTP_200_OK,
)
async def get_subject_in_study_by_id(
    subject_in_study_id: int,
) -> SubjectInStudyInstance:
    try:
        async with database.session() as session:
            subject_in_study = await subject_in_study_repo.get_subject_in_study_by_id(session=session, subject_in_study_id=subject_in_study_id)
    except SubjectInStudyNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return subject_in_study


@university_db_router.post(
    "/add_subject_in_study",
    response_model=SubjectInStudyInstance,
    status_code=status.HTTP_201_CREATED,
)
async def add_subject_in_study(
    subject_in_study_dto: SubjectInStudyCreateUpdateInstance,
) -> SubjectInStudyInstance:
    try:
        async with database.session() as session:
            new_subject_in_study = await subject_in_study_repo.create_subject_in_study(session=session, subject_in_study=subject_in_study_dto)
    except SubjectInStudyAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_subject_in_study


@university_db_router.put(
    "/update_subject_in_study/{subject_in_study_id}",
    response_model=SubjectInStudyInstance,
    status_code=status.HTTP_200_OK,
)
async def update_subject_in_study(
    subject_in_study_id: int,
    subject_in_study_dto: SubjectInStudyCreateUpdateInstance,
) -> SubjectInStudyInstance:
    try:
        async with database.session() as session:
            updated_subject_in_study = await subject_in_study_repo.update_subject_in_study(
                session=session,
                subject_in_study_id=subject_in_study_id,
                subject_in_study=subject_in_study_dto,
            )
    except SubjectInStudyNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_subject_in_study


@university_db_router.delete(
    "/delete_subject_in_study/{subject_in_study_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_subject_in_study(
    subject_in_study_id: int,
) -> None:
    try:
        async with database.session() as session:
            await subject_in_study_repo.delete_subject_in_study(session=session, subject_in_study_id=subject_in_study_id)
    except SubjectInStudyNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return {"detail": "SubjectInStudy deleted successfully"}
