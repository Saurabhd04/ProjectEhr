from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from personalInfo import views

urlpatterns = [
    path('', views.PersonalInfoList.as_view()),
    path('<int:pk>/', views.PersonalInfoDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)