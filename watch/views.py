from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'index.html',{})

def test(request):
    return render(request, 'time.html',{})