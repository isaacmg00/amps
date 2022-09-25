import requests
import subprocess
import shlex
from bs4 import BeautifulSoup

r = requests.get('https://security.archlinux.org/')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('td', class_='wrap')

arch_packages = []


for x in soup.find_all('td', class_='wrap'):
    arch_packages.append(x.text[1:-1])

print(arch_packages)
for i in arch_packages:
    print(i)

# Python 3.5+
# cmd for arch based systems pacman -Q
cmd = 'pacman -Q'
args = shlex.split(cmd)
proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = proc.stdout.read()
output = output.decode().splitlines()
print(output)
print(type(output))

print(len(output))
