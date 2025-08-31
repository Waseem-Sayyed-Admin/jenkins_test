from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket
import psutil

app = FastAPI()

# Allow frontend to access this API (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/system")
def get_system_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    cpu_percent = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()

    return {
        "hostname": hostname,
        "ip": ip_address,
        "cpu": cpu_percent,
        "memory": {
            "total": round(memory.total / (1024 * 1024), 2),  # MB
            "used": round(memory.used / (1024 * 1024), 2)      # MB
        }
    } 
