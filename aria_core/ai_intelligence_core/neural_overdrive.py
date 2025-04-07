# neural_overdrive.py – Unleashes full performance mode across all AI modules

class NeuralOverdrive:
    def __init__(self, context):
        self.context = context
        self.enabled = False

    def activate(self):
        self.enabled = True
        self.context.status.append("Neural Overdrive: ACTIVE")
        for mod in getattr(self.context, 'overdrive_ready_modules', []):
            if hasattr(mod, "accelerate"):
                mod.accelerate()

    def status(self):
        return "ACTIVE" if self.enabled else "STANDBY"
