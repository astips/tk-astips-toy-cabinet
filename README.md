# Toy Cabinet
Asset Library Manager for Animation & VFX Studio.

`https://github.com/astips/tk-astips-toy-cabinet`

![platform](https://img.shields.io/badge/Platform-(windows)&(linux)-blue.svg)
![python](https://img.shields.io/badge/Python-2.7-blue.svg)
![build](https://img.shields.io/badge/Cython-0.29-blue.svg)
![license](https://img.shields.io/badge/License-MIT-green.svg)
![size](https://img.shields.io/badge/Size-12M-yellow.svg)


### FEATURE
* Database based (PostgreSQL, MySQL, SQLite)
* Tag filter
* Dominant color filter
* User permissions manage-able
* Extendable by client
* Support Windows & Linux
* Support Chinese (Sorting & Filtering)


### DEPENDENCY
* [QtSide](https://github.com/astips/QtSide) _`1.0.2 +`_
* [peewee](https://github.com/coleifer/peewee) _`3.8.2 +`_
* [psycopg2](https://github.com/psycopg/psycopg2) _`for PostgreSQL`_
* [Pillow](https://github.com/python-pillow/Pillow)
* [pypinyin](https://github.com/mozillazg/python-pinyin)
* [enum34](https://pypi.org/project/enum34) _`1.1.6 +`_
* [typing](https://github.com/python/typing)


### INSTALLATION
1. Download the latest release and unzip the folder where you want to live.
2. Copy folder "toycabinet" into any dir where already set to the **_PYTHONPATH_** env var.


### USAGE


#### 1. Setup Database Server
* It is strongly recommended to use **_PostgreSQL_**

* Fill the db-information into **_`toycabinet > presets.json`_** file
    ```json
    {
        "db_type": "postgres",
        "db_info": {
            "database": "toycabinet",
            "host": "127.0.0.1",
            "port": "5432",
            "user": "postgres",
            "password": "postgres"
        },
        "email": "animator.well@gmail.com"
    }
    ```
    _db_type: postgres/mysql/sqlite_

* Init toolkit's db by running **_`toycabinet > bin > sptc-initdb`_**(linux) or 
**_`toycabinet > bin > sptc-initdb.bat`_**(windows). If messages display as below means
    init toolkit's database success.
    ```
    DB-CONNECT:  
        SUCCESS
    DB-CONNECTION: 
        <connection object at 0x7f14e1393050; dsn: 'user=postgres host=127.0.0.1 password=xxx port=5432 dbname=toycabinet', closed: 0>
    DB-CREATE-TABLES:  
        SUCCESS
    DB-TABLES:
        authentication
        cabinets
        markets
        tag_groups
        tag_tag_group_connections
        tag_toy_connections
        tags
        toys
        users
    DB-CREATE-ADMIN-USER:  SUCCESS
    DB-USER-ADMIN:
        Name: admin
        Password: 123456
    
    DB-INIT: DONE!
    ```


#### 2. Startup ToyCabinet

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

* Default Admin Account _`you can change the password whenever you want`_
    ```text
    Name: admin
    Password: 123456
    ```
    
    
#### 3. Client Options `make opts to fit your pipeline`

* Folder option _`toycabinet > opt > folder.py`_

    ```python    
    def before_folder_option(location):
        """location: folder full path"""
        # do something, return True or False
        pass
    
  
    def after_folder_option(location):
        """location: folder full path"""
        # do something, return True or False
        pass
    
    
    def retire_folder(location, new_name):
        """
        location: folder full path
        new_name: new folder name (not path, just a name string)
        """
        # do something, return True or False
        pass
    ```

    _example:_
    ```python
    import os
    from my_office import rpc  # my_office is a fake module ~ ~
    
  
    def before_folder_option(location):
        if not os.path.exists(location):
            rpc.create_folder(location)
        rpc.chmod(location, '777', recursive=True)  # change mode by rpc
        return True
    
    
    def after_folder_option(location):
        rpc.chown(location, 'ple:ple', recursive=True) # change owner by rpc
        rpc.chmod(location, '755', recursive=True)  # change mode by rpc
        return True
    
    
    def retire_folder(location, new_name):
        parent_folder = os.path.dirname(location)
        rpc.rename_folder(location, os.path.join(parent_folder, new_name))
        return True
    ```

* Data option _`toycabinet > opt > data.py`_
    ```python
    def archive_database():
        """Archive Database"""
        # do something
        return True
    ```

    _example:_
    
    ```python
    import os
    from my_office import rpc  # my_office is a fake module ~ ~
    
    def archive_database():
        rpc.toy_cabinet_db_archive()
        return True
    ```

### SHORTCUTS
* Alt + Q _`Hide/Show Left Sidebar`_
* Alt + W _`Hide/Show Right Sidebar`_
* Alt + E _`Show/Hide Inner Tag Filter`_
* Alt + R _`Hide/Show Hue Filter`_
* Alt + T _`Show/Hide Creator`_
* Alt + F _`Query from Database`_
* Alt + D _`Show Toy-Item Detail Information`_
* Alt + (1,2,3,4,5,6) _`Auto Fit Size of Toy-Items`_
* Alt/Ctrl + LMB(Click) _`Show Toy-Item Detail Information`_
* Ctrl + MMW(Wheel) _`Dynamic Resize Toy-Items`_
* Ctrl + (+,-) _`Dynamic Resize Toy-Items`_
* Ctrl + A _`Switch Aspect-Ratio of Toy-Items`_
* \` _`Hide/Show Toy-Item Label`_
* Space _`Play Sequence`_


### ATTENTION!
* **[ PyQt4 Invalid ]** 
You will always get **Segmentation Fault** if you set QtSide's _QT_SIDE_BINDING_ env-var to _pyqt4_, 
please use _pyside_ or _pyside2_ instead.

* **[ COMMUNITY vs ENTERPRISE ]**
**One Year Trial Community License**  has full features but quantitative restrictions, 
such as can only create _**`2 markets`**_ **_`100 toys`_**.
There's to be no limitation for **Enterprise License**, Cool.
Email to get the Enterprise License.


### RELEASE
[RELEASE INFO](RELEASE.md)


### ISSUES?
Please send an email with the error message and a detailed step by step process of how you got the error. Comments, 
suggestions and bug reports are welcome.
