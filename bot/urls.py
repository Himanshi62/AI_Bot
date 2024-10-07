from django.contrib import admin
from django.urls import path
from .views import HiMessage, CustomerSupportView, QueryView, SendMessageView

urlpatterns = [
    path('', HiMessage.as_view(), name='hi-message'),
    path('support/', CustomerSupportView.as_view(), name='customer-support'),
    path('query/', QueryView.as_view(), name='query'),
    path('send/', SendMessageView.as_view(), name='send'),
]
