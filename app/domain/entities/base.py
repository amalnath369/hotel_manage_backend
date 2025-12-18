from dataclasses import dataclass, field
from datetime import datetime,UTC
from typing import Optional
from uuid import UUID


@dataclass
class BaseEntity:
    id: Optional[int] = None
    created_at: datetime = field(default_factory=lambda :datetime.now(UTC))
    updated_at: datetime = field(default_factory=lambda : datetime.now(UTC))
    is_active: bool = True

    created_by: Optional[UUID] = None
    updated_by: Optional[UUID] = None

    is_deleted: bool = False
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[UUID] = None

    def mark_inactive(self):
        self.is_active = False
        self.updated_at = datetime.now(UTC)

    def make_active(self):
        self.is_active = True
        self.updated_at = datetime.now(UTC)