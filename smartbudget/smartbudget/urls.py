"""
URL configuration for smartbudget project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import (
    CategoryViewSet, TransactionViewSet, BudgetViewSet,
    SpendingPredictionView, ExpensePredictionView,
    RegisterView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenViewBase
from core.serializers import EmailTokenObtainPairSerializer

class EmailTokenObtainPairView(TokenViewBase):
    serializer_class = EmailTokenObtainPairSerializer

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'budgets', BudgetViewSet)

urlpatterns = [
     # Admin routes
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # JWT auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Prediction routes
    path('api/predict/expense/', ExpensePredictionView.as_view(), name='expense-predict'),
    path('api/predict/spending/', SpendingPredictionView.as_view(), name='spending-predict'),

    # Include the email token view
    path('api/token/email/', TokenObtainPairView.as_view(), name='email_token_obtain_pair'),
    path('api/register/', RegisterView.as_view(), name='register'),

    # Custom email token view
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
]


