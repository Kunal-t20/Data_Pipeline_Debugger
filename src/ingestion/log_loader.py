def load_logs(file_path: str):
    try:
        with open(file_path,"r",encoding="utf-8") as f:
            return f.read()
        
    except FileNotFoundError:
        print("log file not found")

    return " "


