from rest_framework import serializers

from .models import Player, Team, Coach


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('pk', 'name')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('pk', 'name')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('pk', 'name')
