from rest_framework import serializers

from .models import Url


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('id','user', 'url', 'shortcode', 'description', 'views')
        read_only_fields = ('id', 'views', 'shortcode')
