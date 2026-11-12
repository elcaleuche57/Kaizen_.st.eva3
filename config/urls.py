from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from catalogo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.PrendaListView.as_view(), name="lista"),
    path("prenda/<int:pk>/", views.PrendaDetailView.as_view(), name="detalle"),
    path("nuevo/", views.PrendaCreateView.as_view(), name="crear"),
    path("prenda/<int:pk>/editar/", views.PrendaUpdateView.as_view(), name="editar"),
    path("prenda/<int:pk>/eliminar/", views.PrendaDeleteView.as_view(), name="eliminar"),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]