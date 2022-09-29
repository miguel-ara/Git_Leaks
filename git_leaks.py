#! user/bin/python3

from git import Repo
import re

REPO_DIR = './skale-manager'
KEY_WORDS = ['credentials', 'password', 'key', 'username'] 

def extract(repo_dir):
    repo = Repo(repo_dir)
    dir(repo)
    commits = list(repo.iter_commits('develop'))
    return commits

def transform(commits):

    diccionario = dict()
    for i in commits:
        for word in KEY_WORDS:
            if re.search(word, i.message, re.IGNORECASE):
                key = i.hexsha
                data = i.message
                diccionario[key] = data
                #print(f'Commit: {i.hexsha} - {i.message}')

    return diccionario

def load(diccionario):
    for key in diccionario:
        print(f'Commit: {key} - ', end = '')
        print(f'{diccionario[key]}')

if __name__ == '__main__':
    commits = extract(REPO_DIR)
    diccionario = transform(commits)
    load(diccionario)