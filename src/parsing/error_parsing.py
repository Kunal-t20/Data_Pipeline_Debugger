import re #for extarcting error 
from utils.helper import ErrorEvent
from datetime import datetime

def parse_error(raw_log: str)->ErrorEvent:  #for str to helper ErrorEvent objects
    error_type="UnknownError"
    stage="unknown"
    message=raw_log.strip()
    timestamp=datetime.now().isoformat()

    if "ValueError" in raw_log:
        error_type="ValueError"
        stage="preprocessing"

        match=re.search(r"ValueError:(.*)",raw_log)
        if match:
            message=match.group(1).strip()

    elif "KeyError" in raw_log:
        error_type="KeyError"
        stage="feature engineering"

        match=re.search(r"KeyError:(.*)",raw_log)
        if match:
            message=match.group(1).strip()

    
    return ErrorEvent(
        error_type=error_type,
        stage=stage,
        message=message,
        stacktrace=raw_log,
        timestamp=timestamp
    )