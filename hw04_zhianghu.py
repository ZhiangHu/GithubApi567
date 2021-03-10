import requests

def get_repositories(username):
    list1 = list()
    f='https://api.github.com/users/'+{username}+'/repos'
    r = requests.get(f)
    json = r.json()
    for  p  in  range ( 0 , len ( json )):
        rname = json[p]['name']
        n='https://api.github.com/repos/'+{username}+'/'+{rname}+'/commits'
        commit = requests.get(n)
        c = commit.json()
        list1.append(f"Repo: {rname} Commits number: {len(c)}")
    return list1

def main():
    username = input("Please enter the username:")
    print(get_repositories(username))

if __name__=='__main__':
    main()
