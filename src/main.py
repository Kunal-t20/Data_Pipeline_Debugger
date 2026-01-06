from ingestion.log_loader import load_logs
from parsing.error_parsing import parse_error
from classification.classifier import classify_error
from knowledge_base.document import load_all_doc,load_file
from knowledge_base.vector_store import VectorStore


LOG_PATH = r"F:\projects\Data_Pipeline_Debugger\data\sample_log\error1.log"
DOC_PATH = r"F:\projects\Data_Pipeline_Debugger\docs"

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

    try:
        docs=load_all_doc(DOC_PATH)

        if docs:
            vs=VectorStore()
            vs.build(docs)

            print("\n Related Guidance:\n")

            user_query=f"{event.error_type} {event.message}"
            matches=vs.search(user_query,k=2)

            for i,m in enumerate(matches,start=1):
                print(f"match {i} (score={round(m['score'],3)})")
                print(m["text"][:400])
                print()

        else:
            print("No knowledge base document available")

    except Exception as e:
        print(f"Knowledge Base Lookup Error: {e}")

    print("="*25)

if __name__ == "__main__":
    main()
