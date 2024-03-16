from rest_framework import serializers
from django.conf import settings
from main.models import Articles, Announcements, MainNews, OwnersOfGreatHearts, YoungReception, Privileges, Report,\
    Partners


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = "__all__"


class MainNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainNews
        fields = "__all__"


class OwnersOfGreateHeartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnersOfGreatHearts
        fields = "__all__"


class PrivilegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privileges
        fields = "__all__"


class YoungReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoungReception
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = "__all__"
