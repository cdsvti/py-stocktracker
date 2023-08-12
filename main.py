import argparse
import os

def run_script(script_name):
    script_path = os.path.join("src", f"{script_name}.py")
    if os.path.exists(script_path):
        os.system(f"python {script_path}")
    else:
        print(f"Script '{script_name}.py' not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific scripts.")
    parser.add_argument("script", choices=["fiis", "stocks", "fiagro"], help="Specify the script to run: fiis, stocks, or fiagro")

    args = parser.parse_args()
    run_script(args.script)
