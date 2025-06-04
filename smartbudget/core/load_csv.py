import csv
from django.contrib.auth import get_user_model
from core.models import Transaction, Category
from django.utils.dateparse import parse_date

def load_transactions_from_csv(csv_path, user_email):
    User = get_user_model()
    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        print(f"User with email {user_email} does not exist.")
        return

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category_name = row["category"].strip()
            category, _ = Category.objects.get_or_create(name=category_name, user=user)
            Transaction.objects.create(
                user=user,
                category=category,
                amount=float(row["amount"]),
                date=parse_date(row["date"]),
                notes=row.get("description", "")
            )
    print("CSV data imported successfully.")