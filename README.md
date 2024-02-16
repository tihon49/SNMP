# Настройка SNMP и регистрация своих OID средствами python библиотеки pyagentx3

1. Установить snmp:

   ```bash
   sudo apt-get install snmp
   ```
2. Установка snmpd:

   ```bash
   sudo apt-get install snmpd
   ```
3. Добавить свой OID в файл `/etc/snmp/snmpd.conf`

   ```bash
   view	systemonly	included	.1.3.6.1.4.1.54641
   ```
4. Перезагрузить snmpd.service:

   ```bash
   sudo systemctl restart snmpd.service
   ```
5. Запустить файл snmp_agent.py от root пользователя:

   ```bash
   sudo python3 snmp_agent.py
   ```
6. Проверяем появились ли наши OID'ы

   ```bash
   snmpwalk -v2c -c public localhost 1.3.6.1.4.1.54641
   ```
7. Теперь можно составить MIB для более удобного отображения

   ```bash
   # Создаем файл
   sudo vi /usr/share/snmp/mibs/YOUR-MIB-NAME
   ```

```bash
# заполняем его следующим образом:
YOUR-MIB-NAME DEFINITIONS ::= BEGIN

MYIDENTIFIER OBJECT IDENTIFIER ::= { iso(1) org(3) dod(6) internet(1) private(4) enterprises(1) 54641 }

cpu   OBJECT IDENTIFIER ::= {MYIDENTIFIER 50}
network   OBJECT IDENTIFIER ::= {MYIDENTIFIER 51}
disks   OBJECT IDENTIFIER ::= {MYIDENTIFIER 52}
ram   OBJECT IDENTIFIER ::= {MYIDENTIFIER 53}

-- CPU
CoresCount OBJECT-TYPE
        SYNTAX INTEGER
        ACCESS read-only
        STATUS mandatory
        DESCRIPTION
                 "CPU cores count"
        ::= {cpu 0}

CpuUsagePercent OBJECT-TYPE
        SYNTAX DisplayString
        ACCESS read-only
        STATUS mandatory
        DESCRIPTION
                 "CPU usage in percent"
        ::= {cpu 1}

-- RAM
RamTotal OBJECT-TYPE
        SYNTAX Counter64
        ACCESS read-only
        STATUS mandatory
        DESCRIPTION
                 "Total ram size"
        ::= {ram 0}

RamUsed OBJECT-TYPE
        SYNTAX Counter64
        ACCESS read-only
        STATUS mandatory
        DESCRIPTION
                 "Ram used size"
        ::= {ram 1}


RamFree OBJECT-TYPE
        SYNTAX Counter64
        ACCESS read-only
        STATUS mandatory
        DESCRIPTION
                 "Ram free size"
        ::= {ram 2}


RamAvailable OBJECT-TYPE
        SYNTAX Counter64
        ACCESS read-only
        STATUS mandatory
        DESCRIPTION
                 "Ram available size"
        ::= {ram 3}

RamUsedPercent OBJECT-TYPE
        SYNTAX DisplayString
        ACCESS read-only
        STATUS mandatory
        DESCRIPTION
                 "Ram used in percent"
        ::= {ram 4}

END

```

8. Добавляем запись в файл `/etc/snmp/snmp.conf`

   ```bash
   mibs +YOUR-MIB-NAME
   ```
9. Теперь если мы перезапустим скрипт `snmp_agent.py` и после этого выполним команду `snmpwalk -v2c -c public localhost 1.3.6.1.4.1.54641` то увидим следующую картину:

   ```bash

   YOUR-MIB-NAME::CoresCount = INTEGER: 16
   YOUR-MIB-NAME::CpuUsagePercent = STRING: "3.7"
   YOUR-MIB-NAME::network.0.0 = STRING: "lo"
   YOUR-MIB-NAME::network.0.1 = STRING: "True"
   YOUR-MIB-NAME::network.1.0 = STRING: "eno2"
   YOUR-MIB-NAME::network.1.1 = STRING: "True"
   YOUR-MIB-NAME::network.2.0 = STRING: "wlo1"
   YOUR-MIB-NAME::network.2.1 = STRING: "False"
   YOUR-MIB-NAME::network.3.0 = STRING: "virbr0"
   YOUR-MIB-NAME::network.3.1 = STRING: "True"
   YOUR-MIB-NAME::network.4.0 = STRING: "virbr0-nic"
   YOUR-MIB-NAME::network.4.1 = STRING: "False"
   YOUR-MIB-NAME::network.7.0 = STRING: "docker0"
   YOUR-MIB-NAME::network.7.1 = STRING: "False"
   YOUR-MIB-NAME::network.8.0 = STRING: "vnet0"
   YOUR-MIB-NAME::network.8.1 = STRING: "True"
   YOUR-MIB-NAME::disks.0.0 = STRING: "/dev/nvme0n1p3"
   YOUR-MIB-NAME::disks.0.1 = STRING: "ext4"
   YOUR-MIB-NAME::disks.0.2 = STRING: "/"
   YOUR-MIB-NAME::disks.0.3.0 = Counter64: 48891670528
   YOUR-MIB-NAME::disks.0.3.1 = Counter64: 29871108096
   YOUR-MIB-NAME::disks.0.3.2 = Counter64: 16503771136
   YOUR-MIB-NAME::disks.0.3.3 = STRING: "64.4"
   YOUR-MIB-NAME::disks.1.0 = STRING: "/dev/loop0"
   YOUR-MIB-NAME::disks.1.1 = STRING: "squashfs"
   YOUR-MIB-NAME::disks.1.2 = STRING: "/snap/bare/5"
   YOUR-MIB-NAME::disks.1.3.0 = Counter64: 131072
   YOUR-MIB-NAME::disks.1.3.1 = Counter64: 131072
   YOUR-MIB-NAME::disks.1.3.2 = Counter64: 0
   YOUR-MIB-NAME::disks.1.3.3 = STRING: "100.0"
   YOUR-MIB-NAME::disks.2.0 = STRING: "/dev/loop2"
   YOUR-MIB-NAME::disks.2.1 = STRING: "squashfs"
   YOUR-MIB-NAME::disks.2.2 = STRING: "/snap/code/140"
   YOUR-MIB-NAME::disks.2.3.0 = Counter64: 317849600
   YOUR-MIB-NAME::disks.2.3.1 = Counter64: 317849600
   YOUR-MIB-NAME::disks.2.3.2 = Counter64: 0
   YOUR-MIB-NAME::RamTotal = Counter64: 16463421440
   YOUR-MIB-NAME::RamUsed = Counter64: 9805266944
   YOUR-MIB-NAME::RamFree = Counter64: 305479680
   YOUR-MIB-NAME::RamAvailable = Counter64: 5447172096
   YOUR-MIB-NAME::RamUsedPercent = STRING: "66.9"
   YOUR-MIB-NAME::RamUsedPercent = No more variables left in this MIB View (It is past the end of the MIB tree)
   ```
