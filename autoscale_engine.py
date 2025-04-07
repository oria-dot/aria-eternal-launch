# autoscale_engine.py – Autonomous Clone Scaling Engine

import time

class AutoScaleEngine:
    def __init__(self, controller):
        self.controller = controller
        self.last_scale_time = 0
        self.scale_interval = 60  # seconds
        self.max_nodes_per_region = 5
        self.min_income_threshold = 100

    def check_and_scale(self):
        now = time.time()
        if now - self.last_scale_time < self.scale_interval:
            return "Autoscale cooldown active."

        region_load = {r: 0 for r in self.controller.engine.regions}
        income_by_region = {r: 0 for r in self.controller.engine.regions}

        for node in self.controller.engine.nodes.values():
            region_load[node.region] += 1
            income_by_region[node.region] += node.total_income

        actions = []
        for region, load in region_load.items():
            income = income_by_region[region]
            if income >= self.min_income_threshold and load < self.max_nodes_per_region:
                actions.append(f"Scaling {region} – deploying additional clone...")
                self.controller.engine.deploy_node("freelancer", region=region)

        self.last_scale_time = now
        return actions or ["No scaling action needed."]
