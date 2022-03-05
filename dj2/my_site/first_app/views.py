from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse


def simple_view(request):
    return render(request, 'first_app/example.html')


# articles = {
#     "sports": "Sports Page",
#     "finance": "Finance Page",
#     "politics": "Politics Page",
# }


# def news_view(request, topic_arg):
#     try:
#         result = articles[topic_arg]
#         return HttpResponse(result)
#     except:
#         # result = 'no page for that topic'
#         # return HttpResponseNotFound(result)
#         raise Http404('generic error')


# def add_view(request, num1, num2):
#     add_result = num1 + num2
#     result = f"{num1}+{num2} = {add_result}"
#     return HttpResponse(str(result))

# # domain/first_app/0 --> domain/first_app/sports


# def num_page_view(request, num_page):

#     topics_list = list(articles.keys())  # make a list from dictionary keys
#     topic = topics_list[num_page]

#     return HttpResponseRedirect(reverse("news_view", args=[topic]))
