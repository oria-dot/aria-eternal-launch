# clone_mission_router.py – Binds clone roles to mission modules

from freelance_empire_bot import FreelanceEmpireBot
from micro_saas_builder import MicroSaaSBuilder
from gumroad_autopilot import GumroadAutopilot

class CloneMissionRouter:
    def __init__(self):
        self.role_map = {
            "freelancer": self.run_freelance_mission,
            "saas": self.run_saas_mission,
            "gumroad": self.run_gumroad_mission
        }

    def route(self, clone_role):
        if clone_role in self.role_map:
            return self.role_map[clone_role]()
        return f"No mission route found for role: {clone_role}"

    def run_freelance_mission(self):
        bot = FreelanceEmpireBot()
        return bot.run()

    def run_saas_mission(self):
        builder = MicroSaaSBuilder()
        return builder.run()

    def run_gumroad_mission(self):
        uploader = GumroadAutopilot()
        return uploader.run()
