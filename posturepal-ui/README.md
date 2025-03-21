# PosturePal UI

PosturePal UI is a user interface for the PosturePal application, designed to help users maintain good posture while working or studying. This project provides a graphical interface that interacts with the posture detection backend, allowing users to visualize their posture data and configure application settings.

## Project Structure

```
posturepal-ui
├── src
│   ├── main.py                # Entry point of the application
│   ├── ui                     # Contains UI components and logic
│   │   ├── __init__.py        # Marks the ui directory as a package
│   │   ├── app.py             # Main application logic for the UI
│   │   ├── components          # Contains UI components
│   │   │   ├── __init__.py     # Marks the components directory as a package
│   │   │   ├── dashboard.py    # Dashboard component for displaying posture data
│   │   │   └── settings.py     # Settings component for configuring application options
│   │   └── styles              # Contains CSS styles for the UI
│   │       └── style.css       # Styles for UI components
│   ├── services                # Contains services for posture detection
│   │   ├── __init__.py         # Marks the services directory as a package
│   │   └── posture_service.py   # Logic for interacting with the posture detection backend
│   └── assets                  # Contains assets used in the UI
│       └── fonts               # Font files used in the UI
├── requirements.txt            # Lists project dependencies
├── README.md                   # Documentation for the project
└── .gitignore                  # Specifies files to ignore by version control
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd posturepal-ui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will start the PosturePal UI, allowing you to monitor your posture and adjust settings as needed.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.