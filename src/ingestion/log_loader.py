import logging
from pathlib import Path
from typing import Optional, Tuple
from src.utils.helper import ErrorEvent


logger = logging.getLogger(__name__)


def load_logs(file_path: str) -> Tuple[Optional[str], Optional[ErrorEvent]]:

    path = Path(file_path)

    if not path.exists():
        event = ErrorEvent(
            stage="ingestion",
            error_type="FILE_NOT_FOUND",
            message=f"Log file not found: {file_path}",
            stacktrace=None,
            source="local_file"
        )
        logger.error(event)
        return None, event

    try:
        text = path.read_text(encoding="utf-8")
        return text, None

    except Exception as e:
        event = ErrorEvent(
            stage="ingestion",
            error_type="FILE_READ_ERROR",
            message=str(e),
            stacktrace=None,
            source="local_file"
        )
        logger.exception(event)
        return None, event
