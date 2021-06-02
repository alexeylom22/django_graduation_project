from django.urls import path
from users import views
from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reg', views.register, name='register'),
    path('user/', authViews.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('profile/', views.profile, name='profile'),
    path('links', views.index, name='links_page'),
    path('links/add', views.create),
    path('pass-reset/',
        authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'),
        name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
        authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password_reset_complete/',
        authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    path('password-reset/done/',
        authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
