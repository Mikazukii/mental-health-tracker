from django.shortcuts import render


def show_main(request):
    context = {"npm": "2406394881", "name": "Baziz Naïm", "class": "PBP E"}

    return render(request, "main.html", context)
