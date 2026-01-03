from classification.rule import rule_based_classification
from utils.helper import ErrorEvent

def  classify_error(event:ErrorEvent)-> str:

    category=rule_based_classification(
        error_type=event.error_type,
        message=event.message
    )

    return category
