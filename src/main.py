from ingestion.log_loader import load_logs
from parsing.error_parsing import parse_error
from classification.classifier import classify_error


LOG_PATH = r"F:\projects\Data_Pipeline_Debugger\data\sample_log\error1.log"


def main():
    print("\n=== Data Pipeline Debugger ===\n")

    raw_text, ingest_error = load_logs(LOG_PATH)

    if ingest_error:
        print("Ingestion Error Detected:")
        print(ingest_error)
        return

    event = parse_error(raw_text)
    print("Structured Error Event:")
    print(event)

    result = classify_error(event)
    print(f"Category  : {result['category']}")
    print(f"Confidence: {result['confidence']}")
    print(f"Stage     : {result['stage']}")

    print("\n===============================\n")


if __name__ == "__main__":
    main()
