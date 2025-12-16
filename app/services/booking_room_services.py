from app.domain.entities.booking import Booking
from app.domain.entities.enums import BookingStatus,PaymentStatus,RoomStatus,RoomType,ACType
from app.domain.entities.rooms import Room
from typing import List, Optional
from app.domain.repositories.booking_room_repository import BookingRoomRepository
from app.domain.entities.booking_room import BookingRoom



class BookingRoomServices:

    def __init__(self, booking_room_repository: BookingRoomRepository):
        self.booking_room_repository = booking_room_repository


    async def create_booking_room(self, booking: Booking, room: Room) -> BookingRoom:
        try:
            booking_room = BookingRoom(booking=booking, room=room)
            await self.booking_room_repository.save(booking_room)
            return booking_room
        except Exception as e:
            raise e
        

