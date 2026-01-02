from dataclasses import dataclass

@dataclass
class ErrorEvent:
    stage:str
    error_type:str
    message:str
    stacktrace:str 
    timestamp:str | None=None

    def __str__(self):
        return (
            "\n--- ERROR EVENT ---\n"
            f"Stage      : {self.stage}\n"
            f"Type       : {self.error_type}\n"
            f"Message    : {self.message}\n"
            f"Stacktrace : {self.stacktrace}\n"
            f"Timestamp  : {self.timestamp}\n"
            "---------------------------------\n"
        )