# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 9/14/2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""



from nawfas_db import Database

base_dir_loc = "F:\\projektus\\py\\nawfas_db\\examples\\database"

#Sample Docs
docs = ["users", "payment"]

db = Database(base_dir_loc=base_dir_loc, docs=docs)

user = {
    "name": "The Power of Habit",
    "author": "Charles Duhigg",
    "category":"Self Motivation"
}
payment = {
    "user": "sample@data",
    "subcription": 1
}

db.insert(doc_name="payment", val=payment)
for i in range(10):
    try:
        db.insert(doc_name="users", val=user, key="second")
    except:
        db.update("users",user,key="second")
        pass
