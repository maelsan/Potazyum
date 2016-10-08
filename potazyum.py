#! /usr/bin/env python3

import re, argparse, requests, time, bs4 as BeautifulSoup

# Main domains from Stackoverflow family.
URL_SEARCH = {
    'SEARCH_ROOT_STACK':     'http://stackoverflow.com',
    'SEARCH_ROOT_UNIX':      'http://unix.stackexchange.com',
    'SEARCH_ROOT_SECURITY':  'http://security.stackexchange.com',

    'SEARCH_URI': '/search?q='
}

VERSION = "\033[1;36m1.0.1\033[m"

# We define all options.
parser = argparse.ArgumentParser(description='potazyum [options] -q [question]')
parser.add_argument('-q', '--question', dest='question', default='', help='Your question')
parser.add_argument('-s', '--solved', dest='solved', action="store_true", help='Precise if a answer need to be solved.')
parser.add_argument('-n','--vote', dest='vote', default=False, 
                    help='Precise if a answer need to have a sum of vote equal or superior.')
parser.add_argument('-t','--type', dest='type', default='stack', help='Precise the plateform : stack | unix | security.')
parser.add_argument('-v','--version', dest='version', action="store_true", help='Display version')

options = parser.parse_args()
isLink = re.compile('(.)+', re.IGNORECASE)

if options.version:
    print(VERSION)
    exit()
elif isLink.match(options.question) is None:
    parser.error("\033[1;31m[x]\033[m Write your question, please.")

# StackOverflow tips
options.question = options.question + " answers:1" if options.solved else options.question
options.question = options.question + " score:" + options.vote if options.vote else options.question

# Define URI
options.type = options.type if (options.type == 'stack' or options.type == 'unix' or options.type == 'security') else 'stack'
options.type = URL_SEARCH['SEARCH_ROOT_STACK'] if (options.type == 'stack') else options.type
options.type = URL_SEARCH['SEARCH_ROOT_UNIX'] if (options.type == 'unix') else options.type
options.type = URL_SEARCH['SEARCH_ROOT_SECURITY'] if (options.type == 'security') else options.type

# Now, we use request instead of urllib2.
URI = options.type + URL_SEARCH['SEARCH_URI'] + options.question
request = requests.get(URI)

# BeautifulSoup to parse the DOM en extract all informations.
parse = BeautifulSoup.BeautifulSoup(request.text, 'html.parser')

# If this class is found, that means we are considered as a bot.
# There is no solution (or perhaps, use an another bot to complete automatically this captcha).
if parse.find('body', attrs={'class': 'captcha-page'}):
    print("\033[1;31m[x]\033[m It seems that the remote site prevented us from doing a search. He must consider us as a robot.")
    print(" \033[1;36m->\033[m How to fix that for this session ? Go on " + URI + " and complete the captcha.")
    exit()

resultsHeaders = parse.find('div', attrs={'class': 'subheader results-header'})
resultsHeaders = resultsHeaders.find('h2').text.strip()
print ("Number of potentials results : \033[1;36m" + resultsHeaders + "\033[m")
print ("They will not be all displayed (< 10).\n")

for div in parse.findAll('div', attrs={'class': 'question-summary search-result'}):
    color = "\033[1;33m[?]\033[m "
    if (div.find('div', attrs={'class': 'status'}) is not None):
        status = div.find('div', attrs={'class': 'status'})

        # answered OR answered-accepted elif unanswered
        if status['class'][1] == 'answered' or status['class'][1] == 'answered-accepted':
            color = "\033[1;32m[answered]\033[m "
        elif status['class'][1] == 'unanswered':
            color = "\033[1;31m[unanswered]\033[m "

    link = div.find('a')
    print(color + link.text.strip())
    print(options.type + link['href'].strip() + "\n")
    time.sleep(50.0 / 1000.0)
