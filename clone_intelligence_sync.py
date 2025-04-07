# clone_intelligence_sync.py – Sync clone logs and income to central AI memory

import time
from analytics_tracker import AnalyticsTracker

class CloneIntelligenceSync:
    def __init__(self, context):
        self.context = context
        self.analytics = AnalyticsTracker()

    def sync_clone_data(self, clones):
        self.context["clones"] = []
        self.context["income"] = {}
        for clone in clones.values():
            data = clone.get_status()
            self.context["clones"].append(data)
            self.context["income"][clone.id] = data["income"]

    def generate_analytics(self):
        return self.analytics.run(active_clones=self.context["clones"])

    def run(self, clones):
        self.sync_clone_data(clones)
        return self.generate_analytics()
