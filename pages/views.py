from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from django.urls import reverse_lazy
from django.utils.text import slugify
from .models import Items, CommentAuthenticated, CommentAnonymous, ViewsItems, FavoriteItems, GalleryItems
from .forms import CommentAuthenticatedForm, CommentAnonymousForm, EditItemForm, CreateItemForm
from django.utils.text import slugify


class IndexView(ListView):
    model = Items
    template_name = 'pages/index.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        return Items.objects.filter(is_available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добро пожаловать'
        return context


class ShowDetailView(DetailView):
    model = Items
    context_object_name = 'item'
    slug_url_kwarg = 'slug_item'
    template_name = 'pages/detail.html'
    extra_context = {
        'form_comment_anonymous': CommentAnonymousForm,
        'form_comment_authentication': CommentAuthenticatedForm
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        item = get_object_or_404(Items, slug=self.kwargs['slug_item'])
        if self.request.user.is_authenticated:
            if not self.request.session.session_key:
                self.request.session.save()

            user_session_key = self.request.session.session_key
            status_view = ViewsItems.objects.filter(item=item, user_session=user_session_key).exists()
            if status_view is False and user_session_key != 'None':
                view = ViewsItems()
                view.item = item
                view.user_session = user_session_key
                view.save()
                item.views += 1
                item.save()

        context['comments_anonymous'] = CommentAnonymous.objects.filter(item=item)
        context['comments_authenticated'] = CommentAuthenticated.objects.filter(item=item)
        return context


def create_comment_anonymous(request, pk_item):
    form = CommentAnonymousForm(data=request.POST)
    item = Items.objects.get(pk=pk_item)

    if form.is_valid():
        data_form = form.cleaned_data
        comment = CommentAnonymous.objects.create(name=data_form['name'], content=data_form['content'], item=item)
        comment.save()
        return redirect('detail', slug=item.slug)


def create_comment_authenticated(request, pk_item):
    form = CommentAuthenticatedForm(data=request.POST)
    item = Items.objects.get(pk=pk_item)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.item = item
        comment.save()
        return redirect('detail', slug=item.slug)


def favorite_logic(request, pk_item):
    user_id = request.user.pk
    status_favorite = FavoriteItems.objects.filter(author_id=user_id, item_id=pk_item).exists()

    if not status_favorite:
        FavoriteItems.objects.create(author_id=user_id, item_id=pk_item)
    else:
        FavoriteItems.objects.get(author_id=user_id, item_id=pk_item).delete()

    return redirect(request.META.get('HTTP_REFERER', 'index_page'))


def favorite_view(request):
    favorite_items = FavoriteItems.objects.filter(author=request.user)

    context = {
        'favorite_items': favorite_items,
        'title': 'Фавориты'
    }
    return render(request, 'pages/favorite.html', context)


class EditItemView(UpdateView):
    model = Items
    form_class = EditItemForm
    template_name = 'pages/edit_item.html'
    extra_context = {
        'title': 'Изменение товара'
    }

    def get_success_url(self):
        return reverse_lazy('index_page')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk_item'])


class CreateItemView(CreateView):
    model = Items
    form_class = CreateItemForm
    template_name = 'pages/create_item.html'
    extra_context = {
        'title': 'Создание товара'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)
        if 'image' in self.request.FILES:
            images = self.request.FILES.getlist('image')
            for img in images:
                GalleryItems.objects.create(image=img, item=form.instance)
        return response

    def get_success_url(self):
        return reverse_lazy('index_page')


def delete_item(request, pk_item):
    item = get_object_or_404(Items, pk=pk_item)
    item.delete()
    return redirect(request.META.get('HTTP_REFERER', 'index_page'))