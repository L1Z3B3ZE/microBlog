from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import *
from .models import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout


class BBLoginView(LoginView):
    template_name = 'blog/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'blog/logout.html'


class RegisterView(CreateView):
    template_name = 'blog/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')


class ProfilePostsView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/profile.html'
    context_object_name = 'post_user'

    def get_queryset(self):
        return (
            Post.objects.filter(user=self.request.user)
        )


class ChangeUserInfoView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'blog/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'blog/user_confirm_delete.html'
    success_url = reverse_lazy('mainpage')

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/change_user_info.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostView(generic.ListView):
    'вывод постов'
    model = Post
    template_name = 'blog/blog.html'
    paginate_by = 50
    context_object_name = 'post_list'


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment = Comment.objects.filter(post=post)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect('post_detail', pk)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {'post': post, 'comment': comment, 'form': form})


#
@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_update.html', {'form': form, 'comment': comment})


@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        if request.method == 'POST':
            post_id = comment.post.id
            comment.delete()
            return redirect('post_detail', pk=post_id)
    return render(request, 'blog/comment_confirm_delete.html', {'comment': comment})
