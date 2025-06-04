# Python-Basics-For-Better-Understanding
This repository guides some basic python and some more concepts



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
```bash
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

```python
In [1]: import os
   ...: 

In [2]: >>> import os

In [3]: print(os.getcwd())  # Returns current working directory
/home/baijayanta

In [4]: os.path.exists('file.txt')
Out[4]: False

In [5]:                                                                         
Do you really want to exit ([y]/n)? y
```
