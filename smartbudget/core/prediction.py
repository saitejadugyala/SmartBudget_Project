import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
import numpy as np

def predict_next_month_expense(transactions):
    """
    Predicts next month's expense based on past monthly totals.
    :param transactions: Queryset of Transaction model instances
    :return: float (predicted expense)
    """
    if not transactions:
        return 0.0

    # Convert transactions to pandas DataFrame
    data = [{
        'amount': t.amount,
        'date': t.date
    } for t in transactions]

    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    monthly = df.groupby('month').sum().reset_index()

    if len(monthly) < 2:
        return float(df['amount'].sum())  # Not enough data for prediction

    # Convert month period to integer timestamp for regression
    monthly['month_num'] = monthly['month'].apply(lambda x: x.to_timestamp().timestamp())

    X = monthly[['month_num']]
    y = monthly['amount']

    model = LinearRegression()
    model.fit(X, y)

    # Predict for the next month
    next_month = monthly['month'].max().to_timestamp() + pd.DateOffset(months=1)
    next_month_num = np.array([[next_month.timestamp()]])
    prediction = model.predict(next_month_num)

    return round(float(prediction[0]), 2)
def predict_next_month_spending(user):
    """
    Predicts the next month's spending for a user based on their transaction history.
    :param user: User instance
    :return: float (predicted spending)
    """
    from .models import Transaction  # Import here to avoid circular import

    # Get all transactions for the user
    transactions = Transaction.objects.filter(user=user, transaction_type='expense')

    # Predict next month's expense
    predicted_expense = predict_next_month_expense(transactions)
    return predicted_expense    
# This function can be called in views or serializers to get the predicted spending for a user.
# It can also be extended to include more complex prediction logic if needed.