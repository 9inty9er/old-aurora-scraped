import psutil

def get_system_status():
    cpu_temp = psutil.sensors_temperatures().get('coretemp', [])[0].current
    disk_usage = psutil.disk_usage('/').percent
    memory_info = psutil.virtual_memory().percent
    return {
        'cpu_temp': cpu_temp,
        'disk_usage': disk_usage,
        'memory_usage': memory_info
    }

