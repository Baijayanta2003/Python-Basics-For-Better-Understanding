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

