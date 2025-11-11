


from datetime import datetime, timezone
from uuid import uuid4
from fastapi import UploadFile
from data.local_database import DatabaseInterface

from domain_models.data_models import FileData, GallaryTag

class UserFiles:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    
    async def read_user_profile_image(self,  user_id:str) -> list[FileData]:
        return await self.database.read_user_image_gallary(user_id=user_id, tags=[GallaryTag.PROFILE_IMAGE])

    async def read_user_image_gallary(self,  user_id:str, tags:list[GallaryTag]) -> list[FileData]:
        return await self.database.read_user_image_gallary(user_id=user_id, tags=tags)
    
    async def read_users_images_gallary(self,  users_id:list[str], tags:list[GallaryTag]) -> list[FileData]:
        return await self.database.read_users_images_gallary(users_id=users_id, tags=tags)
    
    async def read_user_static_files(self,  user_id:str) -> list[FileData]:
        return await self.database.read_user_static_files(user_id=user_id)

    async def upsert_user_files(self,  user_files : list[FileData]) -> list[FileData]:
        return await self.database.upsert_user_files(user_files = user_files)
    
    async def save_files_on_disk(self,user_id:str, tag:GallaryTag ,image_gallary_files: list[UploadFile],upload_date : datetime | None, upload_directory:str, description : str | None = None) -> list[FileData]:
        upload_date_time = upload_date if upload_date != None else datetime.now(timezone.utc)
        images_meta_data: list[FileData] = []

        for image_gallary_file in image_gallary_files:
            assert(image_gallary_file.filename is not None)
            assert(image_gallary_file.size is not None)
            assert(image_gallary_file.content_type is not None)
            # Define the file upload path
            file_upload_path = f"{upload_directory}{upload_date_time.isoformat(timespec='seconds').replace(':', '_')}F{image_gallary_file.filename}"

            # Ensure the upload directory exists
            import os
            os.makedirs(upload_directory, exist_ok=True)

            # Save the file to the system
            try:
                with open(file_upload_path, "wb") as file:
                    content = await image_gallary_file.read()
                    file.write(content)
            except Exception as e:
                raise e

            # Create metadata for the uploaded file
            meta_data = FileData(
                _id= str(uuid4()),
                user_id=user_id,
                tag=tag,
                file_name=image_gallary_file.filename,
                file_size=image_gallary_file.size,
                upload_date=upload_date_time,
                content_type=image_gallary_file.content_type,
                file_upload_path=file_upload_path,
                description=description
            )
            images_meta_data.append(meta_data)
        return images_meta_data
    
    async def archive_images(self, images_id : list[str]) -> list[str]:
        return await self.database.archive_images( images_id=images_id)