pip install -r requirements.txt
# pip install mongoengine
pip install djongo
pip install pytz
pip install dnspython
pip uninstall pymongo
Y
python3.9 manage.py collectstatic
python3.9 manage.py runserver 


