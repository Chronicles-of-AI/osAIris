from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import DateTime
from sql import Base


class ProjectFlow(Base):
    __tablename__ = "project_flow"
    __table_args__ = {"extend_existing": True}
    pipeline_name = Column(String, primary_key=True)
    pipeline_description = Column(String)
    use_case = Column(String)
    cloud_service_provider = Column(String)
    service_name = Column(String)
    annotation_project_id = Column(Integer)
    annotation_project_name = Column(String)
    annotation_project_description = Column(String)
    raw_annotation_uri = Column(String)
    transform_annotation_uri = Column(String)
    model_id = Column(String)
    functional_stage_id = Column(String)
    current_stage = Column(String)
    created_by = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(String)
