# wordpress-backup
Backup All content + MariaDB(MySQL) database

## English:
The script makes a full backup of the wordpress directory and MariaDB database. The script allows you to backup any ammount of sites. It is assumed that the wordpress content and the database are on the same server. The backup of the database is perform as root.

Arguments:
* -db - Database name
* -wp_dir - Direcory with Wordpress
* -bkp_dir - Directory for backup

Example, of use in the cron:

```20 0 * * * ./wordpress-backup.py -db itdoginfo -wp_dir /var/www/itdog.info -bkp_dir /mnt/wp-backup/itdog.info/ >> /var/log/wp-backup.log 2>&1```

## Russian:
Скрипт делает полный бэкап указаной директории и базы данных MariaDB. Скрипт позволяет бэкапить какое угодно количество сайтов. Предпологается, что контент и база данных лежат на одном сервере. Бэкап базы делается под root правами.

Аргументы:
* -db - Имя базы данных
* -wp_dir - Каталог, в котором размещен Wordpress
* -bkp_dir - Каталог, в который нужно сохранить бэкап

Пример использования в cron: 

```20 0 * * * ./wordpress-backup.py -db itdoginfo -wp_dir /var/www/itdog.info -bkp_dir /mnt/wp-backup/itdog.info/ >> /var/log/wp-backup.log 2>&1```

