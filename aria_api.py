from flask import Flask, request, jsonify
from clone_orchestrator import CloneOrchestrator
from clone_memory_store import get_memory
from income_distribution_engine import IncomeDistributor
from aria_kernel import dispatch_all
from auth_utils import require_api_key
from clone_hub import CloneHub

app = Flask(__name__)
orchestrator = CloneOrchestrator()
hub = CloneHub()
income_engine = IncomeDistributor()

@app.route("/api/status", methods=["GET"])
@require_api_key
def api_status():
    return jsonify(orchestrator.status_report())

@app.route("/api/assign", methods=["POST"])
@require_api_key
def api_assign():
    data = request.get_json()
    if not data or "mission" not in data:
        return jsonify({"error": "Missing 'mission' field"}), 400
    result = orchestrator.assign_task(data["mission"])
    return jsonify({"message": result})

@app.route("/api/memory/<clone>", methods=["GET"])
@require_api_key
def api_memory(clone):
    memory = get_memory(clone)
    return jsonify({"memory": memory})

@app.route("/api/dispatch", methods=["POST"])
@require_api_key
def api_dispatch():
    dispatch_all()
    return jsonify({"status": "Dispatch triggered"})

@app.route("/api/income", methods=["GET"])
@require_api_key
def api_income():
    report = income_engine.distribute()
    return jsonify({"income_distribution": report})

@app.route("/api/clones", methods=["GET"])
@require_api_key
def api_clones():
    return jsonify(hub.clones)

if __name__ == "__main__":
    app.run(port=8093)