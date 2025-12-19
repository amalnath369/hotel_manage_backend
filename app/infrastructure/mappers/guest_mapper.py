from app.domain.entities.guests import Guest, BlacklistGuest
from ..models.guests import GuestModel, BlackListGuestModel



# ----------------- Entity -> Model -----------------

def guest_entity_to_model(entity: Guest) -> GuestModel:
    return GuestModel(
        id=entity.id,
        name=entity.name,
        place=entity.place,
        address=entity.address,
        email=entity.email,
        phone=entity.phone,
        id_card=entity.id_card,
        id_card_num=entity.id_card_num,
        id_card_image_path=entity.id_card_image_path,
        guest_photo_path=entity.guest_photo_path,

        is_active=entity.is_active,
        is_deleted=entity.is_deleted,
        created_by=entity.created_by,
        updated_by=entity.updated_by,
        deleted_by=entity.deleted_by,
    )


def blacklist_guest_entity_to_model(entity: BlacklistGuest,) -> BlackListGuestModel:
    return BlackListGuestModel(
        id=entity.id,
        name=entity.name,
        email=entity.email,
        phone=entity.phone,
        reason=entity.reason,

        id_card=entity.id_card,
        id_card_num=entity.id_card_num,
        id_card_image_path=entity.id_card_image_path,
        guest_photo_path=entity.guest_photo_path,

        is_active=entity.is_active,
        is_deleted=entity.is_deleted,
        created_by=entity.created_by,
        updated_by=entity.updated_by,
        deleted_by=entity.deleted_by,
    )


# ----------------- Model -> Entity -----------------


def guest_model_to_entity(model: GuestModel) -> Guest:
    return Guest(
        id=model.id,
        name=model.name,
        place=model.place,
        address=model.address,
        email=model.email,
        phone=model.phone,
        id_card=model.id_card,
        id_card_num=model.id_card_num,
        id_card_image_path=model.id_card_image_path,
        guest_photo_path=model.guest_photo_path,

        is_active=model.is_active,
        is_deleted=model.is_deleted,
        created_by=model.created_by,
        updated_by=model.updated_by,
        deleted_by=model.deleted_by,
    )


def blacklist_guest_model_to_entity(model: BlackListGuestModel,) -> BlacklistGuest:
    return BlacklistGuest(
        id=model.id,
        name=model.name,
        email=model.email,
        phone=model.phone,
        reason=model.reason,

        id_card=model.id_card,
        id_card_num=model.id_card_num,
        id_card_image_path=model.id_card_image_path,
        guest_photo_path=model.guest_photo_path,

        is_active=model.is_active,
        is_deleted=model.is_deleted,
        created_by=model.created_by,
        updated_by=model.updated_by,
        deleted_by=model.deleted_by,
    )



