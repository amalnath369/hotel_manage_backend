import uuid
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Boolean, func, ForeignKey
from sqlalchemy.orm import  DeclarativeBase, relationship
from sqlalchemy.dialects.postgresql import UUID




class Base(DeclarativeBase):
    pass



class BaseModel(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),  server_default=func.now())

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    # 🔹 AUDIT FIELDS
    created_by: Mapped[uuid.UUID | None] = mapped_column( UUID(as_uuid=True), ForeignKey("users.id"), nullable=True,index=True)
    updated_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True),ForeignKey("users.id"),nullable=True, index=True ) 
    deleted_by: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True),ForeignKey("users.id"),nullable=True,index=True)


    created_by_user = relationship("UserModel", foreign_keys=[created_by])
    updated_by_user = relationship("UserModel", foreign_keys=[updated_by])
    deleted_by_user = relationship("UserModel", foreign_keys=[deleted_by])