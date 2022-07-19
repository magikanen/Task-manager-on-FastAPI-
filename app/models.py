from sqlalchemy.schema import Column
from sqlalchemy.types import Text, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base

class Task(Base):
   __tablename__ = "Tasks"
   task_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
   task_description = Column(Text())
   task_params = Column(JSON)

