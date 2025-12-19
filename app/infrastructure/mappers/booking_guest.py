from app.domain.entities.booking_guest import BookingGuest
from ..models.booking_guest import BookingGuestModel

from .booking_room_mapper import  booking_room_model_to_entity

from .guest_mapper import guest_model_to_entity


# ----------------- Entity -> Model -----------------

def booking_guest_entity_to_model(entity: BookingGuest) -> BookingGuestModel:
    return BookingGuestModel(
        id=entity.id,

        booking_room_id=entity.booking_room.id,
        guest_id=entity.guest.id,

        is_primary=entity.is_primary,

        is_active=entity.is_active,
        is_deleted=entity.is_deleted,
        created_by=entity.created_by,
        updated_by=entity.updated_by,
        deleted_by=entity.deleted_by,
    )


# ----------------- Model -> Entity -----------------

def booking_guest_model_to_entity(model: BookingGuestModel) -> BookingGuest:
    return BookingGuest(
        id=model.id,

        booking_room=booking_room_model_to_entity(model.booking_room),
        guest=guest_model_to_entity(model.guest),

        is_primary=model.is_primary,

        is_active=model.is_active,
        is_deleted=model.is_deleted,
        created_by=model.created_by,
        updated_by=model.updated_by,
        deleted_by=model.deleted_by,
    )
