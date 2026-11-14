# Running Python Programs from the Command Line 



**Yes, you can easily run `calcNatLog.py` directly from the terminal.** Because you are using a virtual environment, you just need to make sure that environment is active so Python can find your installed `mpmath` library.

## Running from PyCharm's built-in Terminal

1. Open the **Terminal** tab at the bottom of PyCharm (`>_`).
2. Check that your prompt starts with `(.venv)` or `(venv)`. PyCharm usually activates this automatically.
3. Type `python calcNatLog.py` and press **Enter**.
4. Any `print()` statements in your script will output directly into the terminal window.

Running from an external terminal (Command Prompt, PowerShell, or Mac Terminal)

If you open a terminal window outside of PyCharm, you have to navigate to your project folder and turn on the virtual environment first.

- **Navigate to your folder.** Use `cd path/to/pymathcalcs` to move into your project directory.
- **<u>Activate the environment (Windows)</u>.** Run `.venv\Scripts\activate` (or `venv\Scripts\activate` depending on your folder name). (**THIS WORKS Only IF you run it from the base directory `pymathcalcs`**: I use: `.venv\Scripts\activate` )
- **Activate the environment (Mac/Linux).** Run `source .venv/bin/activate`.
- **Run the file.** Once you see `(.venv)` appear in your prompt, run `python calcNatLog.py`. (Note: Make sure you are in the right directory)

## Run With **`.venv`**

1. Move to the base directory: **`pymathcalcs`**

2. Run the script: **`.venv\Scripts\activate`**

3. Then move to the appropriate subdirectory: **`cd ./log_2_10`**

4. Then execute the ***python*** Program:

   ```bash
   python log_2_10.py
   ```

   

## Quick Tip

If your script calculates a result without printing it, nothing will appear in the terminal. Make sure your file ends with a `print()` function (for example, `print(mp.log(10))`) so you can see the output on your screen.

Are you passing **numbers directly inside the code**, or do you want to **type numbers into the terminal** each time you run `calcNatLog.py`? I can show you how to accept command-line inputs if you'd like.