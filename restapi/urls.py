from django.urls import include, path
from restapi.views import TransactionViewAPI

urlpatterns = [
   path('', TransactionViewAPI.as_view()),
]