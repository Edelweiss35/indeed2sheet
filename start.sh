#!/bin/bash
cd /home/ubuntu/indeed2sheet
/usr/bin/python3.6 manage.py crontab add
/usr/bin/python3.6 manage.py runserver
echo "success in delopyment"
