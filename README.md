# 100dayspython

100 Days Coding Challange with Python

## Day 1 Installation

### Installation

* [Python 3.7.3](https://www.python.org/downloads/)
* VS-Code python Addon (ms-python.python)
* ```python -m pip install --upgrade pip #upgrade PIP in this case 19.0.3```

### Content

Hello world and simple String processing!
I took Hello World and played with it.
Towards the end i found out about the .format() function, which offered a lot of tools for manipulating Strings

### Sources

[pyformat.info](https://pyformat.info/)
[pythonforbeginners.com](https://www.pythonforbeginners.com/basics/string-manipulation-in-python)

### TODOs

Findout what the ** means (line 3)

```python
formString = "{last} {first}"
data = {"first": "cool!", "last": "you are"}
print ( formString.format(**data) ) 
```

Read Files and apply String Manipulation

## Day 2

### functions

* defining functions in python [docs.python.org](https://docs.python.org/dev/tutorial/controlflow.html#more-on-defining-functions)
* def: for defining functions
* in is for checking if something is in a list
* you can directly call your argument with its name in the function call func(name="franz") < will always set name to franz no matter on which position
* you can give default values in the definition def test(name="Franz") it will be overwritten when an argument is passed
* the form **data recieves a dictionary
* with / in the definition you can force to call an argument by position ```def pos_only_arg(arg, /):``` < this cannot be called by ```pos_only_arg(arg=2)``` < This is new in 3.8
* with \* in the definition you can force to call an argument by name def ```name_only_arg(*, name):``` < this cannot be called by ```name_only_arg(2)```
* with \*name you can input an arbitrary amount of inputs that get saved in a Tuple ```def test(*args):```

### Tuples

* How to Tuple: ```tuple = (1,2,3)``` or ```a = 1,2,3```
* unpacking ```b,c,d = a```
* Tuples are immutable, this means they cannot be changed
* behave pretty much like Lists minus the changeability

## Day 3

### Packages and HTTP-Requests
* How To import ```ìmport <packagename>``` or ```from <packagename> import <thing>```
* [requests](https://2.python-requests.org) package for http request handling
* [colorama](https://pypi.org/project/colorama/) for colorful printing in cmd/bash
* requests supports proxies with ```requests.get(url, proxies=<prxyDict>)```
* requests supports sslVerify skip with ```requests.get(url, verify=False)```
* doing the skip throws warnings (as it should be) you can surpress those with ```requests.packages.urllib3.disable_warnings()```

### Lambda Functions on AWS
* ```def lambda_handler(event, context):``` for the event handler event is the object from the request with return you can manage the http response
* external packages need to be installed via ```pip install <packageName> --target ./``` in the root directory
* everything needs to be zipped and pushed to AWS lambda services

### Pycharm
* jetbrains provides an [opensource IDE for Pyton](https://www.jetbrains.com/pycharm/?fromMenu)

### TODOS
* learn how to work with requirements.txt on AWS lambdas

## Day 4

### Classes
* classes are created via ```class [name]:``` and then filled via the typical indent bracket
* you can define variables and functions inside the Class
* the function ```def __init__(self): ``` is the constructor function
* you can check if an instance is a type of a class via ```isinstance(instance, typename)```

### Misc
* you can print dicts as pretty JSON for example like this ```json.dumps(dic, indent=4)```