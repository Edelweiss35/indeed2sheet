from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, JobSerializer
from .models import Job
from .helper.scraper import scraper_indeed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


@api_view(['GET', 'POST', ])
def JobViewSet(request):
    url = "https://www.indeed.com/jobs?q=%22Proofreader%22+OR+%22Editor%22&sort=date"
    with scraper_indeed() as scraper:
        return Response(scraper.get_account(url), status=status.HTTP_200_OK)


@api_view(['GET', 'POST', ])
def GetNewJobs(request):
    today = datetime.now().strftime("%Y-%m-%d")
    print(today)
    queryset = Job.objects.filter(date=today)
    result = JobSerializer(queryset, many=True)
    return Response(result.data, status=status.HTTP_200_OK)