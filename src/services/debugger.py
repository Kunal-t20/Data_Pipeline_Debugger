from src.ingestion.log_loader import load_logs
from src.parsing.error_parsing import parse_error
from src.classification.classifier import classify_error
from src.analysis.root_cause import analyze_root_cause
from src.suggestion.fix_generator import generate_fix



def _run(event) -> dict:
    result = classify_error(event)
    root = analyze_root_cause(event, result["category"])
    fixes = generate_fix(event, result["category"])

    return {
        "category": result["category"],
        "confidence": result["confidence"],
        "stage": result["stage"],
        "root_cause": root,
        "fixes": fixes,
    }


def run_debugger_from_text(log_text: str) -> dict:
    event = parse_error(log_text)
    return _run(event)


def run_debugger_from_file(log_path: str) -> dict:
    raw_text, ingest_error = load_logs(log_path)

    if ingest_error:
        return {"error": str(ingest_error)}

    event = parse_error(raw_text)
    return _run(event)
