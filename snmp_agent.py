"""
Создание юзера с паролем для SNMPv3:
-a <пароль>
-x <подтверждение_пароля>
-X DES <имя_пользователя>

net-snmp-create-v3-user -ro -a 'P@ssw0rd' -x 'P@ssw0rd' -X DES testUserName

v3 example:
snmpwalk -v3 -u testUserName -l authPriv -a MD5 -A "P@ssw0rd" -x DES -X "P@ssw0rd" localhost 1.3.6.1.4.1.54641

v2 example:
snmpwalk -v2c -c vair localhost 1.3.6.1.4.1.54641
"""



import pyagentx3 as pyagentx

from modules.disks import Disks
from modules.networks import Networks
from modules.cpu_data import Cpu
from modules.ram_data import Ram


class MyAgent(pyagentx.Agent):
    def setup(self):
        # Регистрируем Updater class
        self.register('1.3.6.1.4.1.54641.50', Cpu, freq=10)
        self.register('1.3.6.1.4.1.54641.51', Networks, freq=10)
        self.register('1.3.6.1.4.1.54641.52', Disks, freq=10)
        self.register('1.3.6.1.4.1.54641.53', Ram, freq=10)



def main():
    """Запуск агента."""
    pyagentx.setup_logging()
    try:
        agent = MyAgent()
        agent.start()
    except Exception as e:
        print("Unhandled exception:", e)
        agent.stop()
    except KeyboardInterrupt:
        agent.stop()

if __name__ == '__main__':
    main()
