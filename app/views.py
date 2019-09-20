from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def my_sum(i: int, i2: int):
    return i + i2+1

@csrf_exempt
def test_method(request):
    if request.method == 'GET':
        return JsonResponse({"data": my_sum(1, 2)}, content_type='application/json')
    else:
        return JsonResponse({"data": my_sum(2, 2)}, content_type='application/json')

