class Foto:

    def __init__(self, titulo, url):

        self.__titulo = titulo
        self.__url = url

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, value):
        self.__titulo = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value