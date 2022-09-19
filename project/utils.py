from . models import Project, Tags
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginateProject(request, projects, results):
    page = request.GET.get('page')
    # results = 3
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex =(int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    # projects = paginator.page(page)
    custom_range = range(leftIndex, rightIndex)
    return custom_range, projects



def searchProject(request):
    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    tags = Tags.objects.filter(name__icontains=search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in = tags) |
        Q(description__icontains=search_query)
    )

    return projects, search_query