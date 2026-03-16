# Python Projects Collection

> A collection of **beginner-friendly Python projects** designed to practice programming, build useful utilities, and create simple interactive applications.

DEMO: 2026-03-16 16-46-24.mp4 (in files)

<video src="./2026-03-16 16-46-24.mp4" controls></video>

This repository contains multiple **standalone Python applications** including productivity tools, games, finance trackers, and utility programs. Each project can run independently from the command line and demonstrates core Python concepts such as:

- File handling
- JSON data storage
- Modular programming
- Command-line interfaces
- Basic data management

These projects are great for **learning Python, practicing coding skills, or expanding into larger applications.**

---

# Projects Included

## Task Manager (`main.py`)
A command-line task management system.

**Features**
- Add tasks
- Delete tasks
- Mark tasks as completed
- View tasks with filters

---

## Music Manager (`musicmanager.py`)
Manage and explore a music collection.

**Features**
- Add songs
- Search songs by artist
- Display the longest songs in the collection

---

## Dungeon Game (`dungeon_game.py`)
A simple **text-based adventure game**.

**Features**
- Explore locations
- Fight enemies
- Visit shops
- Manage player stats and inventory

---

## Library System (`biblioteca.py`)
A small library management system.

**Features**
- Add books
- Borrow books
- Return books
- Search books

---

## Pay Tracker (`PayTracker.py`)
A personal finance tracking tool.

**Features**
- Record income
- Record expenses
- Calculate current balance

---

## Fitness App (`fitness_app.py`)
Track your personal fitness progress.

**Features**
- Workout tracking
- Meal logging
- Daily nutrition tracking
- Profile and statistics

---

## Image Manager (`Imagemanager.py`)
An image processing tool built using **Pillow**.

**Features**
- Load images
- Resize images
- Convert images to grayscale
- Crop images
- Store editing history

---

## LifeOS
A **life management system** combining multiple productivity modules.

**Modules**
- Task Management
- Habit Tracking
- Goal Tracking
- Finance Tracking
- Life Score Calculation

---

# Data Files

The applications store persistent data using **JSON files**.

| File | Purpose |
|-----|--------|
| `tasks.json` | Stores tasks for the Task Manager |
| `data.json` | Financial data for PayTracker and LifeOS |
| `biblioteca_data.json` | Library books and user data |
| `fitness_data.json` | Fitness profiles, workouts, and meals |

---

# Requirements

- **Python 3.x**
- **Pillow** (only required for `Imagemanager.py`)

Install Pillow:

```bash
pip install pillow
```

No other external dependencies are required.

---

# Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/python-projects-collection.git
```

2. Navigate into the folder:

```bash
cd python-projects-collection
```

3. Install Pillow (optional):

```bash
pip install pillow
```

---

# Running the Applications

Each project can be executed directly from the command line.

Examples:

```bash
python main.py
python dungeon_game.py
python PayTracker.py
python fitness_app.py
```

To run **LifeOS**:

```bash
python LifeOS/main.py
```

---

# Example Usage

Once launched, each program will display a **menu interface**.

Example actions include:

-  Adding tasks
-  Recording expenses
-  Logging workouts
-  Managing books
-  Playing the dungeon adventure game

Follow the **on-screen instructions** in each program.

---

# Project Structure

```
.
├── main.py                 # Task Manager
├── musicmanager.py         # Music Manager
├── dungeon_game.py         # Dungeon Game
├── biblioteca.py           # Library System
├── PayTracker.py           # Pay Tracker
├── fitness_app.py          # Fitness App
├── Imagemanager.py         # Image Manager
├── tasks.json              # Task data
├── data.json               # Financial data
├── biblioteca_data.json    # Library data
├── README.md               # Project documentation
│
├── LifeOS/
│   ├── main.py             # LifeOS main menu
│   ├── tasks.py            # Task module
│   ├── life_score.py       # Life score calculation
│   ├── habits.py           # Habits module
│   ├── finance.py          # Finance module
│   ├── goals.py            # Goals module
│   └── database.py         # Shared database functions
│
└── __pycache__/            # Python cache files (can be ignored)
```

---

# Learning Goals

This project collection helps practice:

- Python fundamentals
- File persistence with JSON
- Command-line application design
- Modular project structure
- Simple game logic
- Basic data processing

---

# Contributing

Contributions are welcome!

You can help by:

- Adding new Python mini-projects
- Improving existing scripts
- Fixing bugs
- Enhancing documentation

---

# License

This project is open source and available under the **MIT License**.

---

If you find this repository useful, consider **starring it on GitHub!**
