# from rest_framework import viewsets
# from .models import User, UserProfile
# from .serializers import UserSerializer, UserProfileSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#
# class UserProfileViewSet(viewsets.ModelViewSet):
#     serializer_class = UserProfileSerializer
#     queryset = UserProfile.objects.all()
#


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            first_name = serializer.validated_data.get('first_name')
            last_name = serializer.validated_data.get('last_name')
            password = serializer.validated_data.get('password')
            profile_user = serializer.validated_data.get('profile_user')
            basemap = serializer.validated_data.get('basemap')
            car = serializer.validated_data.get('car')
            message = f'The information about the user is {username}{first_name}{last_name}{password}{profile_user}{basemap}{car}! '
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # @api_view(['GET'])
    def retrieve(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def list(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    # @api_view(['PUT'])
    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['PATCH'])
    def partial_update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['DELETE'])
    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############
class UserProfileViewSet(viewsets.ViewSet):
    serializer_class = UserProfileSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            biography = serializer.validated_data.get('biography')
            position = serializer.validated_data.get('position')
            message = f'The information about the userprofile is:{biography}{position}'
            serializer.save()
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        userprofile = UserProfile.objects.get(pk=pk)
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)

    def list(self, request):
        userprofile = UserProfile.objects.all()
        serializer = UserProfileSerializer(userprofile, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        userprofile = UserProfile.objects.get(pk=pk)
        serializer = UserSerializer(instance=userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        userprofile = UserProfile.objects.get(pk=pk)
        serializer = UserProfileSerializer(instance=userprofile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        userprofile = UserProfile.objects.get(pk=pk)
        userprofile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
