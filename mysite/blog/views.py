from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('blog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

	
def historia(request):
	return render(request,'blog/historia.html')
	
def myv(request):
	return render(request,'blog/myv.html')
	
def departamentos(request):
	return render(request,'blog/departamentos.html')
	
def anatomia(request):
	return render(request,'blog/anatomia.html')

def biologia(request):
	return render(request,'blog/biologia.html')
	
def bioquimica(request):
	return render(request,'blog/bioquimica.html')
	
def cirugia(request):
	return render(request,'blog/cirugia.html')

def embriologia(request):
	return render(request,'blog/embriologia.html')
	
def farmacologia(request):
	return render(request,'blog/farmacologia.html')
	
def fisiologia(request):
	return render(request,'blog/fisiologia.html')

def filosofia(request):
	return render(request,'blog/filosofia.html')
	
def informatica(request):
	return render(request,'blog/informatica.html')
	
def ciencias(request):
	return render(request,'blog/ciencias.html')

def microbiologia(request):
	return render(request,'blog/microbiologia.html')
	
def psiquiatria(request):
	return render(request,'blog/psiquiatria.html')