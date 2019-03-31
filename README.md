# tk-astips-toy-cabinet
AssetLib Manager for Animation & VFX Studio.


### FEATURE
* Database based (Postgresql/MySql/Sqlite)
* Tag filter
* Dominant color filter
* Manage user permission by admin
* Extendable by client
* Supports Windows, Linux
* Support Chinese(include sort & filter)


### DEPENDENCY
* [QtSide](https://github.com/astips/QtSide) _`1.0.2 +`_
* [peewee](https://github.com/coleifer/peewee) _`3.8.2 +`_
* [psycopg2](https://github.com/psycopg/psycopg2) _`for PostgreSql-DB`_
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
    
    
#### 3. Client Opts `make opts to fit your pipeline`

* **Folder option** _`toycabinet > opt > folder.py`_

    ```python    
    def before_toy_folder_option(toy_location):
        """do something, return True or False"""
        pass
    
  
    def after_toy_folder_option(toy_location):
        """do something, return True or False"""
        pass
    ```

    For example:
    ```python
    import os
    from my_office import rpc  # my_office is a fake module ~ ~
    
    def before_toy_folder_option(toy_location):
        if not os.path.exists(toy_location):
            rpc.create_folder(toy_location)  # Create folder by RPC
        rpc.chmod(toy_location, '777', recursive=True)   # Change permission mode by RPC
        return True
    
    
    def after_toy_folder_option(toy_location):
        rpc.chown(toy_location, 'ple:ple', recursive=True)  # Change owner by RPC
        rpc.chmod(toy_location, '755', recursive=True)  # Change permission mode by RPC
        return True
    ```
    
### SHORTCUTS
* Alt + Q _`Hide/Show Left Sidebar`_
* Alt + W _`Hide/Show Hue Filter`_
* Alt + D _`Show/Hide Inner Tag Filter`_
* Alt + F _`Query from Database`_
* Alt + B _`Hide/Show Right Sidebar`_
* Alt + T _`SHow/Hide Creator`_
* Alt + (1,2,3,4,5,6) _`Auto Fit Size of Toy-Items`_
* Space _`Play Sequence`_
* \` _`Hide/Show Toy-Item Label`_
* Ctrl + \` _`Show Toy-Item Detail Information`_
* Alt/Ctrl + LMB(Click) _`Show Toy-Item Detail Information`_
* Ctrl + MMW(Wheel) _`Dynamic Resize Toy-Items`_
* Ctrl + (+,-) _`Dynamic Resize Toy-Items`_


### ATTENTION!
* **[ PyQt4 Invalid ]** 
You will always get **Segmentation Fault** if you set QtSide's _QT_SIDE_BINDING_ env-var to _pyqt4_, 
please use _pyside_ or _pyside2_ instead.

* **[ COMMUNITY vs ENTERPRISE ]**
**One Year Trial Community License**  has full features but quantitative restrictions, 
such as can only create _**`2 markets`**_ **_`100 toys`_**.
There's to be no limitation for **Enterprise License**, Cool.


### RELEASE
[RELEASE INFO](RELEASE.md)


### ISSUES?
Please send an email with the error message and a detailed step by step process of how you got the error. Comments, 
suggestions and bug reports are welcome.
