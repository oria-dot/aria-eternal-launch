# aria_boot.py – Unified CLI Entry Point

import argparse
from aria_kernel import dispatch_all, launch_dashboard, launch_telegram

def main():
    parser = argparse.ArgumentParser(description="Launch ARIA System")
    parser.add_argument("--dashboard", action="store_true", help="Launch Flask dashboard")
    parser.add_argument("--telegram", metavar="API_TOKEN", help="Launch Telegram interface")
    parser.add_argument("--dispatch", action="store_true", help="Run income + freelance modules")
    parser.add_argument("--charts", action="store_true", help="Launch analytics chart dashboard")
    parser.add_argument("--dag", action="store_true", help="Run dispatcher using DAG execution mode")

    args = parser.parse_args()

    if args.dag:
        from aria_kernel import run_modules_by_dag
        asyncio.run(run_modules_by_dag())
    elif args.dispatch:
        print(dispatch_all())

    if args.dashboard:
        print("Launching Overwatch Dashboard...")
        launch_dashboard()

    if args.telegram:
        print("Starting Telegram bot...")
        launch_telegram(args.telegram)

    if args.charts:
        import subprocess
        subprocess.Popen(["python", "analytics_dashboard.py"])

if __name__ == "__main__":
    main()