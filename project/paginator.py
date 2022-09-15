from django.core.paginator import Paginator
from . views import projects


page = 1
results = 3
paginator = Paginator(projects, results)

projects = paginator.page(page)