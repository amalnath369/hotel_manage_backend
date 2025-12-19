from app.domain.entities.users import User
from ..models.users import UserModel
from uuid import UUID

# ----------------- Entity -> Model -----------------
def user_entity_to_model(entity: User) -> UserModel:
    return UserModel(
        id=entity.id,
        name=entity.name,
        email=entity.email,
        password=entity.password,
        phone=entity.phone,
        role=entity.role,  # Use enum member, not string
        is_active=entity.is_active,
        is_deleted=entity.is_deleted,
        created_by=entity.created_by,
        updated_by=entity.updated_by,
        deleted_by=entity.deleted_by,
    )


# ----------------- Model -> Entity -----------------
def user_model_to_entity(model: UserModel) -> User:
    return User(
        id=model.id,
        name=model.name,
        email=model.email,
        password=model.password,
        phone=model.phone,
        role=model.role,  # enum member
        is_active=model.is_active,
        is_deleted=model.is_deleted,
        created_by=model.created_by,
        updated_by=model.updated_by,
        deleted_by=model.deleted_by,
    )
