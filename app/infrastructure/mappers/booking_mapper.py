from app.domain.entities.booking import Booking
from ..models.booking import BookingModel
from .guest_mapper import guest_model_to_entity



# ----------------- Entity -> Model -----------------


def booking_entity_to_model(entity: Booking) -> BookingModel:
    return BookingModel(
        id=entity.id,

        primary_guest_id=entity.primary_guest.id,

        check_in=entity.check_in,
        check_out=entity.check_out,

        booking_status=entity.booking_status,
        payment_status=entity.payment_status,

        is_active=entity.is_active,
        is_deleted=entity.is_deleted,
        created_by=entity.created_by,
        updated_by=entity.updated_by,
        deleted_by=entity.deleted_by,
    )


# ----------------- Model -> Entity -----------------


def booking_model_to_entity(model: BookingModel) -> Booking:
    return Booking(
        id=model.id,

        primary_guest=guest_model_to_entity(model.guest),

        check_in=model.check_in,
        check_out=model.check_out,

        booking_status=model.booking_status,
        payment_status=model.payment_status,

        is_active=model.is_active,
        is_deleted=model.is_deleted,
        created_by=model.created_by,
        updated_by=model.updated_by,
        deleted_by=model.deleted_by,
    )
