from flask import Flask, jsonify, render_template
from flask_cors import CORS  # ✅ Import CORS
import psutil
import socket
import datetime
import pytz

app = Flask(__name__)
CORS(app)  # ✅ Apply CORS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_system_data():
    # Get hostname
    hostname = socket.gethostname()

    # Get CPU temperature (might not work on all systems)
    try:
        if hasattr(psutil, 'sensors_temperatures'):
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                cpu_temp = f"{temps['coretemp'][0].current}°C"
            else:
                cpu_temp = "N/A"
        else:
            cpu_temp = "N/A"
    except (AttributeError, KeyError):
        cpu_temp = "N/A"
    
    # Get CPU utilization
    cpu_utilization = f"{psutil.cpu_percent(interval=1)}%"

    # Get memory utilization
    memory = psutil.virtual_memory()
    memory_utilization = f"{memory.percent}%"

    # Get current time with timezone
    current_time_utc = datetime.datetime.now(pytz.utc)
    current_time_local = current_time_utc.astimezone(datetime.datetime.now().astimezone().tzinfo)
    current_time = current_time_local.strftime("%Y-%m-%d %I:%M:%S %p %Z")

    data = {
        'hostname': hostname,
        'cpu_temp': cpu_temp,
        'cpu_utilization': cpu_utilization,
        'memory_utilization': memory_utilization,
        'current_time': current_time
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
