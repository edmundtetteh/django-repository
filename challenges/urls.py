from django.urls import path
from . import views
urlpatterns= [
    path("", views.index),
    path("<int:month>", views.monthly_challeges_num),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
]
