from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from posts import views as postsview
from categorias import views as categoriasview
from comentarios import views as comentariosview

schema_view = get_schema_view(
   openapi.Info(
      title="Blog - API",
      default_version='v1',
      description="Api do projeto blog",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="erikhenderson.dev@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

route = routers.DefaultRouter()

route.register(r'posts', postsview.PostsViewSet, basename="Posts")
route.register(r'categorias', categoriasview.CategoriasViewSet, basename="Categorias")
route.register(r'comentarios', comentariosview.ComentariosViewSet, basename="Comentarios")


urlpatterns = [
   path('', include(route.urls)),
   path('admin/', admin.site.urls),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]