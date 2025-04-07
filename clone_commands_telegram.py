# clone_commands_telegram.py – Telegram Control for Clone Warfare Ops

from clone_command_engine import CloneCommandEngine
from clone_mission_router import CloneMissionRouter
from clone_income_router import CloneIncomeDistributor

class CloneTelegramInterface:
    def __init__(self, context):
        self.context = context
        self.command_engine = CloneCommandEngine()
        self.router = CloneMissionRouter()
        self.distributor = CloneIncomeDistributor()

    def handle_command(self, text):
        parts = text.strip().split()
        if len(parts) < 2:
            return "Invalid command."

        cmd, *args = parts

        if cmd == "/launch":
            role = args[1] if len(args) > 1 else "freelancer"
            deploy_msg = self.command_engine.deploy_clone(role)
            clone_id = deploy_msg.split(": ")[-1].split()[0]
            mission_result = self.router.route(role)
            self.command_engine.complete_clone_mission(clone_id, income_generated=250)
            self.context["status"].append(f"{clone_id} launched and completed mission.")
            return f"{deploy_msg}\n{mission_result}"

        elif cmd == "/status":
            return str(self.command_engine.get_all_status())

        elif cmd == "/retire":
            clone_id = args[1] if len(args) > 1 else None
            return self.command_engine.retire_clone(clone_id)

        elif cmd == "/profit":
            self.distributor.run(list(self.command_engine.clones.values()))
            return f"Income updated. Distribution complete."

        return "Unknown clone command."
