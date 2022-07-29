# **Snake**

**Snake Game written in [Python](https://www.python.org) built using [Pygame](https://www.pygame.org/news).**

The player controls a long, thin creature, resembling a snake, which roams around on a bordered plane, picking up food, trying to avoid hitting its own tail or the edges of the playing area. Each time the snake eats a piece of food, its tail grows longer, making the game increasingly difficult.

----
## **Requirements**

- [Python 3.10.5](https://www.python.org/downloads/release/python-3105/)
- [Pygame 2.1.2](https://www.pygame.org/news)
----
## **Installation**

Snake can be installed via [Pip](https://pypi.org/project/pip/). To start, clone the repository to your local computer and change into the proper directory.

* **Clone Repository**
```bash
  $ git clone https://github.com/niel-conradie/Snake.git
  $ cd Snake
```
### **Pip Install**

* **Create Environment**
```bash
  $ python -m venv .venv
```
* **Activate Environment**
```bash
  # Bash
  $ source .venv/Scripts/activate

  # Command Prompt
  C:> .venv\Scripts\activate.bat

  # macOS
  $ .venv/bin/activate

  # PowerShell
  PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  PS C:> .venv\Scripts\Activate.ps1
```
* **Install Requirements**
```bash
  (.venv) $ python -m pip install -r requirements.txt
```
----
## **Usage**

To launch the Snake Game use thus file.
```bash
  run.py
```
----
## **License**

[MIT License](https://github.com/niel-conradie/Snake/blob/master/LICENSE)

----