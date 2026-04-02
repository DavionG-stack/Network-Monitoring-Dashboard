from flask import Flask, render_template, jsonify
import monitor

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/data")
def data():
    return jsonify(monitor.check_devices())

if __name__ == "__main__":
    app.run(debug=True)