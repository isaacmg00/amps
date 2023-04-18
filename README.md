Amps (Are My Packages Safe?) - A package scanner for Arch Linux based systems
=======================================
[![PyPI version](http://img.shields.io/pypi/v/distro.svg)](https://pypi.org/project/amps/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/distro.svg)](https://img.shields.io/pypi/pyversions/distro.svg)
[![Is Wheel](https://img.shields.io/pypi/wheel/distro.svg?style=flat)](https://pypi.org/project/amps/)

`amps` scans all packages installed via pacman on your system and provides you a simple report of those with open CVE's reported [here.](https://security.archlinux.org/)

Amps currently only supports Arch Linux based systems, but [apt](https://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html), [dpkg](https://wiki.debian.org/dpkg), and [dnf](https://docs.fedoraproject.org/en-US/fedora/latest/system-administrators-guide/package-management/DNF/) capabilities are planned to work for more devices.

## Installation

Via PyPI:
```shell
pip install amps
```
