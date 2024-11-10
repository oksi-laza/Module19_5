from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Post


# Create your views here.
def output_posts_on_page(request):
    posts = Post.objects.all().order_by('-created_at')    # получили все объекты в отсортированном порядке от последнего
    posts_per_page = request.GET.get('posts_per_page')    # количество постов на странице, переданное пользователем
    if not posts_per_page:
        posts_per_page = 3    # количество постов на странице по умолчанию
    paginator = Paginator(posts, posts_per_page)    # укажем количество объектов на странице
    page_number = request.GET.get('page')    # получаем текущую страницу(номер) пользователя
    try:
        page_posts = paginator.get_page(page_number)  # к объекту paginator применяем метод get_page с текущей страницей
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    return render(request, 'output_posts_on_page.html',
                  {'page_posts': page_posts, 'posts_per_page': posts_per_page})
