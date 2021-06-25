from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        request.session['your_name'] = request.POST['your_name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['favorite_language'] = request.POST['favorite_language']
        request.session['comment'] = request.POST['comment']
    return redirect("/result")

def result(request):
        context = {
            'your_name': request.session['your_name'],
            'dojo_location': request.session['dojo_location'],
            'favorite_language': request.session['favorite_language'],
            'comment': request.session['comment'],
        }
        return render(request, "result.html", context)
