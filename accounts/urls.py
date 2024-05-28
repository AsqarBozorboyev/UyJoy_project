from django.urls import path
from .views import user_login, user_logout, dashboard_view, SignuUpView, user_register, edit_user, EditUserView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, \
 PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

urlpatterns = [
    # path('login/', user_login, name='login')
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
    path('logout/', user_logout, name='logout'),
    path('profile/', dashboard_view, name='user_profile'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', user_register, name='user_register'),
    # path('signup/', SignuUpView.as_view(), name='user_register'),
    # path('profile/edit/', edit_user, name='edit_user_information'),
    path('profile/edit/', EditUserView.as_view(), name='edit_user_information'),


]