import requests
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from licenses.models import Licence
from repositories.models import Repository

URL = 'https://api.github.com/orgs/octokit/repos'
PAGE_SIZE = 20


def get_data(request):
    params = {}
    data = requests.get(URL, params=params)
    print(len(data.json()))
    for repository in data.json():

        license = repository.get('license')
        if license is not None:
            key = license.get('key')
            name = license.get('name')
            license = Licence.objects.get_or_create(key=key, name=name)

        Repository.objects.get_or_create(
            name=repository.get('name', ''),
            private=repository.get('private', ''),
            full_name=repository.get('full_name', ''),
            html_url=repository.get('html_url', ''),
            language=repository.get('language', ''),
            forks_count=repository.get('forks_count', 0),
            size=repository.get('size', 0),
            is_template=repository.get('is_template', False),
            pushed_at=repository.get('pushed_at', 0),
            created_at=repository.get('created_at', 0),
            updated_at=repository.get('updated_at', 0))
    return redirect('repositories')


def repositories(request):
    repos = Repository.objects.all()
    paginator = Paginator(repos, PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'repos.html', {'page': page})
