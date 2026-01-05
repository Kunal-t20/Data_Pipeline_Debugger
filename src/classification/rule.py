from typing import Tuple


def rule_based_classification(error_type: str, message: str) -> str:

    text = (error_type + " " + message).lower()

    if "out of memory" in text or "cuda" in text:
        return "ResourceLimit"

    if "nan" in text and "loss" in text:
        return "TrainingInstability"

    if "convergence" in text or "did not converge" in text:
        return "ConvergenceFailure"

    if "convert" in text or "dtype" in text or "type" in text:
        return "SchemaMismatch"

    if "keyerror" in text or "missing" in text or "not found" in text:
        return "MissingColumn"

    if "nan" in text or "null" in text or "infinite" in text:
        return "DataQuality"

    if "shape" in text or "dimension" in text or "size mismatch" in text:
        return "ShapeMismatch"

    if "inference" in text or "unseen" in text or "predict" in text:
        return "InferenceFailure"

    return "Unknown"
