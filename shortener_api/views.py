
from rest_framework import generics
from .serializer import URLSerializer
from .models import Url



class UrlList(generics.ListAPIView):
    queryset = Url.objects.all()
    serializer_class = URLSerializer


class UrlDetailView(generics.RetrieveDestroyAPIView):
    queryset = Url.objects.all()
    serializer_class = URLSerializer


class GenerateUrl(generics.CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = URLSerializer


