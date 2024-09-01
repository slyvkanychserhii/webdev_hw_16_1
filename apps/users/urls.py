from django.urls import path
from apps.users.views.user_views import (
    UserListGenericView,
    RegisterUserGenericView,
    UserDetailGenericView)


urlpatterns = [
    path('', UserListGenericView.as_view()),
    path('<int:pk>/', UserDetailGenericView.as_view()),
    path('register/', RegisterUserGenericView.as_view()),
]
