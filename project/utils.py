from . models import Project, Tags
from django.db.models import Q
# from django.core.paginator import Paginator
# from . views import projects


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


# def paginator(request):
#     page = 1
#     results = 3
#     paginator = Paginator(projects, results)

#     projects = paginator.page(page)