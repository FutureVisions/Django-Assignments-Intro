from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":
        context = {
            'your_name': request.POST['your_name'],
            'dojo_location': request.POST['dojo_location'],
            'favorite_language': request.POST['favorite_language'],
            'comment': request.POST['comment'],
        }
        return render(request, "result.html", context)

