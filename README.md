# celery-email
send email through celery django

## install python3 and setup virtualenv:
```
sudo apt-get install python3
sudo apt install virtualenv   
virtualenv -p python3 envname
source envname/bin/activate
```

## To install RabbitMQ:
  ```bash
  apt-get install -y erlang
  apt-get install rabbitmq-server
  
  Then enable and start the RabbitMQ service:
  systemctl enable rabbitmq-server
  systemctl start rabbitmq-server
  
  Check the status to make sure everything is running smooth:
  systemctl status rabbitmq-server
  ```
  
## Go to project directory celery-email and then 
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## To start celery worker:
```bash
celery -A celery_email worker -l info
```

## Note: Please change following in settings
```python
EMAIL_HOST_USER = 'your email'
EMAIL_HOST_PASSWORD = 'your password
```

## Usage
```bash
endpoint:   POST  http://127.0.0.1:8000/api/v1/send-email
endpoint_params :     
{
	"email_to" : ["email_to@gmail.com"],
	"email_html" : "<h1>This is my HTML test</h1>"
}
```


