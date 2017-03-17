설치

Last login: Wed Mar 15 23:53:57 on ttys000
kimui-MacBook-Pro:~ kim$ pip3 install tensorflow
Collecting tensorflow
  Downloading tensorflow-1.0.0-cp36-cp36m-macosx_10_11_x86_64.whl (39.7MB)
    100% |████████████████████████████████| 39.7MB 35kB/s
Requirement already satisfied: six>=1.10.0 in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from tensorflow)
Requirement already satisfied: numpy>=1.11.0 in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from tensorflow)
Collecting protobuf>=3.1.0 (from tensorflow)
  Downloading protobuf-3.2.0-py2.py3-none-any.whl (360kB)
    100% |████████████████████████████████| 368kB 3.1MB/s
Collecting wheel>=0.26 (from tensorflow)
  Downloading wheel-0.29.0-py2.py3-none-any.whl (66kB)
    100% |████████████████████████████████| 71kB 4.7MB/s
Requirement already satisfied: setuptools in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from protobuf>=3.1.0->tensorflow)
Installing collected packages: protobuf, wheel, tensorflow
Successfully installed protobuf-3.2.0 tensorflow-1.0.0 wheel-0.29.0
kimui-MacBook-Pro:~ kim$ sudo pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py3-none-any.whl
Password:
The directory '/Users/kim/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/kim/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting tensorflow==1.0.1 from https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py3-none-any.whl
  Downloading https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py3-none-any.whl (39.3MB)
    100% |████████████████████████████████| 39.3MB 34kB/s
Requirement already up-to-date: six>=1.10.0 in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from tensorflow==1.0.1)
Requirement already up-to-date: numpy>=1.11.0 in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from tensorflow==1.0.1)
Requirement already up-to-date: wheel>=0.26 in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from tensorflow==1.0.1)
Requirement already up-to-date: protobuf>=3.1.0 in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from tensorflow==1.0.1)
Collecting setuptools (from protobuf>=3.1.0->tensorflow==1.0.1)
  Downloading setuptools-34.3.2-py2.py3-none-any.whl (389kB)
    100% |████████████████████████████████| 399kB 2.0MB/s
Collecting packaging>=16.8 (from setuptools->protobuf>=3.1.0->tensorflow==1.0.1)
  Downloading packaging-16.8-py2.py3-none-any.whl
Collecting appdirs>=1.4.0 (from setuptools->protobuf>=3.1.0->tensorflow==1.0.1)
  Downloading appdirs-1.4.3-py2.py3-none-any.whl
Collecting pyparsing (from packaging>=16.8->setuptools->protobuf>=3.1.0->tensorflow==1.0.1)
  Downloading pyparsing-2.2.0-py2.py3-none-any.whl (56kB)
    100% |████████████████████████████████| 61kB 3.5MB/s
Installing collected packages: tensorflow, pyparsing, packaging, appdirs, setuptools
  Found existing installation: tensorflow 1.0.0
    Uninstalling tensorflow-1.0.0:
      Successfully uninstalled tensorflow-1.0.0
  Found existing installation: pyparsing 2.1.10
    Uninstalling pyparsing-2.1.10:
      Successfully uninstalled pyparsing-2.1.10
  Found existing installation: setuptools 28.8.0
    Uninstalling setuptools-28.8.0:
      Successfully uninstalled setuptools-28.8.0
Successfully installed appdirs-1.4.3 packaging-16.8 pyparsing-2.2.0 setuptools-34.3.2 tensorflow-1.0.1