import psutil
import pyagentx3 as pyagentx



class Cpu(pyagentx.Updater):
    def _get_cpu_usage(self):
       cpu_usage_percent = round(psutil.cpu_percent(), 2) 
       return str(cpu_usage_percent)

    def update(self):
        self.set_INTEGER('0', psutil.cpu_count())
        self.set_OCTETSTRING('1', self._get_cpu_usage())
