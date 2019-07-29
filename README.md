# celery-email
send email through celery django

install python3 and setup virtualenv
sudo apt-get install python3
sudo apt install virtualenv
virtualenv -p python3 envname
source envname/bin/activate

To install it on a newer Ubuntu version is very straightforward:
  apt-get install -y erlang
  apt-get install rabbitmq-server
  
Then enable and start the RabbitMQ service:
  systemctl enable rabbitmq-server
  systemctl start rabbitmq-server
  
Check the status to make sure everything is running smooth:
  systemctl status rabbitmq-server
  
Go to project directory celery-email and then 
  pip install -r requirements.txt

To start celery worker:
celery -A celery_email worker -l info

Note: Please change following in settings
      EMAIL_HOST_USER = 'your email'
      EMAIL_HOST_PASSWORD = 'your password'


