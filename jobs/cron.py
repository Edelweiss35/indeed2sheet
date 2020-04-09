from .helper.scraper import scraper_indeed
from rest_framework.response import Response
from rest_framework import status
from .models import Query


def my_cron_job():
    url = ""
    try:
        url = Query.objects.all()[0].query
    except IndexError:
        p = Query(query="https://www.indeed.com/jobs?q=%22Proofreader%22+OR+%22Editor%22&sort=date")
        p.save()

    with scraper_indeed() as scraper:
        return Response(scraper.get_account(url), status=status.HTTP_200_OK)