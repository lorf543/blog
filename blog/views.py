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
    if request.method == 'POST':
        form = BlogsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)  # Only print errors if the form is not valid
    else:
        form = BlogsForm()
        
    context = {'form': form}
    return render(request, 'blog/updateblog.html', context)



