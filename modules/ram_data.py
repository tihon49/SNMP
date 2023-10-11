import psutil
import pyagentx3 as pyagentx


"""
Стандартный OID: 1.3.6.1.4.1.2021.4
"""

class Ram(pyagentx.Updater):
    def update(self):
        ram_data = psutil.virtual_memory()

        self.set_COUNTER64('0', ram_data.total)
        self.set_COUNTER64('1', ram_data.used)
        self.set_COUNTER64('2', ram_data.free)
        self.set_COUNTER64('3', ram_data.available)
        self.set_OCTETSTRING('4', ram_data.percent)
