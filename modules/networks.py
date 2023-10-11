
import psutil
import pyagentx3 as pyagentx



"""
Базовый OID: 192.168.5.204 1.3.6.1.2.1.31
"""


class Networks(pyagentx.Updater):
    def _get_networks(self):
        addrs = psutil.net_if_stats()
        return addrs

    def update(self):
        network_dict = psutil.net_if_stats()

        for index, interface_name in enumerate(self._get_networks()):
            counter = 0
            self.set_OCTETSTRING(f'{index}.{counter}', interface_name)
            self.set_OCTETSTRING(f'{index}.{counter+1}', str(network_dict.get(interface_name).isup))
        
