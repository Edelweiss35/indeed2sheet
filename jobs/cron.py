from .helper.scraper import scraper_indeed
from rest_framework.response import Response
from rest_framework import status


def my_cron_job():
    url = "https://www.indeed.com/jobs?q=%22Proofreader%22+OR+%22Editor%22&sort=date"
    with scraper_indeed() as scraper:
        return Response(scraper.get_account(url), status=status.HTTP_200_OK)