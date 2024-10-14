import platform
import psutil

class SystemInfo:
    def __init__(self):
        # Gather basic OS information
        self.os_info = {
            'OS': platform.system(),
            'OS Version': platform.version(),
            'Release': platform.release(),
            'Architecture': platform.architecture(),
            'Machine': platform.machine(),
            'Processor': platform.processor(),
            'Node': platform.node(),
            'Python Version': platform.python_version(),
        }
        
        # Gather CPU and memory information
        self.cpu_memory_info = {
            'CPU Cores (Logical)': psutil.cpu_count(logical=True),
            'CPU Cores (Physical)': psutil.cpu_count(logical=False),
            'CPU Frequency': psutil.cpu_freq().current if psutil.cpu_freq() else 'N/A',
            'Memory (Total)': psutil.virtual_memory().total,
            'Memory (Available)': psutil.virtual_memory().available,
            'Memory (Used)': psutil.virtual_memory().used,
        }
        
        # Gather disk usage information
        self.disk_info = self._get_disk_info()
        
        # Gather network interface information
        self.network_info = self._get_network_info()

    def _get_disk_info(self):
        partitions = psutil.disk_partitions()
        info = {}
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            info[partition.device] = {
                'Mount Point': partition.mountpoint,
                'Total Size': usage.total,
                'Used Space': usage.used,
                'Free Space': usage.free,
            }
        return info

    def _get_network_info(self):
        interfaces = psutil.net_if_addrs()
        info = {}
        for interface, addresses in interfaces.items():
            info[interface] = [{'Address': addr.address, 'Netmask': addr.netmask, 'Broadcast': addr.broadcast}
                               for addr in addresses]
        return info

    def get_os_info(self):
        return self.os_info

    def get_cpu_memory_info(self):
        return self.cpu_memory_info

    def get_disk_info(self):
        return self.disk_info

    def get_network_info(self):
        return self.network_info

    def display_info(self):
        print("System Information:")
        for key, value in self.os_info.items():
            print(f'{key}: {value}')
        
        print("\nCPU and Memory Information:")
        for key, value in self.cpu_memory_info.items():
            if isinstance(value, int):
                value = f'{value / (1024 ** 3):.2f} GB' 
            print(f'{key}: {value}')
        
        print("\nDisk Information:")
        for device, details in self.disk_info.items():
            print(f'Device: {device}')
            for key, value in details.items():
                if isinstance(value, int):
                    value = f'{value / (1024 ** 3):.2f} GB'
                print(f'  {key}: {value}')
        
        print("\nNetwork Information:")
        for interface, details in self.network_info.items():
            print(f'\nInterface: {interface}')
            for addr in details:
                print(f'  Address: {addr["Address"]},\n  Netmask: {addr["Netmask"]},\n  Broadcast: {addr["Broadcast"]}')

if __name__ == "__main__":
    system_info = SystemInfo()
    system_info.display_info()
