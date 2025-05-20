from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Blog, Page, Mis_Posts, Comentarios
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password

# Create your views here.
@login_required
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

@login_required
def view_post(request, id):
    post = Blog.objects.get(id=id)
    comments = Comentarios.objects.filter(blog=post, parent_id=None)
    return render(request, 'views/views_posts.html', {
        'post': post,
        'comments' : comments
    })

@login_required
def profile(request):
    user = request.user
    # Actualizar datos del perfil
    if request.method == 'POST':
        action = request.POST.get('action')

        # Actualizar datos del perfil
        if action == 'update_profile':
            user.username = request.POST.get('username')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.save()
            messages.success(request, '¡Los datos del perfil se actualizaron correctamente!')
            return redirect('profile')

        # Cambiar contraseña
        elif action == 'change_password':
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if not check_password(current_password, user.password):
                messages.error(request, 'La contraseña actual es incorrecta.')
            elif new_password != confirm_password:
                messages.error(request, 'Las nuevas contraseñas no coinciden.')
            else:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Evita que se cierre la sesión
                messages.success(request, '¡La contraseña se cambió correctamente!')
                return redirect('profile')
    return render(request, 'profiles/profile.html', {
        'title': 'Perfil',
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    })

def my_post(request):
    posts = Blog.objects.filter(autor=request.user)
    return render(request, 'my_post/mis_post.html', {
        'title': 'Mis posts',
        'posts': posts
    })

def my_comments(request, id):
    blog = get_object_or_404(Blog, id=id)
    user = request.user
    parent_id = request.POST.get('parent_id')
    parent = Comentarios.objects.get(id=parent_id) if parent_id else None

    if not user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para comentar.')
        return redirect('login')

    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            Comentarios.objects.create(  # Eliminar .save()
                texto=texto,
                blog=blog,  # Corregido de 'post' a 'blog'
                autor=user,
                parent=parent
            )
            messages.success(request, '¡Comentario creado!')
            return redirect('view_post', id=blog.id)
        else:
            messages.error(request, 'El comentario no puede estar vacío.')
    comments = Comentarios.objects.all().filter(blog=blog)
    return render(request, 'views/views_posts.html', {
        'post': blog,
        'comments': comments,
        'title': blog.title
    })

def edit_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        post.save()
        messages.success(request, 'El post se ha actualizado correctamente.')
        return redirect('view_post', id=post.id)
    return render(request, 'edit/edit_post.html', {
        'post': post,
        'title': 'Editar post'
    })

def delete_post(request, id):
    post = get_object_or_404(Blog, id=id)
    post.delete()
    messages.success(request, 'El post se ha eliminado correctamente.')
    return redirect('inicio')