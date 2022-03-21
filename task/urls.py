from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('dashboard', postListAndCreate.as_view(), name='dashboard'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
