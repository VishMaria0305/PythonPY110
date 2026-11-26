from django.http import JsonResponse
from django.shortcuts import render
from .database import DATABASE


def products_view(request):
    if request.method == "GET":
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False, 'indent': 4})


def shop_view(request):
    if request.method == "GET":
        return render(request, 'store/shop.html')
