from django.urls import path
from .views import (
    home, about, login_view, courses_list, generative_ai, data_science,
    web_development, cyber_security, cloud_computing, python_data_analytics,
    create_order, verify_payment
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login_view, name='login'),
    path('courses/', courses_list, name='courses'),
    path('generative_ai/', generative_ai, name='generative_ai'),
    path('data_science/', data_science, name='data_science'),
    path('web_development/', web_development, name='web_development'),
    path('cyber_security/', cyber_security, name='cyber_security'),
    path('cloud_computing/', cloud_computing, name='cloud_computing'),
    path('python_data_analytics/', python_data_analytics, name='python_data_analytics'),
    path('create_order/', create_order, name='create_order'),
    path('verify_payment/', verify_payment, name='verify_payment'),
    path('create_order/', create_order, name='create_order'),
    path('verify_payment/', verify_payment, name='verify_payment'),
]

