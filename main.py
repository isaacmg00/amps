import requests
import subprocess
import shlex
import distro
from bs4 import BeautifulSoup


class Package:
    def __init__(self, group, issue, package, affected, fixed, severity, status, ticket, advisory):
        self.group = group
        self.issue = issue
        self.package = package
        self.affected = affected
        self.fixed = fixed
        self.severity = severity
        self.status = status
        self.ticket = ticket
        self.advisory = advisory


def get_system_distribution():
    return subprocess.check_output(['./get_distro.sh'])


system_distro = get_system_distribution()


def get_package_manager(distro):
    return distro.decode("utf-8")


r = requests.get('https://security.archlinux.org/')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find_all('td', class_='wrap')

arch_packages = []

tables = soup.findChildren('table')
my_table = tables[0]
rows = my_table.findChildren(['th', 'tr'])

for row in rows:
    cells = row.findChildren('td')
    for cell in cells:
        value = cell.text
        print(value)
'''
for x in soup.find_all('td', class_='wrap'):
    arch_packages.append(x.text)
    # arch_packages.append(x.text[1:-1])

text = []

for i in soup.find_all('tr'):
    text.append(i.text)

print(text[11])

string = text[11].split("\n")

for item in string:
    if(item == ''):
        print("found nothing")


print(string)
print(type(text[1]))


'''
'''
for i in range(1, len(text)):
    group = i
    package = Package
    print(text[i])
'''
'''
print(arch_packages)
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

check = any(item in arch_packages for item in output)

print(list(set(arch_packages) & set(output)))
print(check)


def intersection(lst1, lst2):

    temp = set(lst2)
    lst3 = [value for value in lst1 if value in temp]
    return lst3


print(intersection(arch_packages, output))
vulnerable_packages = intersection(arch_packages, output)


num_packages = len(output)
print(str(num_packages) + " installed packages.")
print("found " + str(len(vulnerable_packages)) +
      " vulnerable packages on local system.")
print("Check for updates? y/n")

print(get_package_manager(system_distro))
'''
