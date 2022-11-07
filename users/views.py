from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel, UserSearchTweetsLocationModel, UserAlgorithmResultsModel
from .TwitterClientAlgo import TwitterClient
from .Tweetinfo import GetTweetLocatin
from django_pandas.io import read_frame
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .algorithms.UserNaiveBayes import UserNaiveBayesClass
from .algorithms.UserSVMAlgorithm import UserSVMClass
from .algorithms.UserDecisionTree import UserDecisionTreeClass

# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})


def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def UserGetTweetsForm(request):
    return render(request,'users/GetTweetForm.html',{})

def GetTweets(request):
    if request.method=='POST':
        hashtag = request.POST.get('tweettag')
        print("Working")
        #api = TwitterClient()
        #limit = 200
        # calling function to get tweets
        # tweets = api.get_tweets(query=tagname, count=200)
        #tweets = api.get_tweets(query=hashtag, count=limit)
        #print(type(tweets))
        obj = GetTweetLocatin()
        dataList,dataframe = obj.getLocations(hashtag)
        dataframe = dataframe.to_html()
        for x in dataList:
            tweetId = x[0]
            username = x[1]
            created_at = x[2]
            user_screen_name = x[3]
            tweettext = x[4]
            tweet_location = x[5]
            user_loc = x[6]
            #print("Date type ",type(created_at))
            if len(tweet_location)!=0:
                #print("Tweet Location ", tweet_location)
                lattitude,longitude,address = obj.getLatitudeLongitude(tweet_location)
                #print(tweet_location,"==",lattitude,address)
                flag = 0
                if user_loc==None:
                    flag = 0
                else:
                    flag = 1
                UserSearchTweetsLocationModel.objects.create(tweetid=tweetId, username=username, userscreenname=user_screen_name,tweettext=tweettext,
                                                             createdat=created_at,address=address,latitude=lattitude,longitude=longitude,userloc=flag)

        return render(request,"users/GetTweetsinfo.html",{'data':dataframe})

def UserViewDataset(request):
    data_list = UserSearchTweetsLocationModel.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(data_list, 20)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users/UserViewDataSet.html',{'users':users})

def UserNaiveBayes(request):
    data_list = UserSearchTweetsLocationModel.objects.all()
    df = read_frame(data_list)
    obj = UserNaiveBayesClass()
    accuracy,mae,mse,rmse,r_squared = obj.getNaiveResults(df)
    algorithmname = "Naive Bayes"
    username = request.session['loginid']
    UserAlgorithmResultsModel.objects.create(username=username,algorithmname=algorithmname,accuracy=accuracy,mae=mae,mse=mse,rmse=rmse,r_squared=r_squared)
    return render(request,'users/NaiveResults.html',{"accuracy":accuracy,"mae":mae,"mse":mse,"rmse":rmse,"r_squared":r_squared})

def UserSVM(request):
    data_list = UserSearchTweetsLocationModel.objects.all()
    df = read_frame(data_list)
    obj = UserSVMClass()
    accuracy, mae, mse, rmse, r_squared = obj.getSVM(df)
    algorithmname = "SVM"
    username = request.session['loginid']
    UserAlgorithmResultsModel.objects.create(username=username, algorithmname=algorithmname, accuracy=accuracy, mae=mae,mse=mse, rmse=rmse, r_squared=r_squared)
    return render(request, 'users/SVMResults.html',{"accuracy": accuracy, "mae": mae, "mse": mse, "rmse": rmse, "r_squared": r_squared})

def UserDecisionTree(request):
    data_list = UserSearchTweetsLocationModel.objects.all()
    df = read_frame(data_list)
    obj = UserDecisionTreeClass()
    accuracy, mae, mse, rmse, r_squared = obj.getDecisionTree(df)
    algorithmname = "Decision Tree"
    username = request.session['loginid']
    UserAlgorithmResultsModel.objects.create(username=username, algorithmname=algorithmname, accuracy=accuracy, mae=mae,
                                             mse=mse, rmse=rmse, r_squared=r_squared)
    return render(request, 'users/DecisionTreeResults.html',
                  {"accuracy": accuracy, "mae": mae, "mse": mse, "rmse": rmse, "r_squared": r_squared})
