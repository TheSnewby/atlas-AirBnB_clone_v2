import os


if os.getenv('HBNB_MYSQL_STORAGE') == 'db':
    from db_storage import DBStorage
    storage = DBStorage()
else:
    from file_storage import FileStorage
    storage = FileStorage()