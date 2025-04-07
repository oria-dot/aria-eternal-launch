from flask import Flask, render_template_string, request, redirect, url_for
from clone_orchestrator import CloneOrchestrator
from clone_memory_store import get_memory
from analytics_dashboard import load_data
from aria_kernel import dispatch_all

app = Flask(__name__)
orchestrator = CloneOrchestrator()

TEMPLATE = """
<!doctype html>
<title>ARIA Console</title>
<h2>ARIA Unified Dashboard</h2>

<ul>
    <li><a href="{{ url_for('index') }}">Control</a></li>
    <li><a href="{{ url_for('charts') }}">Charts</a></li>
    <li><a href="{{ url_for('memory') }}">Memory</a></li>
    <li><a href="{{ url_for('status') }}">Status</a></li>
</ul>

{% if section == 'control' %}
    <h3>Assign Clone Mission</h3>
    <form action="/assign" method="post">
        <input name="mission" size="50">
        <input type="submit" value="Assign">
    </form>
    {% if message %}
        <p><strong>{{ message }}</strong></p>
    {% endif %}
    <hr>
    <a href='/retire'>Retire Inactive Clones</a>

{% elif section == 'charts' %}
    <h3>Analytics Charts</h3>
    <ul>
        <li><a href="/charts/clone-launches" target="_blank">Clone Launch Frequency</a></li>
        <li><a href="/charts/module-usage" target="_blank">Module Usage</a></li>
        <li><a href="/charts/income" target="_blank">Income Over Time</a></li>
    </ul>

{% elif section == 'memory' %}
    <h3>Recent Clone Memory</h3>
    {% for row in memory %}
        <p><strong>{{ row[0] }}</strong>: {{ row[1] }} <em>({{ row[2] }})</em></p>
    {% endfor %}

{% elif section == 'status' %}
    <h3>System Status</h3>
    <pre>{{ status }}</pre>
    <form action="/dispatch" method="post">
        <button type="submit">Run Dispatcher</button>
    </form>
{% endif %}
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(TEMPLATE, section="control", message=None)

@app.route("/assign", methods=["POST"])
def assign():
    mission = request.form.get("mission")
    result = orchestrator.assign_task(mission)
    return render_template_string(TEMPLATE, section="control", message=result)

@app.route("/retire")
def retire():
    retired = orchestrator.retire_inactive_clones()
    return redirect(url_for('status'))

@app.route("/charts")
def charts():
    return render_template_string(TEMPLATE, section="charts")

@app.route("/memory")
def memory():
    recent = get_memory("Aria_Trader")
    return render_template_string(TEMPLATE, section="memory", memory=recent)

@app.route("/status")
def status():
    return render_template_string(TEMPLATE, section="status", status=orchestrator.status_report())

@app.route("/dispatch", methods=["POST"])
def dispatch():
    dispatch_all()
    return redirect(url_for('status'))

# Proxy analytics charts
from analytics_dashboard import clone_launch_chart, module_usage_chart, income_chart
app.add_url_rule('/charts/clone-launches', view_func=clone_launch_chart)
app.add_url_rule('/charts/module-usage', view_func=module_usage_chart)
app.add_url_rule('/charts/income', view_func=income_chart)

if __name__ == "__main__":
    app.run(port=8092)