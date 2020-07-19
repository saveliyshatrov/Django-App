from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Article, Comment, Student
from . import logic



def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    students = Student.objects.all()
    for i in range(len(students)):
        if students[i].delete == 'yes':
            Student.objects.filter(student_name = students[i].student_name).delete()
    return render(request, 'article/list.html', {'latest_articles_list': latest_articles_list, 'students': students})

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id) 
    except:
        raise Http404("ERROR")
    
    latest_comments_list = a.comment_set.order_by('-id')[:1]
    for i in range(len(latest_comments_list)):
        b, c, d = logic.SplitAndGive(latest_comments_list[i].author_name)

    return render(request, 'article/detail.html', {'article': a, 'latest_comments_list': latest_comments_list, 'b': b, 'c': c, 'd': d})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id) 
    except:
        raise Http404("ERROR")
    a.comment_set.create(author_name = request.POST['name'])

    return HttpResponseRedirect(reverse('detail', args = (a.id,)) )

def about(request):
    return render(request, 'article/about.html')

@csrf_exempt
def students_info(request):

    if request.method == "POST":
        if request.POST['delete'] == 'yes':
            Student.objects.filter(student_name = request.POST['name']).delete()

        if request.POST['delete'] == 'no':
            Student.objects.create(student_name = request.POST['name'], student_course = request.POST['email'], delete = request.POST['delete'])


    return HttpResponseRedirect(reverse('index'))
