from src.ingestion.log_loader import load_logs
from src.parsing.error_parsing import parse_error
from src.classification.classifier import classify_error
from src.knowledge_base.document import load_all_doc
from src.knowledge_base.vector_store import VectorStore
from src.analysis.root_cause import analyze_root_cause
from src.suggestion.fix_generator import generate_fix



LOG_PATH = r"F:\projects\Data_Pipeline_Debugger\data\sample_log\error1.log"
DOC_PATH = r"F:\projects\Data_Pipeline_Debugger\docs"


def main():
    print("\n=== Data Pipeline Debugger ===\n")

    # Ingestion
    raw_text, ingest_error = load_logs(LOG_PATH)
    if ingest_error:
        print("Ingestion Error Detected:")
        print(ingest_error)
        return

    # Parsing
    event = parse_error(raw_text)
    print("Structured Error Event:")
    print(event)
    print("-" * 40)

    # Classification
    result = classify_error(event)
    print(f"Category   : {result['category']}")
    print(f"Confidence : {result['confidence']}")
    print(f"Stage      : {result['stage']}")
    print("-" * 40)

    # Root Cause
    root_cause = analyze_root_cause(event, result["category"])
    print("Root Cause:")
    print(root_cause)
    print("-" * 40)
    
    # Knowledge Base Guidance
    try:
        docs = load_all_doc(DOC_PATH)

        if docs:
            vs = VectorStore()
            vs.build(docs)

            print("Related Guidance:")
            print("-" * 40)

            user_query = f"{event.error_type} {event.message}"
            k = min(2, len(docs))
            matches = vs.search(user_query, k=k)

            for i, m in enumerate(matches, start=1):
                if m["score"] > 1e6:
                    continue

                print(f"[Guidance {i}]")
                summary = m["text"].split("Fix")[0]
                print(summary.strip()[:300])
                print("-" * 40)

        else:
            print("No knowledge base documents available.")

    except Exception as e:
        print(f"Knowledge Base Lookup Error: {e}") 

    # Suggested Fixes
    fixes = generate_fix(event, result["category"])
    print("Suggested Fixes:")
    for i, step in enumerate(fixes, start=1):
        print(f"{i}. {step}")
    print("-" * 40)

    print("=== End ===\n")


if __name__ == "__main__":
    main()
