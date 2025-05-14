from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog, Page
from django.core.paginator import Paginator

# Create your views here.
def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            image = request.FILES.get('image_post')
            title = request.POST.get('title')
            content = request.POST.get('content')
            post = Blog.objects.create(
                imagen_post=image, title=title, content=content, autor=request.user
            )
            post.save()
            messages.success(
                request, 'El post se ha creado correctamente!!'
            )
            return redirect('show_post')
    return render(request, 'create_post/post_create.html', {
        'title': 'Create Post'
    })
    

def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html",{
        "page": page
    })


def show_post(request):
    posts = Blog.objects.all().order_by('created_at')
    paginator = Paginator(posts, 6)
    # recoger el numero de la pagina
    page= request.GET.get('page')
    # para guardar los articulos de la pagina
    page_articles= paginator.get_page(page)
    return render(request, 'mainapp/index.html', {
        'title': 'Pagina Principal',
        'posts': page_articles,
    })

def view_post(request, id):
    post = Blog.objects.get(id=id)
    return render(request, 'views/views_posts.html', {
        'post': post
    })