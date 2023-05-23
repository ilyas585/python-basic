from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Good


class IndexListView(ListView):
    """
    Главная страница
    """
    model = Good
    ordering = '?'
    paginate_by = 3
    template_name = 'online_store/index.html'


class CatalogListView(ListView):
    """
    Каталог товара
    """
    model = Good
    template_name = 'online_store/catalog.html'


class GoodDetailView(DetailView):
    """
    Подробная информация о товаре
    """
    model = Good
    template_name = 'online_store/detail.html'


def sales_view(request):
    """
    Акции
    """
    return render(request, 'online_store/sales.html')


def info_view(request):
    """
    Как заказать
    """
    return render(request, 'online_store/info.html')


def about_view(request):
    """
    О сайте
    """
    return render(request, 'online_store/about.html')
