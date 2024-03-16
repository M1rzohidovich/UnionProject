from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Articles, Announcements, MainNews, OwnersOfGreatHearts, Privileges, YoungReception, Report, Partners
from .serializers import AnnouncementSerializer, ArticleSerializer, MainNewsSerializer, OwnersOfGreateHeartSerializer, \
    YoungReceptionSerializer,  PrivilegesSerializer, ReportSerializer, PartnersSerializer


class GetAnnouncement(APIView):
    def get(self, request, id=None):
        if id:
            ann = Announcements.objects.get(id=id)
            serializer = AnnouncementSerializer(ann)
        else:
            ann = Announcements.objects.all()
            serializer = AnnouncementSerializer(ann, many=True)
        return Response(serializer.data)


class GetArticle(APIView):
    def get(self, request, id=None):
        if id:
            art = Articles.objects.get(id=id)
            serializer = ArticleSerializer(art)
        else:
            art = Articles.objects.all()
            serializer = ArticleSerializer(art, many=True)
        return Response(serializer.data)


class GetMainNews(APIView):

    # def get(self, request):
    #     main = MainNews.objects.all()
    #     serializer = MainNewsSerializer(main, many=True)
    #
    #     return Response(serializer.data)

    def get(self, request, id=None):
        if id:
            data = MainNews.objects.get(id=id)
            serializer = MainNewsSerializer(data)
        else:
            data = MainNews.objects.all()
            serializer = MainNewsSerializer(data, many=True)
        return Response(serializer.data)


class GetOwners(APIView):

    def get(self, request, id=None):
        if id:
            owners = OwnersOfGreatHearts.objects.get(id=id)
            serializer = OwnersOfGreateHeartSerializer(owners)
        else:
            owners = OwnersOfGreatHearts.objects.all()
            serializer = OwnersOfGreateHeartSerializer(owners, many=True)
        return Response(serializer.data)


class GetPrivileges(APIView):

    def get(self, request, id=None):
        if id:
            data2 = Privileges.objects.get(id=id)
            serializer = PrivilegesSerializer(data2)
        else:
            data2 = Privileges.objects.all()
            serializer = PrivilegesSerializer(data2, many=True)
        return Response(serializer.data)


class GetReception(APIView):

    def get(self, request, id=None):
        if id:
            reception = YoungReception.objects.get(id=id)
            serializer = YoungReceptionSerializer(reception)
        else:
            reception = YoungReception.objects.all()
            serializer = YoungReceptionSerializer(reception, many=True)
        return Response(serializer.data)


class GetReport(APIView):

    def get(self, request, id=None):
        if id:
            report = Report.objects.get(id=id)
            serializer = ReportSerializer(report)
        else:
            report = Report.objects.all()
            serializer = ReportSerializer(report, many=True)
        return Response(serializer.data)


class GetPartners(APIView):

    def get(self, request, id=None):
        if id:
            partner = Partners.objects.get(id=id)
            serializer = PartnersSerializer(partner)
        else:
            partner = Partners.objects.all()
            serializer = PartnersSerializer(partner, many=True)
        return  Response(serializer.data)
