from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from apps.telegram.views import get_text

from . import models as m


# Create your views here.
def index(request):
    setting_id = m.Settings.objects.latest('id')
    static_all = m.About.objects.all().order_by("?")[:3]
    static = m.Stati.objects.all().order_by()
    product_all = m.Product.objects.all()
    interesting = m.Interesting.objects.all()
    return render(request, "base/index.html", locals())


def about(request):
    about_id = m.AboutMain.objects.latest('id')
    static = m.Stati.objects.all()
    static_all = m.About.objects.all().order_by("?")[:3]
    return render(request, "base/about.html", locals())


def coming(request):
    return render(request, "base/coming-soon-full.html", locals())


def gallery(request):
    # Assuming YourModel is the model you want to paginate
    queryset = m.Product.objects.all()

    paginator = Paginator(queryset, 3)  # Show 10 items per page

    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginated_queryset = paginator.page(paginator.num_pages)

    return render(request, "base/gallery.html", {'paginated_queryset': paginated_queryset})


# добавоение талаграм бота
def contact_view(request):
    if request.method == "POST":
        message = request.POST.get('message')
        text = request.POST.get('text')
        email = request.POST.get('email')
        if message:
            m.Сontacts.objects.create(message=message, text=text, email=email)

        get_text(f""" Оставлен отзыв 
                Имя пользователя: {message}
                Номер телефона: {text}
                Сообщение: {email}
                """)
        return redirect('index')
    return render(request, 'base/contacts.html', locals())


def where(request):
    static_all = m.About.objects.all()
    return render(request, "base/where.html", locals())


def blog(request):
    return render(request, "blog/blog-list.html", locals())


# форма обратного связи
def blog_post(request):
    blog = m.Blog.objects.latest('id')
    if request.method =="POST":
        email = request.POST.get('email')
        message = request.POST.get('comment')
        name = request.POST.get('author')
        m.Сontacts.objects.create(email=email, message=message, name=name)
        send_mail(
            f'{message}',

            f"""Здравствуйте.
            Спасибо за обратную связь, мы скоро свами свяжемся.
            Ваще сообщение: {message} 
            Ваша почта: {email}
            Ваш Имя {name}
            Если вы ошиблись при указании данных можете обратно зайти на сайт и оставить новый отзыв с правильными данными """,
            "noreply@somehost.local",
            [email])
        return redirect('blog')
    return render(request, "blog/blog-post.html", locals())


def not_faund(request):
    return render(request, "404/404.html", status=404)
