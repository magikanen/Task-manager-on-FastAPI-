from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Text, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database import Base

class Task(Base):
   __tablename__ = "Tasks"
   #id = Column(Integer, primary_key=True, index=True)
   task_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
   task_description = Column(Text()) #nullable
   task_param_1 = Column(Text())
   task_param_2 = Column(Integer)

