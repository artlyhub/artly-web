import os

#1 run testing_scripts.py
testing_script_dir = 'tests/testing_scripts.py'
command = 'echo exec(open("{}").read()) | python manage.py shell'.format(testing_script_dir)
os.system(command)
