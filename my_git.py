import requests
import json

def get_user_git_data(user_name):
    urls= f"https://api.github.com/users/{user_name}/repos"
    response = requests.get(urls)
    status_code=response.status_code;
    if status_code ==403:
        return "Forbidden"
    if status_code !=200:
        return None
    details_list=[]
    for x in response.json():
        details_list.append(x['name'])
    list_commits = []
    for repository in details_list:
        url= f"https://api.github.com/repos/{user_name}/{repository}/commits";
        number = requests.get(url)
        number = len((number.json()))
        list_commits.append(number)
    list_output=[]
    for name, commits in zip(details_list,list_commits):
        result=f"Repository: {name} has {commits} number of commits"
        list_output.append(result)
    return list_output;

if __name__ == "__main__":
    userID = input("Please Enter UserID :- ")
    response = get_user_git_data(userID)
    print(response)


