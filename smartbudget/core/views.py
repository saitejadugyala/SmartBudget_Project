from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Transaction, Budget
from .prediction import predict_next_month_spending
from .prediction import predict_next_month_expense
from .serializers import CategorySerializer, TransactionSerializer, BudgetSerializer, EmailTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all() # Default queryset for all categories
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all() # Default queryset for all transactions
    
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()  # Default queryset for all budgets
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class SpendingPredictionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        prediction = predict_next_month_spending(user)
        return Response({"predicted_spending": prediction})
class ExpensePredictionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        predicted_expense = predict_next_month_expense(transactions)
        return Response({"predicted_next_month_expense": predicted_expense})
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
