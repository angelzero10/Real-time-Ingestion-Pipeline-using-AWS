
# How to Run architecture/diagram.py in a Virtual Environment

This guide will help you run the Python script `architecture/diagram.py` using a virtual environment to manage dependencies.

## Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of terminal/command line usage.

## Steps to Run the Script

### 1. Navigate to the project directory

Open a terminal and navigate to the directory where `diagram.py` is located. Replace `path/to/architecture` with the actual path:

```bash
cd diagrams
```

### 2. Create a virtual environment

Create a new Python virtual environment inside the project directory:

```bash
python3 -m venv venv
```

This command creates a virtual environment named `venv`.

### 3. Activate the virtual environment

Activate the virtual environment to isolate project dependencies:

- **On macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

- **On Windows**:

  ```bash
  venv\Scripts\activate
  ```

Once activated, you will see `(venv)` in your terminal prompt.

### 4. Install dependencies

Install the necessary Python packages within the virtual environment:

```bash
pip install diagrams
```

This installs the `diagrams` package, which is required by the `diagram.py` script.

### 5. Run the script

Now you can run the `diagram.py` script:

```bash
python diagram.py
```

The output image of the architecture diagram will be saved in the current directory as `Real-time_Ingestion_Pipeline.png`.

### 6. Deactivate the virtual environment

After you are done running the script, you can deactivate the virtual environment by running:

```bash
deactivate
```

This will return you to the global Python environment.

## Notes

- Ensure Python is properly installed and available in your system's PATH.
- If you encounter issues with package installations, ensure `pip` is up-to-date by running:

  ```bash
  python3 -m pip install --upgrade pip
  ```

