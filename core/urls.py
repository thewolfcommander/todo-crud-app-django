from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:id>/update/', views.update, name='update'),
    path('task/<int:id>/delete/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('signin/', LoginView.as_view(template_name='signin.html'), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]