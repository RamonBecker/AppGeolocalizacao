from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search, get_client_data, buscar_cidade_atual


class IndexView(View):
    def get(self, request, *args, **kwargs):
        items = []
        city = None
        region = None

        busca_resultado = buscar_cidade_atual()
        cidade_atual = busca_resultado['city']
        regiao_atual = busca_resultado['region']
        pais_atual = busca_resultado['country_name']

      #  while not city:
         #   ret = get_client_data()
         #   if ret:
              #  print(ret)
           #     city = ret['city']
        # O q representa o termo que vai ser buscado, por exemplo: pizzaria
        q = request.GET.get('key', None)
        loc = request.GET.get('loc', None)

        #Definimos aqui uma variavel location para não passar como None na busca com a API YELP
       # location = city

        context = {
            'cidade': cidade_atual,
            'regiao': regiao_atual,
            'pais': pais_atual,
            'city': city,
            'busca': False
        }

        #Se o usuário informar uma localidade passamos para uma variavel o dado recebido
        if loc:
            location = loc
        if q:
            items = yelp_search(keyword=q, location=location)
            print(items)
            i = 0

            i = 0
            lista_endereco = dict()
            for item in items.get('businesses'):
                print(item)
                lista_endereco[item.get('id')] = item.get('location').get('display_address')
                i +=1

            context = {
                'cidade': cidade_atual,
                'regiao': regiao_atual,
                'pais': pais_atual,
                'items': items,
                'city': location,
                'listaEndereco': lista_endereco,
                'busca': True
            }
        return render(request, 'index.html', context)