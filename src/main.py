from ingestion.log_loader import load_logs
from parsing.error_parsing import parse_error

def main():
    raw=load_logs(r"F:\projects\Data_Pipeline_Debugger\data\sample_log\error1.log")
    
    event=parse_error(raw)
    print("Exact structured error:")
    print(event)


if __name__=="__main__":
    main()