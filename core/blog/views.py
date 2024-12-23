from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.form import ContactForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.views import View
from accounts.models import Profile



class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    
    '''
    a class  based listview to show post_list page
    '''
    # this two command to way for  get object all 
    permission_required = "blog.view_post"
    
    model = Post
    # queryset = Post.objects.all()
    template_name = "blog/post_list.html"  

    # change name for object_list and choses your opinion name
    context_object_name = 'posts'
    paginate_by = 3
    # if we added ordering must changing  structure
    ordering = '-id'
    
    # disable when ordering use
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
 
 
class PostDetailView(LoginRequiredMixin, DetailView):
    '''
    a class  based DetailView to show post_detail page
    '''
    model = Post    
    template_name = "blog/post_detail.html"   



class PostCreateView(LoginRequiredMixin, CreateView):
    '''
    a class  based CreateView to show post_form page
    '''
    model = Post 
    # form_class = PostForm
    fields = ['title','content','status','category','published_date']
    success_url = '/'
    template_name = "blog/post_form.html" 

    # get user login and filed author object
    def form_valid(self, form):
        self.object = form.save(commit=False)
        profile = get_object_or_404(Profile, user=self.request.user)
        form.instance.author = profile
        self.object.save()
        return super().form_valid(form)
    
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    '''
    a class  based UpdateView to show post_form page
    '''  
    model = Post 
    form_class = PostForm
    success_url = '/'
    template_name = "blog/post_form.html" 


class PostDeleteView(LoginRequiredMixin, DeleteView):
    '''
    a class  based DeleteView to show post_form page
    '''  
    model = Post 
    success_url = '/'
    template_name = "blog/post_confirm_delete.html" 


class PostDoneView(LoginRequiredMixin, View):  
    '''
    a class  based DoneView to done post in page
    '''  
    model = Post
    success_url = "/"
    def get(self,request,*args,**kwargs):
        # print('post id :',kwargs["pk"])
        post = get_object_or_404(Post,pk=kwargs['pk'])
        post.status = True
        post.save()
        # print('post status update')
        return redirect(self.success_url)
  
'''
fbv for templateview
'''
# def indexView(request):
#     '''
#     a function based view to show index page
#     '''
#     name = "ali"
#     context = {"name":name}
#     return render(request, 'index.html',context)

'''
fbv for redirect
'''
# from django.shortcuts  import redirect
# def RedirectToMaktab(request):
#     return redirect("https://maktabkhooneh.com")

'''
a class  based templateview to show Index page
'''
# class IndexView(TemplateView):
#     template_name = "index.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["name"] = "ali"
#         context["posts"] = Post.objects.all()
#         return context
   

'''
a class  based redirectview to show redirect_to_maktabkhooneh page
'''
# class  RedirectToMaktab(RedirectView): 
#     url ='https://maktabkhooneh.com'
#     def get_redirect_url(self, *args, **kwargs):
#         post = get_object_or_404(Post,pk=kwargs['pk'])
#         print(post)
#         return super().get_redirect_url(*args, **kwargs)






# class PostCreateView(FormView):

    #a class  based FormView to show post_create page

    # template_name = 'blog/contact.html'
    # # f    # form_class = ContactForm
    # form_class = PostForm
    # success_url = '/blog/post/'
    
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)   



    
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view()
# def ApiPostListView(request):
#         return Response("ok")
        