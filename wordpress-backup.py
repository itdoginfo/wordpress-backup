#!/usr/bin/python

import argparse
import os
import shutil
from subprocess import Popen
from datetime import datetime

def make_directory_and_db_names(database_name):
    current_date = datetime.strftime(datetime.now(),"%Y-%m-%d_%H-%M-%S")
    directory_for_all_backup = "{}-{}".format(database_name, current_date)
    directory_for_html_backup = "{}/html-{}".format(directory_for_all_backup, current_date)
    database_sql_file = "{}-database-{}.sql".format(database_name, current_date)
    return directory_for_all_backup, directory_for_html_backup, database_sql_file

def enter_backup_data():
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', type=str, required=True, help='Database name')
    parser.add_argument('-wp_dir', type=str, required=True, help='Path to wordpress directory')
    parser.add_argument('-bkp_dir', type=str, required=True, help='Path to backup directory')
    args = parser.parse_args()
    return args

def make_backup_database(database_name, database_sql_file):
    print (database_name, database_sql_file)
    args = ['mysqldump', '-u', 'root', database_name]
    with open(database_sql_file, 'wb') as f:
        p = Popen(args, stdout=f) 
        p.wait()
 
def make_backup_directory(wordpress_directory, directory_for_html_backup):
    shutil.copytree(wordpress_directory,directory_for_html_backup)

if __name__ == '__main__':
    args = enter_backup_data()
    directory_for_all_backup, directory_for_html_backup, database_sql_file = make_directory_and_db_names(args.db)
    os.chdir(args.bkp_dir)
    os.mkdir(directory_for_all_backup, 0755)
    make_backup_directory(args.wp_dir, directory_for_html_backup)
    make_backup_database(args.db, database_sql_file)
    shutil.move(database_sql_file, directory_for_all_backup)
    shutil.make_archive(directory_for_all_backup, 'zip', directory_for_all_backup) 
    shutil.rmtree(directory_for_all_backup)
