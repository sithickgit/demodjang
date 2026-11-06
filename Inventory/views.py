from django.shortcuts import render

# Create your views here.


def HomePage(request):
    data = {
    "name": 'Ben',
    "age": '27',
    "numbers": [1, 2, 3, 4, 5, 6],
    "marks": {
        "tamil": 100,
        "english": 90
    }
}
    return render(request, 'index.html',data)
