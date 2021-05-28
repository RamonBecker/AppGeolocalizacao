from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search, get_client_data


class IndexView(View):
    def get(self, request, *args, **kwargs):
        items = []

        city = None

        while not city:
            ret = get_client_data()
            city = ret['city']
        # O q representa o termo que vai ser buscado, por exemplo: pizzaria
        q = request.GET.get('key', None)
        loc = request.GET.get('loc', None)

        #Definimos aqui uma variavel location para não passar como None na busca com a API YELP
        location = city

        context = {
            'city': city,
            'busca': False
        }

        #Se o usuário informar uma localidade passamos para uma variavel o dado recebido
        if loc:
            location = loc
        if q:
            items = yelp_search(keyword=q, location=location)
            context = {
                'items': items,
                'city': location,
                'busca': True
            }
        return render(request, 'index.html', context)