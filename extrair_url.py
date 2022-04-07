import re


class URLExtractor:
    def __init__(self, url: str):
        self._url = self.sanitize(url)
        self.validate()

    def __str__(self):
        return self.url

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

    def __ne__(self, other):
        return self.url != other.url

    def sanitize(self, url):
        if(type(url) == str):
            return url.strip()
        else:
            return ''

    def validate(self):
        url_regex = re.compile(
            '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        url_match = re.match(url_regex, self.url)
        if(not url_match):
            raise ValueError('URL não é válida')

    @property
    def url(self):
        return self._url

    @property
    def url_base(self):
        url_base = self.url[:self.url.find('?')]
        return url_base

    @property
    def url_parameters(self):
        url_query = self.url.find('?') + 1
        url_parameters = self.url[url_query:]
        return url_parameters

    def parameter_value(self, parameter):
        url_parameter_index = self.url_parameters.find(parameter)
        url_parameter_value_index = url_parameter_index + len(parameter) + 1
        url_commercial_e_index = self.url_parameters.find(
            '&', url_parameter_index)

        if(url_commercial_e_index == -1):
            url_parameter_value = self.url_parameters[url_parameter_value_index:]
        else:
            url_parameter_value = self.url_parameters[url_parameter_value_index:url_commercial_e_index]

        return url_parameter_value


url = URLExtractor(
    'https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=100')

url_moeda_origem_value = url.parameter_value('moedaorigem')
url_moeda_destino_value = url.parameter_value('moedadestino')
url_valor_value = float(url.parameter_value('valor'))

print(
    f'moeda origem = {url_moeda_origem_value}\n'
    f'moeda destino = {url_moeda_destino_value}\n'
    f'valor = {url_valor_value}'
)
