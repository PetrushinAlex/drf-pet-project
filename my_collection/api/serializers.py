from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from content.models import Game, Movie, Book


class GameSerializer(serializers.ModelSerializer):
  pass


class MovieSerializer(serializers.ModelSerializer):
  pass


class BookSerializer(serializers.ModelSerializer):
  pass
