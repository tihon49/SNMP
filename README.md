# Настройка SNMP и своих регистрация своих OID средствами python библиотеки pyagentx3

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
   sudo systemctl restart snmpd.sercive
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

AERODISK OBJECT IDENTIFIER ::= { iso(1) org(3) dod(6) internet(1) private(4) enterprises(1) 54641 }

cpu   OBJECT IDENTIFIER ::= {AERODISK 50}
network   OBJECT IDENTIFIER ::= {AERODISK 51}
disks   OBJECT IDENTIFIER ::= {AERODISK 52}
ram   OBJECT IDENTIFIER ::= {AERODISK 53}

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
