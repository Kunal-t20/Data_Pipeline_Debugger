from dataclasses import dataclass
from typing import Optional


@dataclass
class ErrorEvent:
    stage: str                  
    error_type: str             
    message: str                
    stacktrace: Optional[str] = None  
    timestamp: Optional[str] = None
    source: Optional[str] = None   # e.g. 'mlflow_run', 'local_log'

    def __str__(self):
        return (
            "\n--- ERROR EVENT ---\n"
            f"Stage      : {self.stage}\n"
            f"Type       : {self.error_type}\n"
            f"Message    : {self.message}\n"
            f"Stacktrace : {self.stacktrace}\n"
            f"Timestamp  : {self.timestamp}\n"
            f"Source     : {self.source}\n"   
        )
    
