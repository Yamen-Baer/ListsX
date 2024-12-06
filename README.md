# List Manager - Futuristic UI

A Python desktop application for managing text-based lists. The application features a modern, futuristic user interface and provides functionality for cleaning lists and performing actions like shuffling list items. 

## Features

- **List Cleaner**: Remove items from one list that exist in another.
- **Actions**: Perform various actions on lists, starting with shuffling the list.
- **File Selection**: Easily select input files through a graphical user interface (GUI).
- **Save Output**: Choose where to save the processed or shuffled list files.
- **User-Friendly Design**: A sleek, modern UI with intuitive navigation between sections.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Yamen-Baer/ListsX.git
    ```
2. Navigate to the project directory:
    ```bash
    cd listsX
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

## Usage

### Main Menu
From the Main Menu, choose:
- **List Cleaner**: To clean lists by removing overlapping items.
- **Actions**: To perform actions like shuffling.

### List Cleaner
1. Select the file to clean using the **Select List To Clear** button.
2. Select the base file to compare against using the **Select The Base List** button.
3. Click **Process** to create a cleaned list, and choose where to save the output.

### Actions
1. Select the list file using the **Select List** button.
2. Click **Shuffle** to randomize the order of the list items, and choose where to save the shuffled file.

## Requirements

- Python 3.7+
- Tkinter (included with standard Python installation)
- Pillow (for image support)
    ```bash
    pip install pillow
    ```

## Development

### File Structure
```
listsX/
│
├── main.py                # Main application script
├── requirements.txt       # Python dependencies
└── assets/
    ├── listsX.ico   # Icon for the program
    ├── listsX.png   # PNG for the program
    └── (additional assets, e.g., images)
```

### Contributing
Feel free to fork the repository and create pull requests for:
- Adding new actions.
- Improving the UI.
- Enhancing functionality.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI framework.
- [Pillow](https://python-pillow.org/) for image support.
