pip install -r requirements.txt
# pip install mongoengine
pip install djongo
pip install pytz
pip install dnspython
pip install pymongo
python3.9 manage.py collectstatic

python3.9  manage.py migrate
# python3.9 manage.py runserver 


