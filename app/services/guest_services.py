from app.domain.entities.guests import Guest
from app.domain.repositories.guest_repository import GuestRepository,BlacklistGuestRepository
from app.domain.entities.enums import IDCard
from typing import List,Optional


class GuestService:
    def __init__(self, guest_repository: GuestRepository, blacklist_guest_repository: BlacklistGuestRepository):
        self.guest_repository = guest_repository
        self.blacklist_guest_repository = blacklist_guest_repository

    
    async def register_guest(self, name: str, email: str, phone: int, 
                             place: str, address: str, id_card: IDCard, id_card_num: str, 
                             id_card_image_path : str,  guest_photo_path: Optional[str] = None) -> Guest:
        
        try:
            if await self.blacklist_guest_repository.get_by_phone(phone):
                return f'The user with this phone number is blacklisted: {phone}'

            if await self.blacklist_guest_repository.get_by_email(email):
                return f'The user with this email is blacklisted: {email}'
            
            if await self.blacklist_guest_repository.get_by_id_card_num(id_card_num):
                return f'The user with this ID card number is blacklisted: {id_card_num}'
            

            guest = Guest(
                name=name,
                email=email,
                phone=phone,
                place=place,
                id_card=id_card,
                address=address, 
                id_card_num=id_card_num,
                id_card_image_path=id_card_image_path,
                guest_photo_path=guest_photo_path,
                is_active=False)
            
            await self.guest_repository.save(guest)
            return guest
        except Exception as e:
            raise e
            



            


        