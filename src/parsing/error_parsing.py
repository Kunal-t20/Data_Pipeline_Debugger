import re
from datetime import datetime
from typing import Optional
from src.utils.helper import ErrorEvent


VALUE_ERROR_RE = re.compile(r"ValueError[: ]+(.*)")
KEY_ERROR_RE = re.compile(r"KeyError[: ]+(.*)")
CUDA_OOM_RE = re.compile(r"CUDA.*out of memory", re.I)
NAN_LOSS_RE = re.compile(r"nan", re.I)


def _extract_message(pattern, text) -> Optional[str]:
    match = pattern.search(text)
    return match.group(1).strip() if match else None


def parse_error(raw_log: str) -> ErrorEvent:
    """
    Convert raw log text → structured ErrorEvent.
    """

    log_lower = raw_log.lower()
    timestamp = datetime.now().isoformat()

    error_type = "UnknownError"
    stage = "unknown"
    message = raw_log.strip()[:300]   
    confidence = 0.3                  

    if "valueerror" in log_lower:
        error_type = "ValueError"
        stage = "preprocessing"
        extracted = _extract_message(VALUE_ERROR_RE, raw_log)
        if extracted:
            message = extracted
        confidence = 0.85

    elif "keyerror" in log_lower:
        error_type = "KeyError"
        stage = "feature_engineering"
        extracted = _extract_message(KEY_ERROR_RE, raw_log)
        if extracted:
            message = extracted
        confidence = 0.85

    elif CUDA_OOM_RE.search(raw_log):
        error_type = "CUDA_OOM"
        stage = "training"
        message = "CUDA ran out of GPU memory"
        confidence = 0.95

    elif NAN_LOSS_RE.search(raw_log):
        error_type = "NanLoss"
        stage = "training"
        message = "Loss became NaN"
        confidence = 0.8

    else:
        message = message.replace("\n", " ")[:200]

    return ErrorEvent(
        stage=stage,
        error_type=error_type,
        message=message,
        stacktrace=raw_log,
        timestamp=timestamp,
        source="log_parser"
    )
