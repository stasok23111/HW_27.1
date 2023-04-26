import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from avito.models import Category, Ad


def status(response):
    return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, name='dispatch')
class Category_View(View):
    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse([{'id': cat.pk, 'name': cat.name} for cat in categories], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_category = Category.objects.create(name=data.get('name'))
        return JsonResponse([{'id': new_category.pk, 'name': new_category.name}], safe=False)


class CategoryDetailView(DetailView):
    model = Category
    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk, 'name': cat.name})



@method_decorator(csrf_exempt, name='dispatch')
class Ad_View(View):
    def get(self, request):
        ad_list = Ad.objects.all()
        return JsonResponse([{'id': ad.pk,
                              'name': ad.name,
                              'price': ad.price,
                              'author': ad.author,
                              'description': ad.description,
                              'address': ad.address,
                              'is_published': ad.is_published
                              } for ad in ad_list], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(**data)
        return JsonResponse([{'id': new_ad.pk,
                              'name': new_ad.name,
                              'price': new_ad.price,
                              'author': new_ad.author,
                              'description': new_ad.description,
                              'address': new_ad.address,
                              'is_published': new_ad.is_published
                              }], safe=False)


class AdDetailView(DetailView):
    model = Ad
    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({'id': ad.pk,
                              'name': ad.name,
                              'price': ad.price,
                              'author': ad.author,
                              'description': ad.description,
                              'address': ad.address,
                              'is_published': ad.is_published
                              })