import psutil

print("=== CPU ===")
print("CPU usage:", psutil.cpu_percent(interval=1), "%")
print("CPU cores:", psutil.cpu_count())
print("CPU frequency:", psutil.cpu_freq())

print("\n=== MEMORY ===")
memory = psutil.virtual_memory()
print("RAM usage:", memory.percent, "%")
print("RAM available:", memory.available / (1024 ** 3), "GB")

print("\n=== DISK ===")
disk = psutil.disk_usage("/")
print("Disk usage:", disk.percent, "%")
print("Disk free:", disk.free / (1024 ** 3), "GB")

print("\n=== NETWORK ===")
network = psutil.net_io_counters()
print("Data sent:", network.bytes_sent / (1024 ** 2), "MB")
print("Data received:", network.bytes_recv / (1024 ** 2), "MB")

print("\n=== SYSTEM ===")
print("Boot time:", psutil.boot_time())