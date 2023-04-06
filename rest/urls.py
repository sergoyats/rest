"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from rest_framework import routers
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from sportsmen.views import SportsmenAPIList, SportsmenAPIUpdate, SportsmenAPIDestroy  # SportsmenViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    # v1 - первая версия API-запроса
    # маршрут для авторизации на основе сессий и cookies (в верхнем правом углу
    # веб-страницы DRF появится ссылка Log in):
    # api/v1/drf-auth/login/ ─ вход (перенаправляет на accounts/profile/);
    # api/v1/drf-auth/logout/ ─ выход:
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # маршрут для получения списка записей:
    path('api/v1/sportsmen/', SportsmenAPIList.as_view()),
    # маршрут для изменения записи:
    path('api/v1/sportsmen/<int:pk>/', SportsmenAPIUpdate.as_view()),
    # маршрут для получения и удаления записи:
    path('api/v1/sportsmendelete/<int:pk>/', SportsmenAPIDestroy.as_view()),

    # маршруты пакета djoser:
    path('api/v1/auth/', include('djoser.urls')),  # users/ ─ список пользователей
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # авторизации на основе токена

    #     # маршруты пакета simplejwt:
    # path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

'''
# кастомные маршрутизаторы вообще лучше прописывать в отдельном файле routers.py!
class MyCustomRouter(routers.SimpleRouter):
    # список маршрутов:
    routes = [
        routers.Route(url=r'^{prefix}$',  # БЕЗ / в конце URL!
                      mapping={'get': 'list'},
                      name='{basename}-list',
                      detail=False,  # список записей
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,  # конкретная запись по id
                      initkwargs={'suffix': 'Detail'})
    ]


router = MyCustomRouter()  # вместо:  router = routers.SimpleRouter()
# в router генерируется набор urls:
router.register(r'sportsmen', SportsmenViewSet, basename='sportsmen')
# указание basename обязательно, если в sportsmen.views.py в SportsmenViewSet
# не указан queryset (роутер не сможет автоматически подставить имя модели при
# формировании маршрутов)

urlpatterns = [
    path('admin/', admin.site.urls),
    # набор маршрутов urls, которые сгенерировал router для SportsmenViewSet:
    path('api/v1/', include(router.urls)),  # v1 - первая версия API-запроса
    # для списка записей /api/v1/sportsmenlist/  доступны GET и POST
    # для одной записи /api/v1/sportsmenlist/число  доступны GET, PUT, DELETE

#    # для обработки GET-запроса у SportsmenViewSet вызывается метод list():
#    path('api/v1/sportsmenlist/', SportsmenViewSet.as_view({'get': 'list'})),
#    # для обработки PUT-запроса у SportsmenViewSet вызывается метод update():
#    path('api/v1/sportsmenlist/<int:pk>/',  # pk ─ id изменяемой записи
#         SportsmenViewSet.as_view({'put': 'update'})),
]
'''
