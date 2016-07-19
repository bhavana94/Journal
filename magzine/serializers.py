from . models import Publication, Article
from rest_framework import serializers

class PublicationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Publication
	

class ArticleSerializer(serializers.ModelSerializer):

	publications=PublicationSerializer(read_only=True, many=True)
	class Meta:
		model = Article
		

