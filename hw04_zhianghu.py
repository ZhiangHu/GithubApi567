import requests

def get_repositories(url):
    result = []
    r = requests.get(url=url)
    if 'next' in r.links :
        result += get_repositories(r.links['next']['url'])

    for repository in r.json():
        result.append(repository.get('name'))

    return result

url = "https://api.github.com/users/stackforge/repos"
print get_repositories(url)
