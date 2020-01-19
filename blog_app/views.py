from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import PostForm, RegisterForm
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone


@login_required
def create_post(request):
    context = dict()
    if request.method == 'POST':
        f = PostForm(request.POST)
        if f.is_valid():

            user = request.user
            name = f.data['name']
            description = f.data['description']
            text = f.data['text']
            date = timezone.now()

            post = Post(user=user, name=name, description=description,
                        text=text, date=date)
            post.save()

            context['form'] = f
            context['post_created'] = True
        else:
            context['form'] = f
    else:
        context['form'] = PostForm()

    return render(request, 'create_post.html', context)


def post_page(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        return render(request, 'post.html', {'post': post})
    except Post.DoesNotExist:
        raise Http404


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        context = dict()
        if request.method == 'POST':
            f = RegisterForm(request.POST)
            if f.is_valid():
                if f.data['username'] not in User.objects.all().values_list('username', flat=True):
                    username = f.data['username']
                    name = f.data['name']
                    surname = f.data['surname']
                    password = f.data['password']

                    usr = User(username=username, first_name=name, last_name=surname)
                    usr.set_password(password)
                    usr.save()

                    context['form'] = f
                    context['user_registered'] = True
                else:
                    context['form'] = f
                    context['errors'] = 'This username is already taken'
            else:
                context['form'] = f
        else:
            context['form'] = RegisterForm()
        return render(request, 'registration/registration.html', context)


def index(request):
    context = dict()
    posts = Post.objects.order_by('-date')
    context['posts'] = posts
    return render(request, 'index.html', context)
