from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from products.models import Product, ProductCategory


class ProductTemplateView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(ProductTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop'
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3

    def get_queryset(self):
        result = super(ProductListView, self).get_queryset()
        if len(self.kwargs):
            category = self.kwargs['category_id']
            result = Product.objects.filter(category_id=category)
        return result

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = ProductCategory.objects.all()

        return context
