from rest_framework import serializers
from .models import *


class CinemaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TvShow
        fields = '__all__'
