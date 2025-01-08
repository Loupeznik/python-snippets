import requests
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="Make HTTP requests in a loop until interrupted.")
    parser.add_argument("--url", required=True, help="The HTTP endpoint to call.")
    parser.add_argument("--output", default="status_codes.log", help="Path to the output file. Defaults to 'status_codes.log'.")
    args = parser.parse_args()

    print(f"Starting requests to {args.url}. Press Ctrl+C to stop.")
    
    with open(args.output, "a") as file:
        try:
            while True:
                response = requests.get(args.url)
                status_code = response.status_code

                log = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {status_code}"
                
                print(log)
                file.write(f"{log}\n")
                
                time.sleep(.5)
        except KeyboardInterrupt:
            print("\nStopped by user.")

if __name__ == "__main__":
    main()
