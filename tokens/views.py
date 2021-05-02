from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import ConfirmationCode
from .serializers import ConfirmationCodeSerializer
from .tokens import generate_confirmation_code, get_tokens_for_user

User = get_user_model()


@api_view(['POST', ])
@permission_classes([AllowAny])
def send_confirmation_code(request):
    email = request.data.get('email')
    if ConfirmationCode.objects.filter(email=email).exists():
        ConfirmationCode.objects.filter(email=email).delete()
    confirmation_code = generate_confirmation_code(email)
    data = {
        'email': email,
        'confirmation_code': confirmation_code
    }
    serializer = ConfirmationCodeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        mail_subject = 'Your confirmation code'
        send_mail(
            mail_subject,
            confirmation_code,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes([AllowAny])
def issue_jwt_tojen(request):
    email = request.data.get('email')
    confirmation_code = request.data.get('confirmation_code')
    if ConfirmationCode.objects.filter(email=email).exists():
        auth_pair = ConfirmationCode.objects.filter(email=email).first()
        if auth_pair.confirmation_code == confirmation_code:
            if not User.objects.filter(email=email).exists():
                user = User.objects.create(email=email)
            else:
                user = User.objects.filter(email=email).first()
            access_token = get_tokens_for_user(user)
            auth_pair.delete()
            return Response(
                {'access_token': access_token},
                status=status.HTTP_200_OK
            )
        return Response(
            {'confirmation_code': ['Неверный confirmation_code']},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response(
        {'email': ['Для этого email не запрашивался confirmation_code']},
        status=status.HTTP_400_BAD_REQUEST
    )
