# iiED Enrollment Dashboard

This is an internal data dashboard built for the Institute for Innovation & Economic Development (iiED) to visualize and explore Excel-based enrollment and demographic data.

## Features

- Upload `.xlsx` files and view data interactively
- Filter by column values
- Visualize data with bar, pie, and line charts
- Download filtered data and summaries
- Runs entirely offline (no internet needed)
- Built with Flask (Python) + Vue.js + Chart.js

---

## Quick Launch

### macOS / Linux

Run the startup script from the root of the project:

```bash
bash start_dashboard.sh
```

> Or if you've already made it executable:
```bash
./start_dashboard.sh
```

### Windows

Just double-click `start_dashboard.bat`  
Or run it from terminal like this:

```bat
start_dashboard.bat
```

Once the app launches, visit:

```
http://127.0.0.1:5423/dashboard
```

> The home and upload form are also available at:
> - `/` for API status
> - `/upload_form` to upload Excel files

---

## Manual Setup (Advanced / Devs)

If you prefer to set things up yourself:

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# Set up virtual environment
python3 -m venv venv

# macOS / Linux
source venv/bin/activate  

# Windows
  venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python backend/app.py
```

---

## Project Structure

```
Service Learning Project/
├── backend/
│   ├── app.py
│   ├── templates/
│   └── uploads/
├── frontend/
│   └── dashboard.html
├── lib/
│   ├── vue.js
│   └── chart.js
├── static/
│   └── style.css
├── start_dashboard.sh
├── start_dashboard.bat
├── requirements.txt
└── README.md
```

---

## Notes

- Uploaded Excel files are stored in `/uploads` (excluded from Git).
- The app works offline by locally serving Vue and Chart.js.
- You can use `CTRL+C` in the terminal to stop the server.

---

## Optional Improvements

- [ ] Add authentication (basic login or password)
- [ ] Add multi-sheet Excel support
- [ ] Automatically summarize top categories on upload
