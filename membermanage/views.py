from django.shortcuts import render,redirect, render_to_response
from .forms import UserForm, LoginForm
# forms.py는 작성한 폼 파일임, 거기서 각 클래스를 부름
# Create your views here.

def home(request):
    return render(request, "index.html")

def signup(request):
    # 회원가입폼 객체 생성
    form = UserForm
    return render(request, 'signup.html', {"form":form})
    # form 객체를 signup.html으로 넘김

def login(request):
    pass

def logout(request):
    pass