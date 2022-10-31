# NOTE: Модули для работы с HTTP (и не только). https://docs.python.org/3/library/urllib.html#module-urllib
from urllib import parse, request

from typing import Any, Dict


class HttpClient(object):
    """Простой http-клиент."""

    def __init__(self):
        self.__response_data = None
        self.__last_url = None

        request.install_opener(self.__get_opener())

    def send_request(self, url: str, params: Dict[str, Any] | None = None, timeout: int = 30):
        """
        Отправляет http-запрос на указанный ресурс.

        :param url: URL запрашиваемого ресурса
        :param params: набор параметров запроса (если пуст - шлём GET-запрос, в противном случае - POST)
        :param timeout: таймаут в секундах, на который может быть заблокирован вызов метода
        """
        post_data = parse.urlencode(params) if params else None
        response = request.urlopen(url, post_data.encode() if post_data else None, timeout)

        self.__response_data = response.read()
        self.__last_url = response.geturl()

    def get_response_text(self, encoding: str = 'utf-8') -> str:
        """Возвращает текстовое представление тела ответа в указанной кодировке."""
        return self.__response_data.decode(encoding)

    @property
    def last_url(self) -> str:
        """Последний запрошенный в ходе запроса URL (с учётом возможных редиректов)."""
        return self.__last_url

    @staticmethod
    def __get_opener():
        return request.build_opener(
            request.HTTPHandler(),
            request.HTTPSHandler(),
            request.HTTPRedirectHandler(),
            request.HTTPCookieProcessor()
        )


if __name__ == '__main__':
    client = HttpClient()
    client.send_request("https://vk.com")

    print(client.last_url)
    print(client.get_response_text())
