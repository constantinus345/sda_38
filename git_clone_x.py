from git import Repo
import os
#pip install python-git

urlx = 'https://github.com/constantinus345/sda_38.git'
print(os.getcwd())

folder = f'{os.getcwd()}/cod_nou'
#os.makedirs(folder)
Repo.clone_from(urlx,folder)