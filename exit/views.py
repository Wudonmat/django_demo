from django.shortcuts import render

# Create your views here.
def exit_home(request):
    return render(request, "exit/exit_home.html")