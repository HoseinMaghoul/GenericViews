# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# from .models import Post, Comment
# from .forms import PostForm
# from django.views import generic
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# # Create your views here.
#
#
# @api_view(['GET', 'POST'])
# def index(request):
#     return Response({"name":"hosein"})
#     # return Response(dict(request.data))
#
#
#
#
# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     template_name = 'posts/post_list.html'
#     context_object_name = 'posts'
#
#
#
#
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, **kwargs):
#         context = super(PostDetail, self).get_context_data()
#         context['comments'] = Comment.objects.filter(post=kwargs['object'].pk)
#         return context
#
#
#
# def post_create(request):
#     if request.metthod == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post.objects.create(**form.changed_data)
#             return HttpResponseRedirect('/posts/')
#     else:
#         form = PostForm()
#
#     return render(request, 'posts/post_create.html', {'form':form})
