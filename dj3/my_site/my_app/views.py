from django.shortcuts import render

# Create your views here.


def example_view(request):
    return render(request, 'my_app/example.html')


# {%%} = django tag, where we place control flow and loops
# {{}} = django variable
def variable_view(request):

    my_var = {
        "first_name": "Red",
        "last_name": "fUSCHIA",
        "some_list": [1, 2, 3],
        "some_dictionary": {"i_k1": "i_v1", "i_k2": "i_v2", "i_k3": "i_v3"},
        "user_logged_in": True,
    }

    return render(request, 'my_app/variable.html', context=my_var)
