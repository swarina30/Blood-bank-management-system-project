from django.shortcuts import render
from BBM.models import donorform as dform
from django.http import JsonResponse
from BBM.models import requesterlist as rform

# from django.http import HttpResponse
# Create your views here.

def About(request):
    return render(request, 'about.html')
def frontpage(request):
    return render(request, 'frontpage.html')
def donorform(request):
    print(request.POST)
    fname=request.POST.get('fname')
    age=request.POST.get('age')
    cno=request.POST.get('cno')
    blood_grp=request.POST.get('blood_grp')
    address=request.POST.get('address')
    email=request.POST.get('email')
    dform.objects.create(name=fname, age=age,contact_number=cno,blood_group=blood_grp,address=address,email=email)

    return  render(request, 'donorform.html')

def request(request):
    print(request.POST)
    pname = request.POST.get('pname')
    dname = request.POST.get('dname')
    b_grp = request.POST.get('b_grp')
    p_add = request.POST.get('p_add')
    cname = request.POST.get('cname')
    m_no = request.POST.get('m_no')
    email_id = request.POST.get('email_id')
    rform.objects.create(patient_name=pname, contact_name=cname, doctor_name=dname, patient_address=p_add, blood_group=b_grp, email=email_id, mobile_number=m_no)

    return render(request, 'request.html')

def search(request):
    return render(request, 'search.html')
#def adminform(request):
   # return render(request, 'adminform.html')
   
#def details(request):
   # return render(request, 'details.html')

def get_donors_list(request):
    blood_grp=request.POST.get('blood_grp',None)
    list_of_donors=dform.objects.filter(blood_group=blood_grp).values()
    context= {
        "list_of_donors":list(list_of_donors)
    }
    print(context)
    return JsonResponse(context)

