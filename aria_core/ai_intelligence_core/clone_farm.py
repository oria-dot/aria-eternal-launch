# clone_farm.py – Overwatch for Monitoring, Assigning, and Scaling Clones

class CloneFarmOverwatch:
    def __init__(self, context):
        self.context = context
        self.clone_registry = {}

    def deploy_clone(self, clone_id):
        from aria_core.ai_intelligence_core.clone_intelligence_core import CloneIntelligenceCore
        role = CloneIntelligenceCore(self.context).assign_clone(clone_id)
        self.clone_registry[clone_id] = role
        self.context.memory.append(f"[Overwatch] Deployed {clone_id} as {role}")
        return role

    def status_report(self):
        return {
            "active_clones": len(self.clone_registry),
            "assignments": self.clone_registry
        }

    def scale_clones(self, count=3):
        for i in range(count):
            clone_id = f"Clone_{len(self.clone_registry)+1}"
            self.deploy_clone(clone_id)
