from django.urls import path

from shortener_api.views import UrlList, GenerateUrl, UrlDetailView

urlpatterns = [
    path('create_url/', GenerateUrl.as_view()),
    path('my-links/', UrlList.as_view()),
    path('my-link/<int:pk>/', UrlDetailView.as_view()),
]
