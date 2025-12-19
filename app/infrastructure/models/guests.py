from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String, Integer, Enum

from . base import BaseModel
from app.domain.entities.enums import IDCard



class GuestModel(BaseModel):
    __tablename__ = 'guests'

    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    place: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    phone: Mapped[int] = mapped_column(Integer, nullable=False)

    id_card: Mapped[IDCard] = mapped_column(Enum(IDCard, name = 'id_card'), nullable=False)
    id_card_num: Mapped[str] = mapped_column(String(50), nullable=False)
    id_card_image_path: Mapped[str] = mapped_column(String(255), nullable=False)

    guest_photo_path: Mapped[str] = mapped_column(String(255), nullable=False)


    bookings = relationship( "BookingModel", back_populates="guest", lazy="selectin")



