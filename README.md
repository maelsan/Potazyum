# Potazyum
[![Software License](https://img.shields.io/badge/license-GNU%20GPL%20V2-green.svg?style=flat-square)](LICENSE) [![Version](https://img.shields.io/badge/version-1.0.0-red.svg?style=flat-square)](https://github.com/maelsan/Potazyum)
[![OS](https://img.shields.io/badge/OS-Linux-orange.svg?style=flat-square)](https://github.com/torvalds/linux)

![](https://github.com/maelsan/Potazyum/blob/master/demo-2.gif?raw=true)

## Installation
Execute the script named `install`, simply.

And if you want delete it, use again `install` but with the option `-r`

## How to use it

    -q or --question For write your question.
    -s or --solved To view only the questions marked as resolved.
    -n or --vote To view only the questions that have a vote sum greater than or equal.
    -t or --type To specify the site you want to search (StackOveflow, Unix, Security).
    -h or --help For display the help message (man).
    -v or --version For display the current version of your Potazyum.

Examples :

    potazyum -q "How to make a sandwich" -s -n 30 # By default, on stackoverflow.com
    potazyum -q "How to hack the NSA" -s -t security # Here, on security.stackexchange.com
    potazyum -q "Why systemd" -t unix -n 2 # And there, on unix.stackexchange.com

## Dependencies
Environment :

- Python3

Modules / Libraries :

- BeautifulSoup
- urllib
- optparse
- re
- time

## Licence
The GNU GENERAL PUBLIC LICENSE V2 (GNU GPL V2). Please see License File for more information.
