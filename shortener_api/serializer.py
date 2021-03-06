import urllib.parse

from django.urls import reverse
from rest_framework import serializers

from .models import Url


class URLSerializer(serializers.ModelSerializer):
    shorten_link = serializers.SerializerMethodField()

    class Meta:
        model = Url
        fields = ('id', 'user', 'url', 'shortcode', 'description', 'views', 'shorten_link')
        read_only_fields = ('id', 'views', 'shortcode', 'shorten_link')

    def get_shorten_link(self, obj):
        request = self.context.get('request')
        return urllib.parse.urljoin(
            request.build_absolute_uri('/')[:-1],
            reverse('shortener', args=(obj.shortcode,)))

    def validate(self, data):
        if 'http://' not in data['url'] and 'https://' not in data['url']:
            raise serializers.ValidationError("Not a valid url")
        return data
