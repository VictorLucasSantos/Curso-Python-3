from django.shortcuts import render


def blogg(request):
    print("blogg")
    return render(request, "blogg/index.html")


def example(request):
    print("example")
    return render(request, "blogg/example.html")
