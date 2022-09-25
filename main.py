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
cmd = 'pacman -Q '
cmd2 = 'cut -f 1 -d " "'
args = shlex.split(cmd)
args2 = shlex.split(cmd2)

proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = subprocess.check_output(args2, stdin=proc.stdout)
#output = proc.stdout.read(args2, stdin=proc.stdout)
proc.wait()

output = output.decode().splitlines()
for item in output:
    print(item)
print(type(output))
print(type(arch_packages))

print(len(output))

check = any(item in arch_packages for item in output)

print(list(set(arch_packages) & set(output)))
print(check)


def intersection(lst1, lst2):

    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


print(intersection(arch_packages, output))
