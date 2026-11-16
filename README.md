# My Toolkit - Week 8 Final Project

## What does it do?
My Toolkit is a menu-driven program with 3 tools in one place:
1. Simple Calculator for + - * /
2. To-Do List Manager to add, view and remove tasks
3. Number Explorer to check even/odd, sum, average, biggest and smallest

## How to run it
1. Make sure Python is installed
2. Download toolkit.py
3. Open terminal in that folder
4. Run: python toolkit.py
5. Choose 1, 2, 3 or 4 to quit

## Reflection
The hardest part for me was planning the menu loop so it keeps running until the user quits without crashing. The bug that took longest to fix was when the program crashed if I typed letters instead of numbers, I fixed it by adding try/except. I also had trouble with removing tasks from the list when the task was not there, so I added a check with if task in tasks. I learned how if/elif/else, loops and lists work together in one real program. If I had one more week, I would add a 4th tool for checking grades and also save the to-do list to a file so tasks are not lost when the program closes. This project made me feel more confident to build bigger programs.

## Files
- toolkit_plan.txt - My plan before coding
- toolkit.py - The main program
- README.md - This file