from django.shortcuts import render,redirect
from myApp.models import Employee
from myApp.forms import EmployeeForm
# Create your views here.
def display(request):
    e=Employee.objects.order_by('eno')
    d={'emp':e}
    return render(request,'myApp/index.html',d)
def insert_view(request):
    f=EmployeeForm()
    if request.method=='POST':
        f=EmployeeForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect("/")                
    d={'form':f}
    return render(request,'myApp/insert.html',d)
    
def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect("/") 
    
def update_view(request,id):
    e=Employee.objects.get(id=id)
    if request.method=='POST':
        f=EmployeeForm(request.POST,instance=e)
        if f.is_valid():
            f.save(commit=True)
        return redirect("/")                
    d={'emp':e}
    return render(request,'myApp/update.html',d)
    
			