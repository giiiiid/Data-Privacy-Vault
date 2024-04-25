from db.databaseConnect import sessionLocal


'''Initializing db'''
def get_db():
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()