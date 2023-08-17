from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializers(data = request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
            data['token'] = token


        else:
            data = serializer.errors

        return Response(data)
    
@api_view(['POST',])
def logut_view(request):

    logout_data = {}
    
    if request.method == 'POST':
        logout_data['user'] = str(request.user)
        request.user.auth_token.delete()
        logout_data['response'] = 'Logout Successful!'
        
        return Response(logout_data, status = status.HTTP_200_OK)