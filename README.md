# Python-Basics-For-Better-Understanding
This repository guides some basic python and some more concepts so that you can understand it better. 
# OS Module
The `os` module in Python provides a way to interact with the operating system — such as working with files, directories, environment variables, and running system commands.

Here are the snippets to guide you through : 


### Importing the Module

```python
import os
```

### Working with Directories

#### Get Current Directory

```python
print(os.getcwd())  # Returns current working directory
```

#### Change Directory

```python
os.chdir('/path/to/folder')  # Change current working directory
```

#### List Files and Folders

```python
print(os.listdir())  # Lists items in current directory
```

#### Create Directory

```python
os.mkdir('new_folder')  # Create one directory
os.makedirs('parent/child/grandchild')  # Create nested directories
```

#### Remove Directory

```python
os.rmdir('folder')  # Remove empty directory
os.removedirs('parent/child/grandchild')  # Remove nested empty directories
```

---

### Working with Files

#### Check if File/Directory Exists

```python
os.path.exists('file.txt') # Bool If exixts gives True else False
os.path.isfile('file.txt') # Bool This case it returns True
os.path.isdir('folder')    # Bool 
```

#### Rename File/Directory

```python
os.rename('old_name.txt', 'new_name.txt')  # Rename from old_name to new_name
```

#### Remove File

```python
os.remove('file.txt')  # Deletes a file
```

---

### File Path Utilities

```python
path = '/home/user/file.txt'   # put the path here
print(os.path.basename(path))  # file.txt
print(os.path.dirname(path))   # /home/user
print(os.path.splitext(path))  # ('/home/user/file', '.txt')
```

---

## See this terminal snippet to illustrate this in detail. 
```python
(myenv) baijayanta:~$ ipython
Python 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.31.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import os

In [2]: print(os.getcwd())  # Returns current working directory
/home/baijayanta

In [3]: # make a new directory named say python_basics

In [4]: os.path.exists('python_basics') # check whether the directory exists
Out[4]: True

In [5]: # remove it and then make again

In [6]: os.rmdir('python_basics') # remove the directory

In [7]: # check again

In [8]: os.path.exists('python_basics') # check whether the directory exists
Out[8]: False

In [9]: # create now 

In [10]: os.mkdir('python_basics') # make the directory

In [11]: os.path.exists('python_basics') # check whether the directory exists
Out[11]: True

In [12]: # change the directory to 'python_basics'

In [13]: os.chdir("python_basics")  # Change current working directory

In [14]: # print the current directory to see the changes

In [15]: print(os.getcwd())  # Returns current working directory
/home/baijayanta/python_basics

In [16]: # print all the files and directory in the current directory

In [17]: print(os.listdir())  # Lists items in current directory
[]

In [18]: # it's empty make some files

In [19]: touch 1.py
  Cell In[19], line 1
    touch 1.py
           ^
SyntaxError: invalid decimal literal
# use ! sign as it's cmd command.

In [20]: ! touch 1.py

In [21]: print(os.listdir())  # Lists items in current directory
['1.py']

In [22]: os.makedirs('parent/child')  # Create nested directories

In [23]: print(os.listdir())  # Lists items in current directory
['parent', '1.py']

In [24]: # check whether a file exists

In [25]: ! touch parent/new.py

In [26]: os.path.exists('parent/new.py')
Out[26]: True

In [27]: os.path.isfile('parent/new.py')
Out[27]: True

In [28]: os.path.isdir('parent/new.py')
Out[28]: False

In [29]: os.path.isdir('parent/')
Out[29]: True

In [30]: print(os.listdir())  # Lists items in current directory
['parent', '1.py']

In [31]: os.rename('1.py','2.py') # rename

In [32]: print(os.listdir())  # Lists items in current directory
['parent', '2.py']

In [33]: # remove the file

In [34]: os.remove('2.py')

In [35]: print(os.listdir())  # Lists items in current directory
['parent']

In [36]: path = '/home/baijayanta/python_basics/parent/new.py'

In [37]: print(os.path.basename(path))  # gives filename 'new.py'
new.py

In [38]: print(os.path.dirname(path))   # gives the directory
/home/baijayanta/python_basics/parent

In [39]: print(os.path.split(path))   # gives the list with 2 elements 1st one is path and 2nd
    ...:  is file name
('/home/baijayanta/python_basics/parent', 'new.py')

In [40]: # exit

In [41]: exit
(myenv) baijayanta:~$
```

---
## Data types and more
The basic data types in python are - 
- Integer
- Float
- Complex
- Boolean
- List
- Tuple
- Dictionary
- String
- Set
  

```python
# basic data types


```

