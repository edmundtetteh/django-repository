from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenge = {
    "january": "This works!",
    "february": "I cant believe it",
    "march": "Great march",
    "april": "Great april",
    "may": "Great may",
    "june": "Great june",
    "july": "Great july",
    "august": "Great august",
    "september": "Great september",
    "october": "Great october",
    "november": "Great november",
    "december": "Great december"
}



# Create your views here



def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challeges_num(request, month):
    months = list(monthly_challenge.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")

    forward_month = months[month-1]
    redirect_path = reverse("month-challenge", arg=[redirect_path])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        response_text = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)
