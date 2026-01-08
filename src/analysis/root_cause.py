from utils.helper import ErrorEvent
ROOT_CAUSE_MAP={
    "SchemaMismatch": (
        "Input data structure or data type does not match what the model "
        "was trained to expect. This usually happens when a column type "
        "changes or categorical values appear where numeric values are required."
    ),

    "MissingColumn": (
        "A required feature or column is missing from the input data. "
        "This can occur due to preprocessing steps dropping columns or "
        "upstream data sources not providing all required fields."
    ),

    "DataQuality": (
        "Input data contains invalid or unreliable values such as NaNs, "
        "nulls, extreme outliers, or corrupted records. This affects model "
        "behavior even if the pipeline does not crash."
    ),

    "ShapeMismatch": (
        "The shape or dimensionality of the input data does not match the "
        "model’s expected input format. This often happens due to incorrect "
        "reshaping, batching, or feature engineering steps."
    ),

    "ResourceLimit": (
        "The pipeline ran out of system resources such as memory or compute. "
        "This typically occurs during large batch processing, model training, "
        "or inference on limited hardware."
    ),

    "TrainingInstability": (
        "Model training became unstable, often due to exploding gradients, "
        "invalid input values, or an excessively high learning rate."
    ),

    "ConvergenceFailure": (
        "The model failed to converge to a stable solution. This can be caused "
        "by poor hyperparameter choices, incorrect feature scaling, or an "
        "inappropriate optimizer."
    ),

    "InferenceFailure": (
        "The model failed during inference due to unexpected inputs, "
        "serialization issues, timeouts, or runtime constraints."
    ),

    "Unknown": (
        "There is not enough information available to confidently determine "
        "the root cause of this error."
    ),
}

def analyze_root_cause(event:ErrorEvent,category:str)->str:
    
    return ROOT_CAUSE_MAP.get(category,"The root cause could not be determined with the available information")