# iiED Enrollment Dashboard

This is an internal data dashboard built for the Institute for Innovation & Economic Development (iiED) to visualize and explore Excel-based enrollment and demographic data.

## Features

- Upload `.xlsx` Excel files and view data interactively
- Filter data by column values
- Visualize using bar, pie, or line charts
- Download filtered data as `.csv` or summaries as `.txt`
- Works completely offline (no internet required)
- Includes styled navigation and responsive layout
- Built with Flask (Python) + Vue.js + Chart.js

---

## Quick Launch

### macOS / Linux

Run from the root folder:

```bash
bash start_dashboard.sh
```

Or if already made executable:

```bash
./start_dashboard.sh
```

### Windows

Double-click:

```
start_dashboard.bat
```

Or launch in terminal:

```cmd
start_dashboard.bat
```

### After Setup
After running either the .sh or .bat file launch the app in your browser:

```
http://127.0.0.1:5423/
```
> From there, use the navigation bar to go to Upload or Dashboard views.

---

## Manual Setup

```bash
# Clone the repo
git clone https://github.com/rriicc00/iied-enrollment-dashboard.git
cd iied-enrollment-dashboard

# Set up virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python backend/app.py
```

---

## Project Structure

```
iied-enrollment-dashboard/
├── backend/
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   └── upload_form.html
│   └── uploads/           # Excel files saved here
├── frontend/
│   └── dashboard.html     # Vue.js chart dashboard
├── lib/
│   ├── vue.js
│   └── chart.js
├── static/
│   └── style.css          # App-wide styling
├── start_dashboard.sh     # For Mac/Linux
├── start_dashboard.bat    # For Windows
├── requirements.txt
└── README.md
```

---

## Notes

- Uploaded files persist in `/uploads/` and are excluded from version control.
- All tools (Vue/Chart.js) are hosted locally — no CDN or internet needed.
- The dashboard supports filtering and live charting from any uploaded file.
- To stop the app, press `CTRL+C` in your terminal.

---

## Optional Improvements

- Add basic authentication (login page or admin access)
- Multi-sheet Excel upload support
- Detect dark mode preference from OS and apply CSS
- Upload history with metadata (timestamp, size)

---