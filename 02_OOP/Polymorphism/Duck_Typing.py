class FileLogger:
    def write(self, message):
        print(f"Saving to disk: {message}")
class CloudLogger:
    def write(self, message):
        print(f"Sending to cloud server: {message}")
class MockLogger:
    def write(self,message):
        print(f"Testing environment log: {message}")

def log_system_event(logger_object, event_text):
    logger_object().write(event_text)

log_system_event(FileLogger, "User logged in")
log_system_event(CloudLogger, "Database timeout occured")