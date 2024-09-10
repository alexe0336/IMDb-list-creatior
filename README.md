# IMDb List Creator

This Python script automates the process of creating an IMDb list, eliminating the need to manually add hundreds of movies or TV shows.

## Prerequisites

Before running this script, ensure you have the following:

- An IMDb account
- A comma-separated list of movie or TV show titles
- Python 3.0 or later
- Selenium
- ChromeDriver

## Installation

### Python 3.0

Download and install Python 3.0 or later from [python.org](https://www.python.org/downloads/).

### Selenium

Install Selenium using pip:

```bash
pip install selenium
```

### ChromeDriver

- Download the appropriate version of for your version of Chrome. https://googlechromelabs.github.io/chrome-for-testing/#stable
- Ensure the ChromeDriver executable is in your system's PATH.

## Usage

1. **Navigate to the directory containing the script:**

    ```bash
    cd path/to/script/directory
    ```

2. **Run the script:**

    ```bash
    python imdbscript.py
    ```

3. **Wait for the script to complete.** Do not interact with the Chrome web page that opens. The script will automatically close the browser when finished.

4. **Access and modify your IMDb list** on the IMDb website.

## Important Notes

- Make sure you have a stable internet connection while running the script.
- Do not interact with the Chrome window that opens during script execution.
- If you encounter any issues, ensure all prerequisites are correctly installed and up to date.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit a pull request or open an issue.

