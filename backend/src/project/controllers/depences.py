from typing import Annotated
from fastapi import Depends, HTTPException, status

from project.utils.jwt_utils import JwtUtil
from project.instances.user import UserResponse
from project.infrastructure.postgres.repository.user_repo import UserRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.infrastructure.postgres.repository.university_db_repo import (
    ProfessorRepository, 
    FaculteRepository, KafedraRepository, DirectionRepository,
    GropRepository, StudyPlanRepository, SubjectRepository, StudentRepository,
    NagruzkaRepository, ExamRepository, GradeRepository, SubjectInStudyRepository
)

user_repo = UserRepository()
professor_repo = ProfessorRepository()
faculte_repo = FaculteRepository()
kafedra_repo = KafedraRepository()
direction_repo = DirectionRepository()
grop_repo = GropRepository()
study_plan_repo = StudyPlanRepository()
subject_repo = SubjectRepository()
student_repo = StudentRepository()
nagruzka_repo = NagruzkaRepository()
exam_repo = ExamRepository()
grade_repo = GradeRepository()
subject_in_study_repo = SubjectInStudyRepository()

database = PostgresDatabase()


async def get_user_from_token(token: Annotated[str, Depends(JwtUtil.oauth2_scheme)]) -> UserResponse:
    user_login = JwtUtil.login_from_token(token=token)

    async with database.session() as session:
        user = await user_repo.get_user_by_login(login=user_login, session=session)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return UserResponse(login=user.login, avatar=user.avatar, isadmin=user.isadmin)

def check_for_admin_permissions(user: UserResponse):
    if user.isadmin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No permissions for this")