from django.shortcuts import render
from django.views.generic import ListView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from .models import Post,Category,Audio
from django.urls import reverse_lazy # new
from .forms import PostForm,CgForm,AudioForm
from rest_framework import viewsets
from .serializers import UserSerializer,AudioSerializer,CategorySerializer

def index(request):
    return render(request,'index.html')

class UserList(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): # new
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('homes')

class UpdatePost(UpdateView):
    model = Post
    fields = ['name','email','password','sub','cover']
    template_name = 'post.html'
    success_url = reverse_lazy('home')

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class CgList(ListView):
    model = Category
    template_name = 'category.html'

class CreateCgView(CreateView):
    model = Category
    form_class = CgForm
    template_name = 'cgform.html'
    success_url = reverse_lazy('category')

class UpdateCg(UpdateView):
    model = Category
    fields = ['img','name','des']
    template_name = 'cgform.html'
    success_url = reverse_lazy('category')

class DeleteCg(DeleteView):
    model = Category
    template_name = 'cgdelete.html'
    success_url = reverse_lazy('category')

class AudioList(ListView):
    model = Audio
    template_name = 'audio.html'

class AudioCreate(CreateView):
    model = Audio
    form_class = AudioForm
    template_name = 'audioform.html'
    success_url = reverse_lazy('audio')

class AudioUpdate(UpdateView):
    model = Audio
    fields = ['img','name','des','audio','cg','sub']
    template_name = 'audioform.html'
    success_url = reverse_lazy('audio')

class AudioDelete(DeleteView):
    model = Audio
    template_name = 'audiodelete.html'
    success_url = reverse_lazy('audio')

class UserViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AudioViewset(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
