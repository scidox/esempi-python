import shutil
du=shutil.disk_usage("/")
print(du)
du.free/du.total*100
import psutil
psutil.cpu_percent(0.1)

