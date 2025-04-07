# clone_command_engine.py – Core Clone Warfare Controller

import time

class Clone:
    def __init__(self, role, id=None):
        self.id = id or f"{role}_{int(time.time())}"
        self.role = role
        self.status = "Idle"
        self.missions = []
        self.launch_time = None
        self.total_income = 0.0

    def assign_mission(self, mission):
        self.status = "Active"
        self.launch_time = time.time()
        self.missions.append(mission)
        return f"[{self.id}] Mission assigned: {mission}"

    def complete_mission(self, income_generated=0.0):
        self.status = "Idle"
        duration = round(time.time() - self.launch_time, 2)
        self.total_income += income_generated
        return f"[{self.id}] Mission complete in {duration}s | Income: ${income_generated:.2f}"

    def get_status(self):
        return {
            "id": self.id,
            "role": self.role,
            "status": self.status,
            "missions": self.missions,
            "income": self.total_income
        }

class CloneCommandEngine:
    def __init__(self):
        self.clones = {}

    def deploy_clone(self, role):
        new_clone = Clone(role)
        self.clones[new_clone.id] = new_clone
        return f"Clone Deployed: {new_clone.id} ({role})"

    def assign_to_clone(self, clone_id, mission):
        if clone_id in self.clones:
            return self.clones[clone_id].assign_mission(mission)
        return f"Clone {clone_id} not found."

    def complete_clone_mission(self, clone_id, income=0.0):
        if clone_id in self.clones:
            return self.clones[clone_id].complete_mission(income)
        return f"Clone {clone_id} not found."

    def retire_clone(self, clone_id):
        if clone_id in self.clones:
            del self.clones[clone_id]
            return f"Clone {clone_id} retired."
        return f"Clone {clone_id} not found."

    def get_all_status(self):
        return {cid: clone.get_status() for cid, clone in self.clones.items()}
