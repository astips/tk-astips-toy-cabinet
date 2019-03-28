# tk-astips-toy-cabinet
AssetLib Manager for Animation & VFX Studio.


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
1. Download the latest release and unzip the folder where you want to live.
2. Copy folder "toycabinet" into any dir where already set to the **_PYTHONPATH_** env var.


### USAGE

#### 1. Setup Database Server
* It is strongly recommended to use **_PostgreSQL_**

* Fill the db-information to **_`toycabinet > presets.json`_** file
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
**_`toycabinet > bin > sptc-initdb.bat`_**(windows). If you see messages below means
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
#### 2. Set the QT_SIDE_BINDING env-var before running.
* 
    ```python
    import os
    os.environ['QT_SIDE_BINDING'] = 'pyside'  # or pyside2
    ```

#### 3. Startup ToyCabinet

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
**One Year Trial Community License**  has full features but quantitative restrictions, 
such as can only create _**`2 markets`**_ **_`100 toys`_**.
There's to be no limitation for **Enterprise License**, Cool.


### RELEASE
[RELEASE INFO](RELEASE.md)


### HAVING ISSUES?
Please send an email with the error message and a detailed step by step process of how you got the error. Comments, 
suggestions and bug reports are welcome.
