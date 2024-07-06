import psutil

class SystemMonitor:
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        memory_info = psutil.virtual_memory()
        return memory_info.percent

    def get_disk_usage(self):
        disk_info = psutil.disk_usage('/')
        return disk_info.percent

