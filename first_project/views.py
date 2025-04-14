import os

from django.http import HttpResponse
from django.shortcuts import render
import datetime

from first_project.models import Phone

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}
def Home_page(request):
    return HttpResponse("<pre>hellow, this webpage have url"
                        "\n/current_time/ "
                        "\n/workdir/ "
                        "\n/recipe/ "
                        "\n/create_phone/ "
                        "\n/catalog/ <pre>")

def current_time(request):
    return HttpResponse(f'{datetime.datetime.now().time()}')

def workdir(request):
    files = os.listdir('.')
    return HttpResponse("<br>".join(files))

def recipe(request, str_):
    dish = []
    sum_ = int(request.GET.get('sum_', 1))
    for name, values in DATA[str_].items():
        dishes = f" {name}: {values * sum_} "
        dish.append(dishes)
    return HttpResponse("<br>".join(dish))

def create_phone(request):

    with open('C:/Users/20dim/Desktop/start_Django/first_project/dating.txt', encoding='utf-8' ) as f:
        data = f.read().replace('\n',';').split(';')
        for i in range(0, len(data), 5):
            name,image,price,release_date,lte_exists = data[i:i+5]
            Phone.objects.create(name=name,
                          image=image,
                          price=int(price),
                          release_date=release_date,
                          lte_exists=lte_exists)

    return HttpResponse('ready')
def get_phone(request):
    user_get_phone = request.GET.get('name',)
    if user_get_phone:
        phone_object = Phone.objects.filter(name=user_get_phone)
    else:
        phone_object = Phone.objects.all()
    phones = [
        f'''
        <div style="border: 1px purple; padding: 10px; margin=bottom: 20px;">
            <h2 style= "color: purple; front-size: 24px;">{i.name}</h2>
            <strong> Price:</strong>{i.price} <br>
            <img src="{i.image}" alt="{i.name}" style="max-width:200px;"> <br><br>
            <strong> Release_date:</strong>{i.release_date} <br>
            <strong> LTE:</strong>{'✅' if i.lte_exists else '❌'}
        </div>
        ''' for i in phone_object]
    return HttpResponse("".join(phones))