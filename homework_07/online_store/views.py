from django.shortcuts import render
from .models import Good


def index_view(request):
    """
    Каталог товара
    """
    # goods = Good.objects.all()
    goods = [Good(name="nice"), Good(name="Omez"), Good(name="Katrogel")]
    return render(request, 'online_store/index.html', {'goods': goods})


def about_view(request):
    """
    О сайте
    """
    return render(request, 'online_store/about.html')
