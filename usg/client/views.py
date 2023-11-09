from django.shortcuts import render
import pyrebase

# Create your views here.
config = {
    'apiKey': "AIzaSyA0vBvWec1huC34E048rzWtUwkKd5bfAxU",
    'authDomain': "usg-django-pplprak.firebaseapp.com",
    'databaseURL': "https://usg-django-pplprak-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "usg-django-pplprak",
    'storageBucket': "usg-django-pplprak.appspot.com",
    'messagingSenderId': "1048754184838",
    'appId': "1:1048754184838:web:16794aa3970c3b8dd2a707",
    'measurementId': "G-PC679TGGMD"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()


def signin(request):
    return render(request, 'signin.html')


def postsignin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password('email', 'password')
    except:
        message = "Invalid Email or Password"
        return render(request, 'signin.html', {'email': email})
    session_id = user['idToken']
    session_id['uid'] = str(session_id)
    message = 'Login Success'
    return render(request, '', {'message': message})


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, 'signin.html')


def postsignup(request):
    email = request.POST.get('email')
    passs = request.POST.get('pass')
    name = request.POST.get('name')
    try:
        user = auth.sign_in_with_email_and_password('email', passs)
        uid = user['localID']
        idtoken = request.session['uid']
        print(uid)
    except:
        return render(request, 'signin-reg/regist.html')
    return render(request, 'signin.html')


def reset(request):
    return render(request, 'reset.html')


def postreset(request):
    email = request.POST.get('email')
    try:
        auth.send_password_reset_email(email)
        message = "An email to reset password is successfully sent"
        return render(request, 'reset.html', {'msg': message})
    except:
        message = "Something went wrong, Please re-check the email you provided"
        return render(request, 'reset.html', {'msg': message})
# Create your views here.


def dasboardClient(request):
    return render(request, 'client-dashboard.html')


def dasboardClientNone(request):
    return render(request, 'client-dashboard-non.html')


def detailHistory(request):
    return render(request, 'history/history-detail.html')


def base(request):
    return render(request, 'base.html')


def baseSignIn(request):
    return render(request, 'base_signin.html')


def SignIn(request):
    return render(request, 'signin-reg/signin.html')


def regist(request):
    return render(request, 'signin-reg/regist.html')


def outputScenario(request):
    return render(request, 'output-user-scenario/output_scenario.html')


def inputUserStory(request):
    return render(request, 'input-user/input.html')


def history(request):
    return render(request, 'history/history.html')


def userProfile(request):
    return render(request, 'user_profile/user-profile.html')
