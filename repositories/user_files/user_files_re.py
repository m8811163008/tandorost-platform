


from datetime import datetime
from uuid import uuid4
from fastapi import UploadFile
from data.local_database import DatabaseInterface

from domain_models.data_models import FileMetaData, GallaryTag, UserStaticFiles

class UserFiles:
    def __init__(self, database: DatabaseInterface):
        self.database = database

    
    async def read_user_profile_image(self,  user_id:str) -> FileMetaData | None:
        profile_images = await self.database.read_user_image_gallary(user_id=user_id, tags=[GallaryTag.PROFILE_IMAGE])
        if profile_images is None:
            return None
        return profile_images[GallaryTag.PROFILE_IMAGE][-1]

    async def read_user_image_gallary(self,  user_id:str, tags:list[GallaryTag]) -> dict[GallaryTag, list[FileMetaData]] | None:
        return await self.database.read_user_image_gallary(user_id=user_id, tags=tags)
    
    async def read_user_static_files(self,  user_id:str) -> UserStaticFiles | None:
        return await self.database.read_user_static_files(user_id=user_id)

    async def upsert_user_files(self,  user_files:UserStaticFiles) -> UserStaticFiles:
        return await self.database.upsert_user_files(user_files = user_files)
    
    async def save_files_on_disk(self, image_gallary_files: list[UploadFile],upload_directory:str) -> list[FileMetaData]:
        upload_date_time = datetime.now()
        images_meta_data: list[FileMetaData] = []

        for image_gallary_file in image_gallary_files:
            assert(image_gallary_file.filename is not None)
            assert(image_gallary_file.size is not None)
            assert(image_gallary_file.content_type is not None)
            # Define the file upload path
            file_upload_path = f"{upload_directory}/{upload_date_time.isoformat(timespec="seconds").replace(':', '_')}F{image_gallary_file.filename}"

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
            meta_data = FileMetaData(
                image_id= str(uuid4()),
                file_name=image_gallary_file.filename,
                file_size=image_gallary_file.size,
                upload_date=upload_date_time,
                content_type=image_gallary_file.content_type,
                file_upload_path=file_upload_path,
            )
            images_meta_data.append(meta_data)
        return images_meta_data
    
    async def archive_images(self,user_id:str, images_id : list[str]):
        await self.database.archive_images(user_id=user_id, images_id=images_id)