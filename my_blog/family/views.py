from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from family.models import Family


def create_family(request, name: str, last_name: str, email: str, birth_date: int):

    template = loader.get_template("template_family.html")
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    family = Family(name=name, last_name=last_name, email=email, birth_date=birth_date)
    family.save()  # save into the DB

    context_dict = {"family": family}
    render = template.render(context_dict)
    return HttpResponse(render)





def family_list(request):
    family_list = Family.objects.all()

    context_dict = {"family_list": family_list}

    return render(
        request=request,
        context=context_dict,
        template_name="family/family_list.html",
    )