from django.http import HttpResponse
from django.template import loader
from .models import Member
# from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
    # mydata = Member.objects.all().values()
    # mydata = Member.objects.values_list('firstname')
    # mydata = Member.objects.filter(firstname='Emil').values()
    # mydata = Member.objects.filter(firstname='Emil').values()
    # mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
    # mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    # mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    # mydata = Member.objects.filter(firstname__startswith='L').values()
    # mydata = Member.objects.all().order_by('firstname').values()
    # mydata = Member.objects.all().order_by('-firstname').values()
    # mydata = Member.objects.all().order_by('lastname', '-id').values()
    # template = loader.get_template('template.html')
    # context = {
    #     'mymembers': mydata,
    # }
    # return HttpResponse(template.render(context, request))
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))  

   
