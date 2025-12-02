# Python venv (Virtual Environment)

## What is venv?
`venv` is a tool in Python that creates an isolated environment for each project.  
Every project gets its own Python interpreter, its own pip, and its own packages.

## Why do we use venv?
- Avoids package conflicts between projects  
- Each project can have different versions of libraries  
- Keeps the system Python clean  
- Industry standard for professional development  
- Makes deployments and debugging easier  

## How venv works (Simple Explanation)
When you create a venv:
- Python copies the interpreter into a new folder (`env/`)
- Creates a dedicated `pip`
- Creates its own package storage (`site-packages`)
- Any package you install stays inside this folder only

## Commands

### Create a virtual environment
```
python3 -m venv env
```
### Activate environment
**macOS / Linux**
```
source env/bin/activate
```
### Install packages inside venv
```
pip install <package-name>
```
### Freeze installed packages
```
pip freeze > requirements.txt
```
### Install from requirements.txt
```
pip install -r requirements.txt
```
### Deactivate venv
```
deactivate
```
