from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import PostForm, RegisterForm, CommentForm
from django.contrib.auth.models import User
from .models import Post, Comment
from django.utils import timezone
import json


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

            context['form'] = PostForm()
            context['post_created'] = True
        else:
            context['form'] = f
    else:
        context['form'] = PostForm()

    return render(request, 'create_post.html', context)


def post_page(request, post_id):
    context = dict()
    if request.method == 'POST':
        try:
            f = CommentForm(request.POST)
            if f.is_valid():
                user = request.user
                text = f.data['text']
                comm = Comment(text=text, user=user, post_id=post_id, date=timezone.now())
                comm.save()
                f.full_clean()
                return HttpResponseRedirect(str(post_id))
        except Post.DoesNotExist:
            raise Http404

    context['form'] = CommentForm()
    post = Post.objects.get(pk=post_id)
    context['post'] = post

    comments = Comment.objects.filter(post_id=post_id).order_by('-date')
    context['comments'] = comments

    return render(request, 'post.html', context)


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
                    context['form'] = RegisterForm()
                    context['errors'] = 'This username is already taken'
            else:
                context['form'] = f
        else:
            context['form'] = RegisterForm()
        return render(request, 'registration/registration.html', context)


@login_required
def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        try:
            action = ''
            post = Post.objects.get(pk=post_id)
            if request.user not in post.liked_users.all():
                post.liked_users.add(request.user)
                action = 'add'
            else:
                post.liked_users.remove(request.user)
                action = 'remove'
            post.save()
            ctx = {"post_likes": post.get_rating(), "action": action}
            return HttpResponse(json.dumps(ctx), content_type='application/json')
        except Post.DoesNotExist:
            raise Http404


def index(request):
    context = dict()
    posts = Post.objects.order_by('-date')
    context['posts'] = posts
    return render(request, 'index.html', context)
