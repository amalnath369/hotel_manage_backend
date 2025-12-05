from enum import Enum


#--------------- USER ROLE--------------

class Role(str, Enum):
    STAFF = "STAFF"
    ADMIN = "ADMIN"



#--------------- ROOM DETAILS-------------

class RoomStatus(str, Enum):
    AVAILABLE = 'AVAILABLE'
    OCCUPIED =  'OCCUPIED'
    MAINTENANCE = 'MAINTENANCE'


class RoomType(str, Enum):
    SINGLE = 'SINGLE'
    DOUBLE = 'DOUBLE'
    FAMILY =  'FAMILY'
    EXECUTIVE = 'EXECUTIVE'
    NON_EXECUTIVE = 'NON_EXECUITIVE'


class ACType(str, Enum):
    AC = 'AC'
    NON_AC = 'NON_AC'


#---------------- Booking & Payment Details-------------------

class BookingStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    CHECKED_IN = "CHECKED_IN"
    CHECKED_OUT = "CHECKED_OUT"
    CANCELLED = "CANCELLED"


class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    PARTIAL = "PARTIAL"
    REFUNDED = "REFUNDED"


#---------------------- Id Card------------------------


class IDCard(str, Enum):
    AADHAR_CARD = 'AADHAR_CARD'
    VOTERS_ID  = 'VOTER_ID'
    PASSPORT = 'PASSPORT'
    DRIVING_LICENCE ='DRIVING_LICENCE'