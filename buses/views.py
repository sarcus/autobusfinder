from django.shortcuts import render
from django.http import HttpResponse
from .TimeTablesDownloader.both import show_all
from datetime import date, timedelta
from autobusfinder.settings import TIMETABLES_DIR
from django.shortcuts import render_to_response


def index(request):
    tupla = show_all()
    save_both(*tupla)
    return HttpResponse("Done.")

def working_day(request):
    d = date.today()
    working_day = d + timedelta(days=7-d.weekday() if d.weekday() > 3 else 0)
    tupla = show_all(working_day)
    save_both(*tupla)
    return HttpResponse("Done.")

def saturday(request):
    today = date.today()
    sat = today + timedelta((5 - today.weekday()) % 7)
    tupla = show_all(sat)
    save_both(*tupla)
    return HttpResponse("Done.")

def sunday(request):
    today = date.today()
    sat = today + timedelta((6 - today.weekday()) % 7)
    tupla = show_all(sat)
    save_both(*tupla)
    return HttpResponse("Done.")

def from_warsaw(requests):
    return render_to_response(TIMETABLES_DIR + '/from_warsaw.html')

def to_warsaw(requests):
    return render_to_response(TIMETABLES_DIR + '/to_warsaw.html')

def save_both(both_from, both_to):
    both_from.to_html(TIMETABLES_DIR + '/from_warsaw.html')
    both_to.to_html(TIMETABLES_DIR + '/to_warsaw.html')