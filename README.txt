# 🧱 3D Plate with Holes — CadQuery + Trimesh + Local HTML Viewer

This project creates a simple **3D metal plate with three circular holes**, exports it as **STL**, converts it to **GLB**, and launches a **local 3D viewer** using `<model-viewer>` in your browser.  
Built with Python, CadQuery, and Trimesh.

---

## ⚙️ Prerequisites

You must have:
- **Python 3.10 or newer**
- **pip** (comes with Python)
- **Internet connection** (for model-viewer)
- **Chrome, Edge, or Firefox** browser

---

## 🧩 Installation & Setup

Copy and paste the following commands in your terminal (CMD, PowerShell, or VS Code terminal):

```bash
# STEP 1 — Install Python (if not installed)
# Download from: https://www.python.org/downloads/
# ✅ During installation: CHECK the box “Add Python to PATH”

# STEP 2 — Open terminal in your project folder

# STEP 3 — Install all required libraries
pip install cadquery trimesh numpy shapely Rtree

# STEP 4 — (Optional, only if errors occur)
pip install scipy pythreejs

# STEP 5 — Save the provided Python code as "three_hole_link.py"

# STEP 6 — Run the script
python three_hole_link.py

# It will automatically:
#   ✅ Create an STL file: three_hole_link.stl
#   ✅ Convert STL → GLB: three_hole_link.glb
#   ✅ Generate HTML viewer: three_hole_link.html
#   ✅ Start a local web server: http://localhost:8000/
#   ✅ Auto-open the 3D model in your browser

# STEP 7 — When done, return to the terminal and press Enter to stop the server.
\