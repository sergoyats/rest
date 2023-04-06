# from io import BytesIO
from rest_framework import serializers
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer

from .models import Sportsmen


class SportsmenSerializer(serializers.ModelSerializer):
    """
    Сериалайзер, связанный с моделями.
    Обработка данных в БД: чтение, добавление, изменение, удаление.
    """
    # в скрытом поле по умолчанию прописывается текущий пользователь:
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sportsmen
        # возвращаемые клиенту поля модели:
        fields = '__all__'  # ЛИБО конкретно указать = ('title', 'content', 'cat')

# class SportsmenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# def encode():  # кодирование объектов класса SportsmenModel в JSON-строку
#     model = SportsmenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     model_sr = SportsmenSerializer(model)  # объект сериализации
#     print(model_sr.data, type(model_sr.data), sep='\n')  # словарь
#     json = JSONRenderer().render(model_sr.data)  # байтовая JSON-строка
#     print(json)
#
#
# def decode():  # декодирование JSON-строки в объекты класса SportsmenModel
#     # имитация запроса от клиента в виде байтовой JSON-строки:
#     stream = BytesIO(b'{"title":"Fabien Claude",
#                         "content":"Content: Fabien Claude"}')
#     data = JSONParser().parse(stream)
#     serializer = SportsmenSerializer(data=data)  # объект сериализатора
#     serializer.is_valid()
#     print(serializer.validated_data)  # OrderedDict
