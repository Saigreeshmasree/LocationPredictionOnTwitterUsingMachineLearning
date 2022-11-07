from django.shortcuts import render
from django.contrib import messages
from users.models import UserRegistrationModel,UserAlgorithmResultsModel

# Create your views here.

def AdminLoginCheck(request):
    if request.method == 'POST':
        usrid = request.POST.get('loginid')
        pswd = request.POST.get('pswd')
        print("User ID is = ", usrid)
        if usrid == 'admin' and pswd == 'admin':
            return render(request, 'admins/AdminHome.html')
        elif usrid == 'Admin' and pswd == 'Admin':
            return render(request, 'admins/AdminHome.html')
        else:
            messages.success(request, 'Please Check Your Login Details')
    return render(request, 'AdminLogin.html', {})


def AdminHome(request):
    return render(request, 'admins/AdminHome.html')


def ViewRegisteredUsers(request):
    data = UserRegistrationModel.objects.all()
    return render(request, 'admins/RegisteredUsers.html', {'data': data})


def AdminActivaUsers(request):
    if request.method == 'GET':
        id = request.GET.get('uid')
        status = 'activated'
        print("PID = ", id, status)
        UserRegistrationModel.objects.filter(id=id).update(status=status)
        data = UserRegistrationModel.objects.all()
        return render(request, 'admins/RegisteredUsers.html', {'data': data})

def AdminNaiveBayes(request):
    data = UserAlgorithmResultsModel.objects.filter(algorithmname="Naive Bayes")
    return render(request,'admins/AdminNaiveBayes.html',{'data':data})

def AdminSVM(request):
    data = UserAlgorithmResultsModel.objects.filter(algorithmname="SVM")
    return render(request,'admins/AdminSVM.html',{'data':data})

def AdminDecisionTree(request):
    data = UserAlgorithmResultsModel.objects.filter(algorithmname="Decision Tree")
    return render(request, 'admins/AdminDecisionTree.html', {'data': data})