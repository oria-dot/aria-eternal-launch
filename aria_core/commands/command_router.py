# command_router.py – Fixed

def handle_command(cmd, context):
    if cmd == "run_council_vote":
        return "Council vote successfully triggered."
    elif cmd == "status":
        return f"System Mode: {context.get('mode', 'Unknown')}"
