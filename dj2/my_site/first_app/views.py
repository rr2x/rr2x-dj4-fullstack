from django.shortcuts import render
from django.http.response import HttpResponse

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page",
}


def news_view(request, topic_arg):
    return HttpResponse(articles[topic_arg])


def add_view(request, num1, num2):
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))
