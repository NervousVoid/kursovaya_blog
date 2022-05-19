from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, RegisterForm, CommentForm
from django.contrib.auth.models import User
from .models import Post, Comment
from django.core import serializers
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
    try:
        context = dict()
        if request.method == 'POST':
            f = CommentForm(request.POST)
            if f.is_valid():

                user = request.user
                text = f.data['text']
                comm = Comment(text=text, user=user, post_id=post_id, date=timezone.now())
                comm.save()
                f.full_clean()
        context['form'] = CommentForm()
        post = Post.objects.get(pk=post_id)
        context['post'] = post

        comments = Comment.objects.filter(post_id=post_id).order_by('-date')
        context['comments'] = comments

        return render(request, 'post.html', context)
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
                    context['form'] = RegisterForm()
                    context['errors'] = 'This username is already taken'
            else:
                context['form'] = f
        else:
            context['form'] = RegisterForm()
        return render(request, 'registration/registration.html', context)


# @login_required
# def liker(request, post_id):
#     if request.method == "POST" and request.is_ajax():
#         try:
#             post = Post.objects.get(pk=post_id)
#             if request.user not in post.liked_users:
#                 post.liked_users.append(request.user)
#                 post.rating += 1
#             else:
#                 post.liked_users.remove(request.user)
#                 post.rating -= 1
#             post.save()
#             return redirect('index')
#         except Post.DoesNotExist:
#             raise Http404


@login_required
def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        try:
            action = ''
            post = Post.objects.get(pk=post_id)
            if request.user not in post.liked_users:
                post.liked_users.append(request.user)
                post.rating += 1
                action = 'add'
            else:
                post.liked_users.remove(request.user)
                post.rating -= 1
                action = 'remove'
            post.save()
            ctx = {"post_likes": post.rating, "action": action}
            return HttpResponse(json.dumps(ctx), content_type='application/json')
        except Post.DoesNotExist:
            raise Http404

    #     likedpost = Post.objects.get(id=post_id)
    #     m = Like(post=likedpost)
    #     m.save()
    #     print(123)
    #     return HttpResponse('success')
    # else:
    #     return HttpResponse("unsuccesful")


# @login_required
# def like_button(request):
#     if request.method == "POST":
#         if request.POST.get("operation") == "like_submit":
#             content_id = request.POST.get("content_id", None)
#         content = get_object_or_404(LikeButton, pk=content_id)
#         if content.likes.filter(id=request.user.id):  # already liked the content
#             content.likes.remove(request.user)  # remove user from likes
#             liked = False
#         else:
#             content.likes.add(request.user)
#             liked = True
#         ctx = {"likes_count": content.total_likes, "liked": liked, "content_id": content_id}
#         return HttpResponse(json.dumps(ctx), content_type='application/json')
#
#     contents = LikeButton.objects.all()
#     already_liked = []
#     id = request.user.id
#     for content in contents:
#         if content.likes.filter(id=id).exists():
#             already_liked.append(content.id)
#     ctx = {"contents": contents, "already_liked": already_liked}
#     return render(request, "index.html", ctx)


# def contact_form(request):
#     form = ContactForm()
#     if request.method == "POST" and request.is_ajax():
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             form.save()
#             return JsonResponse({"name": name}, status=200)
#         else:
#             errors = form.errors.as_json()
#             return JsonResponse({"errors": errors}, status=400)
#
#     return render(request, "contact.html", {"form": form})


def index(request):
    context = dict()
    posts = Post.objects.order_by('-date')
    context['posts'] = posts
    return render(request, 'index.html', context)
