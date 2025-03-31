import asyncio
import motor.motor_asyncio
from datetime import datetime



async def manage_mongo():
    
    MONGO_DETAILS = "mongodb://localhost:27017" 
    DATABASE_NAME = "tandorost"
    COLLECTION_NAME = "users"

    try:
        # 1. Establish Connection
        print(f"Attempting to connect to MongoDB at {MONGO_DETAILS}...")
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

        # The ismaster command is cheap and does not require auth.
        await client.admin.command('ismaster')
        print("Successfully connected to MongoDB!")

        # 2. Access Database
        # MongoDB creates the database implicitly if it doesn't exist
        # upon the first write operation or collection creation.
        db = client[DATABASE_NAME]
        print(f"Accessed database: '{DATABASE_NAME}'")

        # 3. Access Collection
        # MongoDB creates the collection implicitly if it doesn't exist
        # upon the first write operation.
        collection = db[COLLECTION_NAME]
        print(f"Accessed collection: '{COLLECTION_NAME}'")

        # 4. Define a Sample Document
        sample_document = {
            "item": "journal",
            "quantity": 25,
            "tags": ["blank", "red"],
            "size": { "h": 14, "w": 21, "uom": "cm" },
            "status": "A",
            "inserted_at": datetime.utcnow() # Add a timestamp
        }
        print(f"\nPrepared sample document: {sample_document}")

        # 5. Insert the Document
        print(f"Inserting document into '{DATABASE_NAME}.{COLLECTION_NAME}'...")
        insert_result = await collection.insert_one(sample_document)

        # 6. Confirmation
        if insert_result.acknowledged:
            print(f"\nDocument inserted successfully!")
            print(f"Inserted document ID: {insert_result.inserted_id}")

            # Optional: Verify insertion by finding the document
            print("\nVerifying insertion...")
            retrieved_doc = await collection.find_one({"_id": insert_result.inserted_id})
            if retrieved_doc:
                print("Successfully retrieved the inserted document:")
                print(retrieved_doc)
            else:
                print("Verification failed: Could not retrieve the inserted document.")
        else:
            print("Document insertion was not acknowledged by the server.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")

    finally:
        # Motor clients are often designed to be long-lived.
        # Explicitly closing might not always be necessary in short scripts,
        # but it's good practice if you know you're done with the client.
        if 'client' in locals() and client:
            # client.close() # Motor manages connections efficiently, closing might not be needed here.
            print("\nMongoDB client connection management handled by Motor.")
        print("Script finished.")


# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(manage_mongo())