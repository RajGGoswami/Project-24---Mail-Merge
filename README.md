# Project-24---Mail-Merge

This project automates the creation of personalized letters using Python, similar to how traditional mail merge works in word processors.

**Project Overview**

The script:

Reads a letter template

Reads a list of names

Replaces a placeholder ([name]) with each real name

Saves each personalized letter as a separate file

**Why this project exists**

This project was built to practice:

Reading and writing files in Python

Working with file paths and directories

String manipulation (replace, strip)

Automating repetitive document creation tasks

Clean, readable scripting for real-world use cases

**What I learned**

How .read() and .readlines() behave differently

Why .strip() is important when handling file input

How to dynamically generate file names

How small scripts can eliminate repetitive manual work

How Python can replicate common office automation tasks

**How the script works (high level)**

Open and read the starting letter template

Open and read all invited names

Loop through each name

Clean the name formatting

Replace [name] placeholder with the actual name

Write a new personalized letter file for each person

**Project File Structure**

├── Input/

│   ├── Letters/

│   │   └── starting_letter.txt

│   └── Names/

│       └── invited_names.txt

│

├── Output/

│   └── ReadyToSend/

│       ├── letter_for_Alice

│       ├── letter_for_Bob

│       └── ...

│

├── main.py

**Design Notes**

Placeholder-based replacement keeps the template reusable

File naming ensures each letter is uniquely identifiable

Logic is linear and easy to extend (email, PDFs, etc.)

Script is intentionally simple and readable
