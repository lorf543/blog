from django.shortcuts import render, get_object_or_404,redirect,HttpResponse



from .forms import BlogsForm
from .models import Blogs
# Create your views here.

def blog(request):
    
    blogs = Blogs.objects.all()
    context = {'blogs':blogs}

    return render (request,'blog/home.html',context)


def singleblog(request, slug):

    blog = get_object_or_404(Blogs, slug=slug)
    context = {'blog': blog}

    return render(request, 'blog/singleBlog.html', context)



def updateblog(request,slug):
    blog = get_object_or_404(Blogs, slug=slug)

    if request.method == 'POST':
        form = BlogsForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = BlogsForm(instance=blog)
        
    context= {'form':form}

    return render(request,'blog/updateblog.html', context)

def createeblog(request):
    form = BlogsForm()
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    context= {'form':form}

    return render(request,'blog/updateblog.html', context)


