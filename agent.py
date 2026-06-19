import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("\n===== AI DevOps Agent Report =====\n")

print(f"CPU Usage    : {cpu}%")
print(f"Memory Usage : {memory}%")
print(f"Disk Usage   : {disk}%")

print("\nRecommendations:\n")

if cpu > 80:
    print("⚠ High CPU Usage")
    print("- Check running processes")
    print("- Scale application instances")
elif cpu > 60:
    print("⚠ CPU usage increasing")
    print("- Monitor workload")
else:
    print("✅ CPU healthy")

if memory > 80:
    print("⚠ High Memory Usage")
    print("- Restart memory-intensive services")
elif memory > 60:
    print("⚠ Memory usage increasing")
else:
    print("✅ Memory healthy")

if disk > 80:
    print("⚠ Disk space running low")
    print("- Remove unnecessary files")
else:
    print("✅ Disk healthy")
