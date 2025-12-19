from app.domain.entities.booking_room import BookingRoom
from ..models.booking_room import BookingRoomModel

from booking_mapper import booking_model_to_entity
from .room_mapper import room_model_to_entity


# ----------------- Entity -> Model -----------------


def booking_room_entity_to_model(entity: BookingRoom) -> BookingRoomModel:
    return BookingRoomModel(
        id=entity.id,

        booking_id=entity.booking.id,
        room_id=entity.room.id,

        extra_bed=entity.extra_bed,

        is_active=entity.is_active,
        is_deleted=entity.is_deleted,
        created_by=entity.created_by,
        updated_by=entity.updated_by,
        deleted_by=entity.deleted_by,
    )



# ----------------- Model -> Entity -----------------

def booking_room_model_to_entity(model: BookingRoomModel) -> BookingRoom:
    return BookingRoom(
        id=model.id,

        booking=booking_model_to_entity(model.booking),
        room=room_model_to_entity(model.room),

        extra_bed=model.extra_bed,

        is_active=model.is_active,
        is_deleted=model.is_deleted,
        created_by=model.created_by,
        updated_by=model.updated_by,
        deleted_by=model.deleted_by,
    )
