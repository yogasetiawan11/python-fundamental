# What is venv and Why Do We Use It?

## What is venv?
`venv` stands for **virtual environment** in Python.  
It is a tool that helps you create an isolated space for your Python projects, where you can install packages and dependencies without affecting other projects or the global Python installation.

## Why Do We Use venv?
- **Isolation:** Each project can have its own dependencies, even if different projects need different versions of the same package.
- **No Conflicts:** Avoids version conflicts between packages used in different projects.
- **Easy Management:** You can easily create, activate, and delete environments for different projects.
- **Safe Testing:** Try out new packages or versions without breaking your main Python setup.

Virtual environment will do logical separation on your virtual machine for the Python packages
install virtual environment:
```bash
pip install virtualenv
```

let's say Im working for project x, I need to create a module using this command:
```bash
python -m venv project-x 
```
It will create a new folder ``project-x``. Once you create venv, you can run this command:
Linux:
```bash
source project-x/bin/activate
```
Power shell:
```bash
project-x\Scripts\Activate.ps1
```
you will go inside project-x (virtual environment) file then you can download a Module that you need. for example Jira:
```bash
pip install jira 
```
Jira will install in this virtual environment it won't widespread to another file, so there are no any conflict with other packages.