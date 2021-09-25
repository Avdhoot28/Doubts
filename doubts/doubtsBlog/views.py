from django.shortcuts import render
from .models import Doubt, Answer
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.


def home(request):
    context = {
        'doubts': Doubt.objects.all(),
        'colors': ['bg-dark', 'bg-danger'],
        'from_date': timezone.now()
    }
    return render(request, 'doubtsBlog/index.html', context)


class DoubtListView(LoginRequiredMixin, ListView):
    model = Doubt
    template_name = 'doubtsBlog/index.html'  # <app>/<model>_<viewtype>.html
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['doubts'] = Doubt.objects.all().order_by('-date_posted')
        context['colors'] = ['bg-dark', 'bg-danger']
        context['from_date'] = timezone.now()
        return context
    # context_object_name = 'posts'
    ordering = ['-date_posted']

class DoubtDetailView(LoginRequiredMixin, DetailView):
    model = Doubt

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        obj = super().get_object()
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['answer_list'] = Answer.objects.filter(doubt = obj.id)
        return context

class DoubtCreateView(LoginRequiredMixin, CreateView):
    model = Doubt
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['content', 'image']

    def form_valid(self, form):
        # print(self.kwargs['pk'])
        form.instance.author = self.request.user
        obj = Doubt.objects.get(pk=self.kwargs['pk'])
        form.instance.doubt = obj
        return super().form_valid(form)


class DoubtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Doubt
    success_url = '/'

    def test_func(self):
        doubt = self.get_object()
        if self.request.user == doubt.author:
            return True
        return False


class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    success_url = reverse_lazy('doubtsBlog-home')

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.author:
            return True
        return False



class AuthorDetailView(DetailView):

    queryset = Answer.objects.all()
    success_url = reverse_lazy('doubtsBlog-home')

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.votes += 1
        obj.save()
        return obj











