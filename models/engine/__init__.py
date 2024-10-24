import os

storage_type = os.getenv('HBNB_MYSQL_STORAGE')
if  storage_type == 'db':
    from .db_storage import DBStorage
    storage = DBStorage()
else:
    from .file_storage import FileStorage
    storage = FileStorage()
