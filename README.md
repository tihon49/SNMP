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
   view	wywtemonly	included	.1.3.6.1.4.1.54641
   ```
4. Перезагрузить snmpd.service:

   ```bash
   sudo systemctl restart snmpd.sercive
   ```
5. Запустить файл snmp_agent.py от root пользователя:

   ```bash
   sudo python3 snmp_agent.py
   ```
