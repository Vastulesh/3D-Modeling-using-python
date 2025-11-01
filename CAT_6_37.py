import os
import webbrowser
import cadquery as cq
from cadquery import exporters
import http.server
import socketserver
import threading
import trimesh

# --- Parameters ---
radius_hole = 25
distance = 60
thickness = 10
outer_offset = 10

hole_centers = [(-distance, 0), (0, 0), (distance, 0)]

# --- Compute outer plate size ---
half_length = distance + radius_hole + outer_offset
half_width = radius_hole + outer_offset

# --- Create outer plate ---
plate = (
    cq.Workplane("XY")
    .rect(2 * half_length, 2 * half_width)
    .extrude(thickness)
)

# --- Cut three circular holes ---
for x, y in hole_centers:
    plate = plate.cut(
        cq.Workplane("XY").center(x, y).circle(radius_hole).extrude(thickness)
    )

# --- Export to STL ---
stl_path = os.path.join(os.getcwd(), "three_hole_link.stl")
exporters.export(plate, stl_path)
print("✅ STL export complete:", stl_path)

# --- Convert STL → GLB using trimesh ---
glb_path = os.path.join(os.getcwd(), "three_hole_link.glb")

mesh = trimesh.load_mesh(stl_path)
mesh.export(glb_path)
print("✅ Converted STL → GLB:", glb_path)

# --- Create HTML viewer for GLB ---
html_code = f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>3D Model Viewer</title>
    <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    <style>
      body {{
        margin: 0;
        background-color: #111;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
      }}
      model-viewer {{
        width: 90vw;
        height: 90vh;
      }}
    </style>
  </head>
  <body>
    <model-viewer src="three_hole_link.glb"
      camera-controls
      auto-rotate
      rotation-per-second="15deg"
      background-color="#111">
    </model-viewer>
  </body>
</html>
"""

html_path = os.path.join(os.getcwd(), "three_hole_link.html")
with open(html_path, "w") as f:
    f.write(html_code)

print("HTML viewer created:", html_path)

# --- Start local server ---
def start_server():
    with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as httpd:
        print("Serving at http://localhost:8000/")
        httpd.serve_forever()

thread = threading.Thread(target=start_server, daemon=True)
thread.start()

# --- Automatically open browser ---
webbrowser.open("http://localhost:8000/three_hole_link.html")

input("Press Enter to stop the local server...\n")
