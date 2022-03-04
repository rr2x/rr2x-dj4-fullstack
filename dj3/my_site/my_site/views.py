from django.shortcuts import render


def my_custom_server_error_view(request, *args, **argv):
    return render(request, "error_view.html", status=500)
