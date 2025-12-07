from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import BlogPost
from .forms import BlogPostForm


class BlogListView(ListView):
    model = BlogPost
    template_name = "blogs/blog_list.html"
    context_object_name = "posts"
    ordering = ["-date_added"]


class BlogCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")


class BlogUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")
