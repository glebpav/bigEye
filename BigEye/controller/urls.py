from django.urls import path

from .views import *

app_name = "controller"


urlpatterns = [
    path('employee/', EmployeeView.as_view()),
    path('dataCollection/', DataCollectionView.as_view()),
    path('employee/<int:pk>', EmployeeView.as_view()),
]

