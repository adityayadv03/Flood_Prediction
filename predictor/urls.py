from django.urls import path
from .views import home, predict_risk,predict_advanced_risk,chatbot_view

urlpatterns = [
    path('', home, name='home'),
    path('predict_risk/', predict_risk, name='predict_risk'),
    path('predict_advanced_risk/', predict_advanced_risk, name='predict_advanced_risk'),
    path("chatbot/", chatbot_view, name="chatbot"),
]