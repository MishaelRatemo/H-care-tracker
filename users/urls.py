from django.urls import path
from django.contrib.auth.decorators import login_required
from users.views import SignupView
from users import views 



urlpatterns = [
    path('signup/',views.signup, name='register'),
    path('login/',views.login, name='login' ),
    # path(
    #     # route='signup/',
         
    #     # view=views.SignupView.as_view(),
    #     # name='signup'
    # ),
    # path(
    #     route='login/',
    #     view=views.LoginView.as_view(),
    #     name='Login'
    # ),
    # path(
    #     route='me/profile/',
    #     view=views.UpdateProfileView.as_view(),
    #     name='update_profile'
    # ),

    # # Posts
    # path(
    #     route='<str:username_slug>/',
    #     view=login_required(views.UserDetailView.as_view()),
    #     name='detail'
    # ),
]