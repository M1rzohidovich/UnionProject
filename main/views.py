from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Articles, Announcements, MainNews, OwnersOfGreatHearts, Privileges, YoungReception
from .serializers import AnnouncementSerializer, ArticleSerializer, MainNewsSerializer, OwnersOfGreateHeartSerializer, \
    YoungReceptionSerializer,  PrivilegesSerializer


class GetAnnouncement(APIView):

    def get(self, request):
        ann = Announcements.objects.all()
        serializer = AnnouncementSerializer(ann, many=True)

        return Response(serializer.data)


class GetArticle(APIView):

    def get(self, request):
        art = Articles.objects.all()
        serializer = ArticleSerializer(art, many=True)

        return Response(serializer.data)


class GetMainNews(APIView):

    def get(self, request):
        main = MainNews.objects.all()
        serializer = MainNewsSerializer(main, many=True)

        return Response(serializer.data)


class GetOwners(APIView):

    def get(self, request):
        oogh = OwnersOfGreatHearts.objects.all()
        serializer = OwnersOfGreateHeartSerializer(oogh, many=True)

        return Response(serializer.data)


class GetPrivileges(APIView):

    def get(self, request):
        privileges = Privileges.objects.all()
        serializer = PrivilegesSerializer(privileges, many=True)

        return Response(serializer.data)


class GetReception(APIView):

    def get(self, request):
        reception = YoungReception.objects.all()
        serializer = YoungReceptionSerializer(reception, many=True)

        return Response(serializer.data)




