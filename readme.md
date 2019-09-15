## nawfas_db
    Yet another Toy NoSQL-ish Database in Pure Python.
    
### Why "nawfas_db"?
    1. I know it is easier to use SQLite for test case and sometime for Production,
        But I wanted to re-invent the wheel.
    2. Simple yet powerful implementation of Python Dictionary is all I wanted to try.
    3. Key-value storing gives a lot more flexibility while writing mock servers ( I was in the middle of building One).
    4. It's always fun to try out something new in an hour.
### How to install
 It is in pure Python so no extra batteries are needed.
First clone this repository.
    
``` python
    git clone <this_proect_repo>
    
```
Go to the project root directory and type

```python
python setup.py install
```
#### Or You can simply use pip

``` python
pip install git+https://github.com/sabbiramin113008/nawfas_db.git

```

The package should be installed on your system.

### How to Use
As while I am writing, I used to try with Full directory path for Database file discovery.
It means if you are using windows, you have to provide the full directory path in the parameter. 

First import the module in your script.

```python
from nawfas_db import Database
```
Now choose the directory where you want to put the Database document.
Also you need to provide the list of the documents (similar to Tables int RDBMS universe).

```python
base_dir_loc = "<some_directory>" #"F:\\py\\examples\\database"
docs = ["users","payment"]

```
Now initialize the Database Object.

```python
db = Database(base_dir_loc=base_dir_loc, docs=docs)
```
Insert a record, but before that let's prepare our user and payment docs.

```python
user = {
    "name": "The Power of Habit",
    "author": "Charles Duhigg",
    "category":"Self Motivation"
}
payment = {
    "user": "sample_user_id",
    "subcription": 1
}
```

Now Insert into the docs
```python
#insert a Payment type Doc
db.insert(doc_name="payment", val=payment)
```
Again 
```python
#Insert a User Type Doc
for i in range(10):
    try:
        db.insert(doc_name="users", val=user, key="second")
    except:
        db.update("users",user,key="second")
        pass
```
Also for getting a Record, 
```python
print(db.get(doc_name="users", key="first"))

```

But for all records
```python
print (db.get_all(doc_name="users"))
```
For insert operation "key" is not mandatory as uuid is used, 
but for the key. For the update and Get operation, a key must be provided. 

It should work on Linux or MacOS too. But I didn't get time to test it, honestly.
