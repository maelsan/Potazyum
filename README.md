# Potazyum
[![Software License](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE) [![codebeat badge](https://codebeat.co/badges/f970588a-3843-448b-8c71-6a3f3140707b)](https://codebeat.co/projects/github-com-maelsan-potazyum) [![Build Status](https://travis-ci.org/maelsan/Potazyum.svg?branch=master)](https://travis-ci.org/maelsan/Potazyum)


![](https://github.com/solikate/Potazyum/blob/master/pictures/demo-2.gif?raw=true)

## Use Potazyum
Here's all options available on Potazyum:

```
-q or --question 	Your question
-s or --solved 		To view only the questions marked as resolved
-n or --vote 		To view only the questions that have a vote sum greater than or equal
-t or --type 		To specify the site you want to search (StackOveflow, Unix, Security)
-h or --help 		For display the help message (man)
-v or --version 	For display the current version of your Potazyum
 ```

You can use them together, as follow:

```shell
potazyum.py -q "Stop a go routine" -s -n 30 	# Only solved, > 30 upvotes & by default on stackoverflow.com
potazyum.py -q "Zero day" -s -t security 		# Ony solved, on security.stackexchange.com
potazyum.py -q "What is systemd" -t unix -n 2 	# On unix.stackexchange.com, > 2 upvotes
```

## Accessibility

I made this script without real installation process. I suppose that you have enough knowledge about how to add an executable to your path (or to your `bin` directory according to your system). After you added potazyum to your path/bin folder, you will access it from everywhere in your terminal.

## Dependencies
Potazyum has been made with Python3, and this project uses some libraries that you must install before all.

```
pip install -r requirements.txt
```

## Licence
The GNU GENERAL PUBLIC LICENSE V2 (GNU GPL V2). Please see License File for more information.
