from flask import Flask, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)
LOG_FILE = "analytics_log.csv"

def load_data():
    try:
        return pd.read_csv(LOG_FILE)
    except Exception:
        return pd.DataFrame()

@app.route("/charts/clone-launches")
def clone_launch_chart():
    df = load_data()
    launches = df[df["event_type"] == "clone_launch"]
    count = launches["source"].value_counts()

    plt.figure()
    count.plot(kind="bar", title="Clone Launch Frequency")
    plt.xlabel("Clone")
    plt.ylabel("Launches")

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/charts/module-usage")
def module_usage_chart():
    df = load_data()
    mods = df[df["event_type"] == "module_run"]
    count = mods["source"].value_counts()

    plt.figure()
    count.plot(kind="pie", autopct="%1.1f%%", title="Module Run Distribution")
    plt.ylabel("")

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/charts/income")
def income_chart():
    df = load_data()
    inc = df[df["event_type"] == "income_distribution"]
    inc["amount"] = inc["data"].apply(lambda x: eval(x).get("reinvestment", 0))
    inc["timestamp"] = pd.to_datetime(inc["timestamp"])
    inc = inc.sort_values("timestamp")

    plt.figure()
    plt.plot(inc["timestamp"], inc["amount"].cumsum(), marker='o')
    plt.title("Cumulative Reinvestment Over Time")
    plt.xlabel("Time")
    plt.ylabel("USD")
    plt.grid(True)

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/charts")
def index():
    return """
    <h2>ARIA Analytics Charts</h2>
    <ul>
        <li><a href='/charts/clone-launches'>Clone Launch Chart</a></li>
        <li><a href='/charts/module-usage'>Module Usage Pie</a></li>
        <li><a href='/charts/income'>Income Growth</a></li>
    </ul>
    """

if __name__ == "__main__":
    app.run(port=8090)