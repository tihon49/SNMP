import psutil

import pyagentx3 as pyagentx



"""
Стандартный OID: 1.3.6.1.4.1.2021.13
"""

# Updater class в котором хранятся значения OID.
class Disks(pyagentx.Updater):
    def get_disks_data(self):
        return psutil.disk_partitions()

    def update(self):
        for index, disk in enumerate(self.get_disks_data()):
            counter = 0
            disk_size_data = psutil.disk_usage(disk.mountpoint)

            self.set_OCTETSTRING(f'{index}.{counter}', disk.device)
            self.set_OCTETSTRING(f'{index}.{counter+1}', disk.fstype)
            self.set_OCTETSTRING(f'{index}.{counter+2}', disk.mountpoint)

            self.set_COUNTER64(f'{index}.{counter+3}.{counter}', disk_size_data.total)
            self.set_COUNTER64(f'{index}.{counter+3}.{counter+1}', disk_size_data.used)
            self.set_COUNTER64(f'{index}.{counter+3}.{counter+2}', disk_size_data.free)
            self.set_OCTETSTRING(f'{index}.{counter+3}.{counter+3}', disk_size_data.percent)
            
