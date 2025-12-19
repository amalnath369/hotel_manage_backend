from app.domain.entities.rooms import Room
from ..models.rooms import RoomModel
from uuid import UUID


# ----------------- Entity -> Model -----------------

def room_entity_to_model(entity: Room) -> RoomModel:
    return RoomModel(
        id=entity.id,
        room_number=entity.room_number,
        room_type=entity.room_type,
        ac_or_non_ac=entity.ac_or_non_ac,
        floor=entity.floor,
        status=entity.status,

        is_active=entity.is_active,
        is_deleted=entity.is_deleted,
        created_by=entity.created_by,
        updated_by=entity.updated_by,
        deleted_by=entity.deleted_by,
    )


# ----------------- Model -> Entity -----------------


def room_model_to_entity(model: RoomModel) -> Room:
    return Room(
        id=model.id,
        room_number=model.room_number,
        room_type=model.room_type,
        ac_or_non_ac=model.ac_or_non_ac,
        floor=model.floor,
        status=model.status,

        is_active=model.is_active,
        is_deleted=model.is_deleted,
        created_by=model.created_by,
        updated_by=model.updated_by,
        deleted_by=model.deleted_by,
    )
