from django.shortcuts import render

# Create your views here.


def index_view(request):
    content = {
        "name": "Saba",
        "last_name": "Shafiee",
        "my_job": "Computer vision engineer",
    }
    return render(request, "website/index.html", context=content)


# index.html line 9
