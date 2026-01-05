from typing import Dict
from classification.rule import rule_based_classification
from utils.helper import ErrorEvent


def classify_error(event: ErrorEvent) -> Dict:


    error_type = event.error_type or ""
    message = event.message or ""

    category = rule_based_classification(
        error_type=error_type,
        message=message
    )

    confidence = 0.5  

    if category != "Unknown":
        confidence = 0.85

    if "Unknown" == category:
        confidence = 0.3

    return {
        "category": category,
        "confidence": confidence,
        "stage": event.stage
    }
