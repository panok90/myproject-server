from django.urls import path
from products.views import ProductListView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('<int:category_id>/', ProductListView.as_view(), name='category'),
    path('page/<int:page>/', ProductListView.as_view(), name='page'),
]