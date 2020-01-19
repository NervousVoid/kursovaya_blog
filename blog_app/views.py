from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from .forms import PostForm
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


def index(request):
    context = dict()
    posts = Post.objects.order_by('-date')
    context['posts'] = posts
    return render(request, 'index.html', context)
