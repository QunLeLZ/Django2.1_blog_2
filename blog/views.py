from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from blog.models import Article,Category,Tag,Gbook
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import GbookForm
from django.conf import settings

# Create your views here.
categories = Category.objects.all()
tags = Tag.objects.all()
new_list = Article.objects.order_by('-create_time')[:5]
dates = Article.objects.datetimes('create_time','month',order='DESC')

def index(request):
    posts = Article.objects.all()[:5]
    context = {'post_list':posts,
               'category_list': categories,
               'tag_list': tags,
               'new_list': new_list,
               'date_list':dates,
               }
    return render(request,'index.html',context=context)

def detail(request,id):
    post = get_object_or_404(Article,id=str(id))
    post.viewed()
    post_tag = post.tags.all()
    context = {'post': post,
               'category_list': categories,
               'tag_list': tags,
               'tags':post_tag,
               'new_list': new_list,
               'date_list': dates,
               }
    return render(request,'detail.html', context=context)

def articles(request):
    posts = Article.objects.all()
    paginator = Paginator(posts, 2)
    try:
        page = request.GET.get('page')
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {'post_list': post_list,
               'category_list': categories,
               'tag_list': tags,
               'new_list': new_list,
               'date_list': dates,
               }
    return render(request, 'articles.html', context=context)

def archives(request,year,month):
    posts = Article.objects.filter(create_time__year=year,create_time__month=month).order_by('create_time')
    paginator = Paginator(posts, settings.PAGE_NUM)
    try:
        page = request.GET.get('page')
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {'post_list': post_list,
               'category_list': categories,
               'tag_list': tags,
               'new_list': new_list,
               'date_list': dates,
               }
    return render(request,'archives.html',context=context)

def search_category(request,id):
    posts = Article.objects.filter(category_id=id)
    category = categories.get(id=id)
    paginator = Paginator(posts, settings.PAGE_NUM)
    try:
        page = request.GET.get('page')
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {'post_list': post_list,
               'category':category,
               'category_list': categories,
               'tag_list': tags,
               'new_list': new_list,
               'date_list': dates,
               }
    return render(request,'category.html',context=context)

def search_tag(request,tag):
    posts = Article.objects.filter(tags__name__contains=tag)
    paginator = Paginator(posts, settings.PAGE_NUM)
    try:
        page = request.GET.get('page')
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {'post_list': post_list,
               'category_list': categories,
               'tag_list': tags,
               'new_list': new_list,
               'date_list': dates,
               }
    return render(request,'tag.html',context=context)


def about(request):
    return render(request,'about.html')

def gbook(request):
    form_list = Gbook.objects.all()
    form_gbook = GbookForm()
    if request.method == 'POST':
        form = GbookForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/gbook/')
        else:
            return render(request,'gbook.html',{'form_list':form_list,'form_gbook':form_gbook})
    return render(request,'gbook.html',{'form_list':form_list,'form_gbook':form_gbook})