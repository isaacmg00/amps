import requests
import subprocess
import shlex
import distro
from bs4 import BeautifulSoup


def get_system_distribution():
    return subprocess.check_output(['./get_distro.sh'])


system_distro = get_system_distribution()


def get_package_manager(distro):
    return distro.decode("utf-8")


r = requests.get('https://security.archlinux.org/')
soup = BeautifulSoup(r.content, 'html.parser')
arch_packages = []
vuln_packages = []

index = 1
list = []

for x in soup.find_all('td', class_='wrap'):
    list.append([x.text[1:-1], index])
    index += 1
    arch_packages.append(x.text[1:-1])

# Python 3.5+
# cmd for arch based systems pacman -Q
cmd = 'pacman -Q '
cmd2 = 'cut -f 1 -d " "'
args = shlex.split(cmd)
args2 = shlex.split(cmd2)

proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = subprocess.check_output(args2, stdin=proc.stdout)
proc.wait()

output = output.decode().splitlines()


def intersection(lst1, lst2):
    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


vulnerable_packages = set(intersection(arch_packages, output))

for vuln in vulnerable_packages:
    print(str(arch_packages.index(vuln)+1) + " " + str(vuln))


num_packages = len(output)
print(str(num_packages) + " installed packages.")
print("found " + str(len(vulnerable_packages)) +
      " vulnerable packages on local system.")
print("Check for updates? y/n")

print(get_package_manager(system_distro))
