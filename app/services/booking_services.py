from app.domain.entities.booking import Booking
from typing import List, Optional
from app.domain.repositories.booking_repository import BookingRepository
from app.domain.entities.enums import BookingStatus,PaymentStatus
from app.domain.entities.guests import Guest


class BookingServices:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    async def create_booking(self, primary_guest: Guest, booking_status: BookingStatus, 
                             check_in_date: str, check_out_date: str) -> Booking:
        try:
            booking = Booking(primary_guest=primary_guest, booking_status=booking_status, 
                              check_in=check_in_date, check_out=check_out_date)
            await self.booking_repository.save(booking)
            return booking
        except Exception as e:
            raise e


    async def duration(self, booking_id: str) -> int:
        
        booking = await self.booking_repository.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        
        return (booking.check_out - booking.check_in).days
    

    async def mark_checked_in(self, booking_id: str) -> None:
        booking = await self.booking_repository.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        
        if booking.booking_status != BookingStatus.CONFIRMED:
            raise ValueError("Booking not confirmed")
        
        booking.booking_status = BookingStatus.CHECKED_IN
        await self.booking_repository.update(booking)


    async def mark_checked_out(self, booking_id: str) -> None:
        booking = await self.booking_repository.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        
        if booking.booking_status != BookingStatus.CHECKED_IN:
            raise ValueError("Guest not checked in")
        
        booking.booking_status = BookingStatus.CHECKED_OUT
        await self.booking_repository.update(booking)


    async def get_bookings_by_status(self, status: BookingStatus) -> List[Booking]:
        bookings = await self.booking_repository.get_by_status(status)
        return bookings
    


    async def mark_payment(self, booking_id: str, status: PaymentStatus) -> None:
        booking = await self.booking_repository.get_by_id(booking_id)
        if not booking:
            raise ValueError("Booking not found")
        
        if booking.payment_status == status:
            raise ValueError("Payment status already set to the given status")

        booking.payment_status = status
        await self.booking_repository.update(booking)