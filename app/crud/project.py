from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDProject(CRUDBase):
    ...


project_crud = CRUDProject(CharityProject)
