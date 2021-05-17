from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from core import models
from core.generics import BasicRetrieveUpdateDestroyAPIView
from core.permissions import ReadOnly
import core.serializers
# Create your views here.


class userView(BasicRetrieveUpdateDestroyAPIView):
    """
        通过id获取userInfo
    """
    serializer_class = core.serializers.UserSerializer
    permission_classes = [IsAuthenticated | ReadOnly]
    model = models.User
    queryset = model.objects.all()
