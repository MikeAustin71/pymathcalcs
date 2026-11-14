

# How to Reinstall Python Libs

I keep a copy of  all libraries required by this project in a file named ***requirements.txt*** located in the project root directory.

If you ever need to reinstall the libraries (a.k.a. modules), run the following command:

```bash

```

# Should You Create a requirements.txt File?

Yes.

For a project that you intend to keep, share, archive, or revisit months from now, I strongly recommend creating a:

```text
requirements.txt
```

file.

The reason is exactly what you just experienced:

- The old virtual environment was deleted.
- All installed packages disappeared.
- You had to rediscover and reinstall the required package (`mpmath`).

A `requirements.txt` file preserves the list of project dependencies so the environment can be recreated quickly.

---

# Simple Approach

If `mpmath` is the only third-party package required by the project, create a file named:

```text
requirements.txt
```

with the contents:

```text
mpmath
```

Then, any future rebuild becomes:

```powershell
pip install -r requirements.txt
```

---

# Preferred Approach

Since the project is now working correctly, let `pip` generate the file for you.

Run:

```powershell
pip freeze > requirements.txt
```

Then inspect the file:

```powershell
Get-Content requirements.txt
```

You will probably see something similar to:

```text
mpmath==1.3.0
```

The advantage is that the exact version number is recorded.

---

# Typical Python Workflow

For most personal projects, I recommend:

1. Create the project.
2. Create `.venv`.
3. Install required packages.
4. Generate `requirements.txt`.

```powershell
pip freeze > requirements.txt
```

5. Commit the source code and `requirements.txt` to Git.

---

# Do NOT Commit .venv

The virtual environment should normally stay out of Git.

Most repositories include a `.gitignore` entry such as:

```text
.venv/
```

This prevents hundreds or thousands of environment files from being uploaded to GitHub.

The files that belong in the repository are typically:

```text
.gitignore
requirements.txt
README.md
*.py
```

The `.venv` directory*should remain local.

---

# Recommendation For This Project

From th* project root directory, run:

```*owershell
pip freeze > requirements.txt
```

Then verify the contents:

```powershell
Get-Content requirements.txt
```

If you see something similar to:

```*ext
mpmath=1.3.0
```

then you're set.

The*next time `.venv` must be rebuilt,*recovery becomes:

```powershell
p* -3.14 -m venv .ven*
```

```powershell
.\.venv\Script*\Activate.ps1
```

```powershell
p*p install -r requirements*txt
```

and your environment will*be restored automatically.

That is considered standard practice for python projects.

