from django.contrib import admin
from django.urls import path
from shop import views
from users import views as viewsusers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', views.products_list_view),
    path('api/v1/products/<int:id>', views.products_detail_view),
    path('api/v1/products/reviews/', views.products_reviews_view),
    path('api/v1/products/tags/', views.products_tags_view),

    path('api/v1/login/', viewsusers.login),
    path('api/v1/register/', viewsusers.register)

]
