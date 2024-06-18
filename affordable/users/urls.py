from django.urls import path
from users import views as user_views

app_name = "users"

urlpatterns = [
    path("signin/", user_views.UserSigninView.as_view(), name="signin"),
    path("signup/", user_views.UserSignupView.as_view(), name="signup"),
    path("forgot/", user_views.UserForgotView.as_view(), name="forgot"),
    path("profile/", user_views.UserProfileView.as_view(), name="profile"),
    path("signout/", user_views.UserSignoutView.as_view(), name="signout"),
]
