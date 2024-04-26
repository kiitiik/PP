from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_hime.html', {'news': news})


class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm
    permission_required = 'news.change_news'


class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = Artiles
    success_url = '/news/'
    template_name = 'news/news-delete.html'
    permission_required = 'news.delete_news'


@permission_required(perm='news.add_news', raise_exception=True)
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'форма заполнена не верно'

    form = ArtilesForm()
    data = {
        'form': form,
        'error': error

    }
    return render(request, 'news/create.html', data)
