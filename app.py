from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

# Dashboard Page
@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        cpu=psutil.cpu_percent(interval=1),
        memory=psutil.virtual_memory().percent,
        disk=psutil.disk_usage('/').percent
    )

# Health Check API
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "AI DevOps Agent"
    })

# System Metrics API
@app.route("/metrics")
def metrics():
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    })

# AI Agent API
@app.route("/agent")
def agent():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    recommendations = []

    # CPU Analysis
    if cpu > 80:
        recommendations.append("High CPU Usage - Scale application")
    elif cpu > 60:
        recommendations.append("CPU usage increasing - Monitor workload")
    else:
        recommendations.append("CPU Healthy")

    # Memory Analysis
    if memory > 80:
        recommendations.append("High Memory Usage - Restart services")
    elif memory > 60:
        recommendations.append("Memory usage increasing - Monitor applications")
    else:
        recommendations.append("Memory Healthy")

    # Disk Analysis
    if disk > 80:
        recommendations.append("Disk Space Low - Clean files")
    elif disk > 60:
        recommendations.append("Disk usage increasing - Check storage")
    else:
        recommendations.append("Disk Healthy")

    return jsonify({
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "recommendations": recommendations
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
