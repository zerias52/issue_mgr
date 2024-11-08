from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.urls import path
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path("changepassword/", PasswordChangeView.as_view(), name="change password"),
    path("resetpassword/", PasswordResetView.as_view(), name="reset password"),
]