from typing import Optional

from sqlalchemy import Index, Column, Enum
from sqlmodel import Field, JSON

from app.libs.types import Timestamp
from app.models.base_model import BaseModel, TimeStampMixin, PrimaryKeyMixin


class RunStep(BaseModel, PrimaryKeyMixin, TimeStampMixin, table=True):
    __table_args__ = (
        Index("run_step_run_id_idx", "run_id"),
        Index("run_step_run_id_type_idx", "run_id", "type"),
    )

    status: str = Field(
        sa_column=Column(Enum("cancelled", "completed", "expired", "failed", "in_progress"), nullable=False)
    )
    type: str = Field(sa_column=Column(Enum("message_creation", "tool_calls"), nullable=False))
    assistant_id: str = Field(nullable=False)
    thread_id: str = Field(nullable=False)
    run_id: str = Field(nullable=False)
    object: str = Field(nullable=False, default="thread.run.step")
    metadata_: Optional[dict] = Field(default=None, sa_column=Column("metadata", JSON))
    last_error: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    step_details: Optional[dict] = Field(default=None, sa_column=Column(JSON))
    completed_at: Optional[Timestamp] = Field(default=None)
    cancelled_at: Optional[Timestamp] = Field(default=None)
    expires_at: Optional[Timestamp] = Field(default=None)
    failed_at: Optional[Timestamp] = Field(default=None)
    message_id: Optional[str] = Field(default=None)


class RunStepRead(RunStep):
    pass
