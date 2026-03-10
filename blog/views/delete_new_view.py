from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from blog.models import News

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'blog/news_delete_form.html'
    success_url = reverse_lazy('blog:news')