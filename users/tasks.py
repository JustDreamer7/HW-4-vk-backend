import csv
import datetime

from celery import shared_task

from users.models import User


# from application import celery_app

@shared_task
def count_users():
    num_users = len(User.objects.filter(is_active=True))
    with open('users_counter.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([datetime.datetime.now(), num_users])
    return 'Success'

# def count_auth_users(request):


