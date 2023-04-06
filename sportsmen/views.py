from rest_framework import generics  # , mixins
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# from rest_framework.viewsets import GenericViewSet

from .models import Sportsmen  # , Category
from .permissions import IsAdminOrReadOnly  # , IsUserOrReadOnly
from .serializers import SportsmenSerializer


# указанные здесь разрешения и параметр пагинации имеют приоритет над глобальными
# DEFAULT_PERMISSION_CLASSES и PAGE_SIZE в settings.py


class SportsmenAPIListPagination(PageNumberPagination):
    page_size = 3  # по 3 записи на странице
    # добавив параметр  ?page_size=число  в конец URL пользователь может получить
    # желаемое число записей на одной странице:
    page_size_query_param = 'page_size'
    max_page_size = 10  # но не более 10-и записей!


class SportsmenAPIList(generics.ListCreateAPIView):
    """
    Возвращает список записей по GET-запросу.
    Добавляет новую запись по POST-запросу.
    """
    queryset = Sportsmen.objects.all()
    serializer_class = SportsmenSerializer
    # добавить новую запись сможет лишь авторизованный пользователь
    # (без авторизации доступно будет лишь чтение записей):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # подключение кастомной пагинации к списку записей текущего представления:
    pagination_class = SportsmenAPIListPagination


class SportsmenAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    Изменяет ОДНУ запись (т.к. queryset в Django ленивый)
    по PUT- или PATCH-запросу.
    На уровне каждого класса представлений можно указать способ
    аутентификации пользователя (по сессиям или токенам).
    """
    queryset = Sportsmen.objects.all()
    serializer_class = SportsmenSerializer
    # запись просматривать может только авторизованный пользователь:
    permission_classes = (IsAuthenticated,)
    # изменять запись может только её автор:
    # permission_classes = (IsUserOrReadOnly, )
    # доступ ТОЛЬКО по токену:
    # authentication_classes = (TokenAuthentication, )


class SportsmenAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    Возвращает (по GET-запросу). Удаляет (по DELETE-запросу) одну запись.
    """
    queryset = Sportsmen.objects.all()
    serializer_class = SportsmenSerializer
    # удалять записи может только администратор сайта:
    permission_classes = (IsAdminOrReadOnly,)


'''
class SportsmenViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):
    # queryset = Sportsmen.objects.all()
    serializer_class = SportsmenSerializer

    # переопределение метода get_queryset для определённого отбора записей:
    def get_queryset(self):  # возвращает список первых трёх записей из БД
        pk = self.kwargs.get('pk')  # kwargs ─ локальный атрибут self
        if not pk:
            return Sportsmen.objects.all()[:3]
        return Sportsmen.objects.filter(pk=pk)  # список из одной записи

    # @action позволяет прописать новый маршрут в SportsmenViewSet
    @action(methods=['get'], detail=True)  # detail=False вернёт СПИСОК категорий
    def category(self, request, pk=None): # category будет именем нового маршрута
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})  # байтовая JSON-строка
'''
