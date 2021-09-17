FROM python:3.8.5

WORKDIR /code 

COPY requirements.txt .

RUN pip3 install -r requirements.txt
COPY . ./
RUN python manage.py migrate
RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"
CMD python manage.py collectstatic --noinput