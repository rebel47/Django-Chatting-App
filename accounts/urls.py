from django.urls import path
from accounts import views
from .views import UserEditView, UserRegisterView


urlpatterns = [
    path('',views.home, name="home"),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
