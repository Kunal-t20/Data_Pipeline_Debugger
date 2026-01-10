from utils.helper import ErrorEvent
from typing import List

FIX_GENERATOR_MAP={
    "SchemaMismatch": [
        "Validate the input schema against the schema used during training",
        "Convert categorical or string values to the expected numeric format",
        "Add schema validation checks before preprocessing or inference",
    ],

    "MissingColumn": [
        "Check upstream data extraction logic for dropped columns",
        "Restore or backfill missing required features",
        "Add required-column checks before model execution",
    ],

    "DataQuality": [
        "Check for missing, null, or invalid values in the input data",
        "Clean or impute missing values before model execution",
        "Add data validation rules to detect anomalies early",
    ],

    "ShapeMismatch": [
        "Verify input feature dimensions and tensor shapes",
        "Ensure batch size and reshape operations are correct",
        "Add shape assertions in the preprocessing pipeline",
    ],

    "ResourceLimit": [
        "Reduce batch size or input data volume",
        "Use a smaller model or enable memory-efficient settings",
        "Monitor system memory and compute usage during execution",
    ],

    "TrainingInstability": [
        "Reduce the learning rate",
        "Enable gradient clipping to prevent exploding gradients",
        "Normalize input features and verify training labels",
    ],

    "ConvergenceFailure": [
        "Tune learning rate and batch size",
        "Improve feature scaling and normalization",
        "Try a different optimizer or initialization strategy",
    ],

    "InferenceFailure": [
        "Validate input data before inference",
        "Handle unseen or unexpected values gracefully",
        "Add retries or fallback logic for inference failures",
    ],

    "Unknown": [
        "Review logs manually to identify the failure point",
        "Add additional logging to capture more context",
        "Update classification rules if a new error pattern is observed",
    ],

}

def generate_fix(event:ErrorEvent,category:str)->str:
    return FIX_GENERATOR_MAP.get(category,
                                [
                                     "Review logs manually to identify the root cause",
                                    "Verify pipeline configuration and input data"
                                ]
                                    )