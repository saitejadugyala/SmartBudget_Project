from celery import shared_task
from .prediction import predict_next_month_spending
from django.contrib.auth.models import User

@shared_task
def run_predictions_for_all_users():
    for user in User.objects.all():
        result = predict_next_month_spending(user)
        print(f"[{user.username}] Prediction: {result}")


# Create your tests here.
