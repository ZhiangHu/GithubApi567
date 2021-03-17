import requests

def get_repositories(username):
    list1 = list()
    f='https://api.github.com/users/'+{username}+'/repos'
    re = requests.get(f)
    json = re.json()
    for  p  in  range ( 0 , len ( json )):
        rename = json[p]['name']
        n='https://api.github.com/repos/'+{username}+'/'+{rname}+'/commits'
        commit = requests.get(n)
        c = commit.json()
        list1.append(f"Repo: {rename} Commits number: {len(c)}")
    return list1

def main():
    username = input("Enter the username:")
    print(get_repositories(username))

if __name__=='__main__':
    main()
