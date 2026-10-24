from abc import ABC, abstractmethod
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        return "Connected to typical Database"
    def generate(self, database):
        return f"Database name: {database}"
class PostgresConnector(DatabaseConnector):
    def connect(self):
        print(super().connect())
        return "Connected to PostgreSQL database."
        
class BadConnector(DatabaseConnector): # This will CRASH because it forgot to implement 'connect()'
    pass
# db=BadConnector() # Throws TypeError: Can't instantiate abstract class
psg=PostgresConnector()
print(psg.connect())
print(psg.generate("LAPTOP-RBLEO"))