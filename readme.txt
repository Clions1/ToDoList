
Task Manager Application - Documentation

Overview:
This Python script creates a simple Task Manager application using the tkinter library. The user can add tasks to a list, which are displayed as checkboxes. The user can mark tasks as completed by selecting the checkboxes, and then click a "Complete" button to remove the checked tasks from the list.

Prerequisites:
- Python 3.x installed on your system.
- tkinter library (usually comes pre-installed with Python).

Features:
- Add tasks (up to a maximum of 10 tasks).
- Tasks are displayed as checkboxes.
- Tasks can be marked as complete by checking the box.
- Completed tasks can be removed by clicking the "Complete" button.

Code Breakdown:

1. Setting Up the Main Window:

```python
window = tk.Tk()
window.geometry("500x400")
window.resizable(False, False)
```
- `tk.Tk()` creates the main window of the application.
- `window.geometry("500x400")` sets the size of the window to 500x400 pixels.
- `window.resizable(False, False)` prevents the user from resizing the window.
