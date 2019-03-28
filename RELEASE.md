# tk-astips-toy-cabinet
Studio asset-lib manager.


### FEATURE
* Database based (Postgresql/MySql/Sqlite)
* Tag filter
* Dominant color filter
* Manage user permission by admin
* Extendable by client
* Supports Windows, Linux


### DEPENDENCY
* [QtSide](https://github.com/astips/QtSide) `1.0.2 +`
* [peewee](https://github.com/coleifer/peewee) `3.8.2 +`
* [psycopg2](https://github.com/psycopg/psycopg2) `for PostgreSql-DB`
* [pypinyin](https://github.com/mozillazg/python-pinyin)
* [Pillow](https://github.com/python-pillow/Pillow)
* [numpy](https://github.com/numpy/numpy)
* [enum](https://pypi.org/project/enum34) `1.1.6 +`
* [typing](https://github.com/python/typing)


### INSTALLATION
1.Download the latest release and unzip the folder where you want to live.
2.Copy folder "toycabinet" into any dir where already set to the **_PYTHONPATH_** env var.


### USAGE
* Set the QT_SIDE_BINDING env-var before running.

```python
import os
os.environ['QT_SIDE_BINDING'] = 'pyside'  # or pyside2
```

* Startup as Standalone
```python
from toycabinet.main import startup
if __name__ == '__main__':
    startup()
```

* Startup in DCC
```python
from toycabinet.main import startup
startup(context='maya')  # maya / houdini / nuke / ...
```

### SHORTCUTS
* Alt + Q `Hide/Show Left Sidebar`
* Alt + W `Hide/Show Hue Filter`
* Alt + D `Show/Hide Inner Tag Filter`
* Alt + F `Query from Database`
* Alt + B `Hide/Show Right Sidebar`
* Alt + (1,2,3,4,5,6) `Auto Fit Size of Toy-Items`
* Space `Play Sequence`
* \` `Hide/Show Toy-Item Label`
* Ctrl + \` `Show Toy-Item Detail Information`
* Alt/Ctrl + LMB(Click) `Show Toy-Item Detail Information`
* Ctrl + MMW(Wheel) `Dynamic Resize Toy-Items`
* Ctrl + (+,-) `Dynamic Resize Toy-Items`


### ATTENTION !
* [**PyQt4 Invalid !**] 
You will always get **Segmentation Fault** if you set QtSide's **_QT_SIDE_BINDING_** env-var to _**pyqt4**_, 
please use **_pyside_** or **_pyside2_** instead.

* [**COMMUNITY vs ENTERPRISE**]
Community License has full features but quantitative restrictions, 
such as can only create _**`2 markets`**_ **_`200 toys`_**.


### RELEASE
[RELEASE INFO](RELEASE.md)


### HAVING ISSUES?
Please send an email with the error message and a detailed step by step process of how you got the error. Comments, 
suggestions and bug reports are welcome.
