from dataclasses import dataclass
from .base import BaseEntity
from .rooms import Room
from .booking import Booking



@dataclass(kw_only=True)
class BookingRoom(BaseEntity):
    booking: Booking
    room: Room              
    room_price: float
    extra_bed: bool = False



if __name__ == '__main__':
    from .rooms import *
    from .booking import *
    from .guests import *
    from  .booking_guest import *
    from .enums import *

    from datetime import datetime

    # Guests
    rahul = Guest(
        name="Rahul",
        place="Delhi",
        address="Some address",
        email="rahul@mail.com",
        phone=1234567890,
        id_card=IDCard.AADHAR_CARD,
        id_card_num="123456789012",
        id_card_image_path="path/to/id.jpg"
    )

    rahulBrother = Guest(
        name="Rahul Brother",
        place="Delhi",
        address="Brother address",
        email="brother@mail.com",
        phone=9876543210,
        id_card=IDCard.AADHAR_CARD,
        id_card_num="ABCDE1234F",
        id_card_image_path="path/to/id_brother.jpg"
    )

    rahulFriend = Guest(
        name="Rahul Friend",
        place="Delhi",
        address="Friend address",
        email="friend@mail.com",
        phone=1122334455,
        id_card=IDCard.AADHAR_CARD,
        id_card_num="P1234567",
        id_card_image_path="path/to/id_friend.jpg"
    )

    # Rooms
    room101 = Room(
        room_number="101",
        room_type=RoomType.DOUBLE,
        ac_or_non_ac=ACType.AC,
        floor=1
    )

    room102 = Room(
        room_number="102",
        room_type=RoomType.SINGLE,
        ac_or_non_ac=ACType.NON_AC,
        floor=1
    )


    booking = Booking(
    primary_guest=rahul,
    check_in=datetime(2025, 5, 12),
    check_out=datetime(2025, 5, 14),
    booking_status=BookingStatus.CONFIRMED,
    payment_status=PaymentStatus.PENDING
    
)

    room1 = BookingRoom(booking=booking, room=room101, room_price=2000)
    # room2 = BookingRoom(booking=booking, room=room102, room_price=1800)

    a=BookingGuest(booking_room=room1, guest=rahul, is_primary=True)
    b=BookingGuest(booking_room=room1, guest=rahulBrother)

    print(a.booking_room)
    print(b.guest.name)
    # BookingGuest(booking_room=room2, guest=rahulFriend, is_primary=True)
