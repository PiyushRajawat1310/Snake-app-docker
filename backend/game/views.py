from django.shortcuts import render

# Create your views here.

def snake_view(request):
    return render(request, 'snake.html')

