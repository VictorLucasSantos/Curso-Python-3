from django.shortcuts import render


def blogg(request):
    print("blogg")
    context = {"text": "Olá blog", "title": "Essa é uma página de blog "}
    return render(request, "blogg/index.html", context)


def example(request):
    print("example")
    context = {"text": "Olá example", "title": "Essa é uma página de exemplo "}

    return render(request, "blogg/example.html", context)
