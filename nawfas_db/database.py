# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 9/14/2019
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import codecs
import json
import uuid


def doc_path_builder(base_dir_path, doc_name):
    return f"{base_dir_path}\{doc_name}.json"


class Database:
    def __init__(self, base_dir_loc, docs):
        self.base_dir_loc = base_dir_loc
        self.docs = docs
        doc_paths = dict()
        for doc in self.docs:
            doc_path = doc_path_builder(self.base_dir_loc, doc)
            doc_paths[str(doc)] = doc_path

            # First Look if we have existing Database Docs
            try:
                with codecs.open(doc_path, "r", "utf-8") as file_reader:
                    content = json.load(file_reader)
                    if isinstance(content, dict):
                        print(f"`{doc} exists, Already")
                        continue
            except:

                try:
                    with codecs.open(doc_path, "w", "utf-8") as file_writer:
                        json.dump(dict(), file_writer, ensure_ascii=False, indent=1)
                        print(f"Empty `{doc}` is Created")
                except Exception as e:
                    raise Exception(f"Error: {e}")

        self.docs_path = doc_paths

    def _load_doc(self, doc_name):
        try:
            print("In _load_doc")
            with codecs.open(self.docs_path[doc_name], "r", "utf-8") as file_reader:
                content = json.load(file_reader)
                return content
        except Exception as e:
            raise Exception(f"Error: {e}")

    def _dump_doc(self, content, doc_name):
        try:
            with codecs.open(self.docs_path[doc_name], "w", "utf-8") as file_writer:
                json.dump(content, file_writer, ensure_ascii=False, indent=1)
                print("dumped Success")

        except:
            print("Error In Dumping")
            raise Exception("Can't Update Document")

    def insert(self, doc_name, val, key=None):
        if key:
            key = key
        else:
            key = f"{uuid.uuid4()}"
        content = self._load_doc(doc_name)

        if key not in content.keys():
            content[key] = val
            self._dump_doc(content, doc_name)
        else:
            raise Exception("Duplicate Key")

    def update(self, doc_name, val, key):
        content = self._load_doc(doc_name)
        if key not in content.keys():
            raise Exception("No key Found")
        else:
            content[key] = val
            self._dump_doc(content, doc_name)

    def get(self, doc_name, key):
        content = self._load_doc(doc_name)
        if key not in content.keys():
            raise Exception("No key Found")
        else:
            return content[key]

    def delete(self, doc_name, key):
        content = self._load_doc(doc_name)
        if key not in content.keys():
            raise Exception("No key Found")
        else:
            content[key] = None
            self._dump_doc(content, doc_name)
