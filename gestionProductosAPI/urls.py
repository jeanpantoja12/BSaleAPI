from django.urls import path

from . import views

urlpatterns = [
    
    # URL's de renderizado para las vistas de API's
    path("search_api", views.search_api, name='search_api'),
    path("categories_api",views.categories_api, name='categories_api'),
    path("categories_api/search/<str:cat>/<int:num>",views.categorysearch_api, name='categoriesearch_api')
]