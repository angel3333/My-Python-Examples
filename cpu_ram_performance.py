import psutil


def check_cpu_performance():
    # Get CPU usage percentage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")


def check_ram_performance():
    # Get RAM usage details
    mem = psutil.virtual_memory()
    total_ram = mem.total / (1024 ** 3)  # Convert bytes to GB
    used_ram = mem.used / (1024 ** 3)  # Convert bytes to GB
    ram_percent = mem.percent
    print(f"Total RAM: {total_ram: .2f} GB")
    print(f"Used RAM: {used_ram: .2f} GB")
    print(f"RAM Usage: {ram_percent}%")


if __name__ == "__main__":
    print("Checking CPU Performance:")
    check_cpu_performance()
    print("\nChecking RAM Performance:")
    check_ram_performance()
