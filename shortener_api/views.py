from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView

from .models import Url
from .serializer import URLSerializer


class UrlList(generics.ListAPIView):
    serializer_class = URLSerializer

    def get_queryset(self):
        user_id = self.request._user.id
        queryset = Url.objects.filter(user=user_id)
        return queryset


class UrlDetailView(generics.RetrieveDestroyAPIView):
    queryset = Url.objects.all()
    serializer_class = URLSerializer


class GenerateUrl(generics.CreateAPIView):
    queryset = Url.objects.all()
    serializer_class = URLSerializer


class RedirectUrl(APIView):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(Url, shortcode=shortcode)
        obj.views += 1
        obj.save()
        return HttpResponseRedirect(obj.url)
