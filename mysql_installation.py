#!/usr/bin/python3
# Script:- Python scripting for MySQL Installation

import requests
import subprocess
import sys
import re


def download_repo():
    print(" Downloading the MySQL repository ")
    download_file=requests.get("https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm")
    if download_file.status_code == requests.codes.OK:
        with open(f"{inst_file}",'wb') as f:
            f.write(download_file.content)
        print("Download Successful\n\n")
    else:
        print("Unable to reach https://dev.mysql.com ..exiting")
        sys.exit(2)

def install_repo():
    print("Installing repository..")
    inst_cmd=f"yum install {inst_file} -y"
    inst_repo=subprocess.run([f"{inst_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    if (inst_repo.returncode == 1) and (re.search(".*does\snot\supdate\sinstalled\spackage.*",inst_repo.stdout.decode()) != None):
        print("\nRepo package already installed with latest")
    elif (inst_repo.returncode == 1) and (re.search(".*does\snot\supdate\sinstalled\spackage.*",inst_repo.stdout.decode()) == None):
        print("\nThere is error installing the repo")
        print("Error information below to Debug issue\n",inst_repo.stdout,"\n",inst_repo.stderr)
        sys.exit(3)
    else:
        print("\nRepo installed on the system")


def install_mysqldb():
    print("Installing MySQl DB")
    db_inst_cmd=f"yum install mysql-community-server -y"
    db_inst=subprocess.run([f"{db_inst_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    if db_inst.returncode != 0:
        print("\nThere is error installing the MySQL DB")
        print("\nError information below to Debug issue\n",db_inst.stderr)
        sys.exit(4)
    else:
        print("\n***MySQL DB Installation successful***")


print(" MySQL Database installation ")
draw="="
inst_file="/tmp/mysql-database-repo.rpm"
print(8*draw,"MENU",8*draw)
print("1) MySQL-5.6 \n2) MySQL-5.7 \n3) MySQL-8.0")
choice=int(input("Choose a MySQL Database version: "))
if choice == 1:
    dis_cmd=f"/bin/yum-config-manager --disable mysql80-community,mysql57-community"
    enb_cmd=f"/bin/yum-config-manager --enable mysql56-community"
    subprocess.run([f"{dis_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    subprocess.run([f"{enb_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    download_repo()
    install_repo()
    install_mysqldb()
elif choice == 2:
    dis_cmd=f"/bin/yum-config-manager --disable mysql80-community,mysql56-community"
    enb_cmd=f"/bin/yum-config-manager --enable mysql57-community"
    subprocess.run([f"{dis_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    subprocess.run([f"{enb_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    download_repo()
    install_repo()
    install_mysqldb()
elif choice == 3:
    dis_cmd=f"/bin/yum-config-manager --disable mysql57-community,mysql56-community"
    end_cmd=f"/bin/yum-config-manager --enable mysql80-community"
    subprocess.run([f"{dis_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    subprocess.run([f"{enb_cmd}"],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    download_repo()
    install_repo()
    install_mysqldb()
else:
    print("Invalid choice")
    sys.exit(1)

