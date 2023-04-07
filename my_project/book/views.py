from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import Book, BookInstance

# Create your views here.
def index(request):
    num_books = BookInstance.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_available = BookInstance.objects.filter(availability='Y').count()
    return render(request, 'book/index.html')


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/book_form.html'
    fields = '__all__'
    success_url = reverse_lazy('book:index')


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    fields = '__all__'
    success_url = reverse_lazy('book:index')


class BookInstanceCreateView(CreateView):
    model = BookInstance
    template_name = 'book/book_instance_form.html'
    fields = ['book']
    success_url = reverse_lazy('book:detail_instance', kwargs={'id': '00000000-0000-0000-0000-000000000000'})
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        form.instance.giver = self.request.user
        instance = form.save()
        self.success_url = reverse_lazy('book:detail_instance', kwargs={'id': instance.id})
        return redirect(self.success_url)


class BookInstanceDetailView(DetailView):
    model = BookInstance
    template_name = 'book/book_instance_detail.html'
    fields = '__all__'
    success_url = reverse_lazy('book:detail_instance')
    pk_url_kwarg = 'id'


class BookInstanceUpdateView(UpdateView):
    model = BookInstance
    template_name = 'book/book_instance_update.html'
    fields = ['borrow_the_book']
    success_url = reverse_lazy('book:list_instance')
    pk_url_kwarg = 'id'


class BookInstanceListView(ListView):
    model = BookInstance
    template_name = 'book/book_instance_list.html'
    queryset = BookInstance.objects.order_by('book')
    context_object_name = 'book_instance_list'