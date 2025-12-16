from app.domain.entities.booking_guest import BookingGuest
from app.domain.repositories.booking_guest_repository import BookingGuestRepository
from app.domain.repositories.guest_repository import GuestRepository
from app.domain.entities.booking_room import BookingRoom
from app.domain.entities.guests import Guest
from typing import Optional



class BookingGuestService:
    def __init__(self, booking_guest_repo: BookingGuestRepository, guest_repo : GuestRepository):
        self.booking_guest_repository = booking_guest_repo
        self.guest_repo= GuestRepository


    async def create_booking_guest(self, room = BookingRoom, guest = Guest,
                                    primary: Optional[bool] = False ) -> BookingGuest:
        
        try:
            if  guest.is_active:
                id = guest.id
                book = await self.booking_guest_repository.list_by_guest_id(id)
                raise ValueError(f'The Guest is already active in another booking: {book}')
            guest.is_active = True
            await self.guest_repo.update(guest)
            booking_guest = BookingGuest(booking_room=room, guest=guest, primary=primary)
            await self.booking_guest_repository.save(booking_guest)
            return booking_guest
        except Exception as e:
            raise e
