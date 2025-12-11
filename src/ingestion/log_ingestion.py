import argparse
import json
from pathlib import Path
from .parsers import parse_line
#from src.ingestion.parsers import parse_line


def ingest_file(file_path):
    logs = []
    with open(file_path, "r") as f:
        for line in f:
            parsed = parse_line(line.strip())
            if parsed:
                logs.append(parsed.__dict__)
    return logs


def save_output(logs, output_file="normalized_logs.json"):
    with open(output_file, "w") as f:
        json.dump(logs, f, indent=4)
    print(f"Saved normalized logs to: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Log ingestion module")
    parser.add_argument("--file", type=str, required=True, help="Path to log file")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        raise FileNotFoundError("File does not exist!")

    logs = ingest_file(file_path)
    save_output(logs)


if __name__ == "__main__":
    main()

