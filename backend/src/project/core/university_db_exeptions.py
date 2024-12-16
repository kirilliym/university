from typing import Final
from fastapi import HTTPException, status

class ProfessorNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Professor с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class ProfessorAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Professor с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class FaculteNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Faculty с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class FaculteAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Faculty с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class KafedraNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Department с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class KafedraAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Department с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class DirectionNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Direction с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class DirectionAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Direction с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class GropNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Group с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class GropAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Group с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class StudyPlanNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "StudyPlan с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class StudyPlanAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "StudyPlan с названием '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class SubjectNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Subject с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class SubjectAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Subject с названием '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class StudentNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Student с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class StudentAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Student с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class NagruzkaNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Nagruzka с id {id} не найдена"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class NagruzkaAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Nagruzka с id {id} уже существует"

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class ExamNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Exam с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class ExamAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Exam с названием '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class GradeNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Grade с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class GradeAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Grade с id {id} уже существует"

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class SubjectInStudyNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "SubjectInStudy с id {id} не найден"
    message: str

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)


class SubjectInStudyAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "SubjectInStudy с id {id} уже существует"

    def __init__(self, _id: int | str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

