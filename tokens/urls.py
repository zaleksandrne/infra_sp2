from django.urls import path

from .views import issue_jwt_tojen, send_confirmation_code

urlpatterns = [
    path('email/', send_confirmation_code, name='sendcode'),
    path('token/', issue_jwt_tojen, name='issuetoken'),
]
