#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect('app.db')
for line in con.iterdump():
    print(line)