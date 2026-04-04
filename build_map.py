import folium

# Initialize a dark-themed world map
m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter", control_scale=True)

# Define locations and their popup HTML
locations = [
    {"name": "Chennai", "lat": 13.0827, "lon": 80.2707, "img": "assets/img/chennai.jpg"},
    {"name": "Melbourne", "lat": -37.8136, "lon": 144.9631, "img": "assets/img/melbourne.jpg"},
    {"name": "Bangkok", "lat": 13.7563, "lon": 100.5018, "img": "assets/img/bangkok.jpg"},
    {"name": "Melbourne", "lat": -37.8136, "lon": 144.9631, "img": "assets/img/melbourne.jpg"}
]

# Loop through and add markers
for loc in locations:
    popup_html = f"""
    <div style="width: 200px; font-family: 'Meslo LG L', monospace;">
        <h4 style="color: #bd93f9; margin-bottom: 5px;">{loc['name']}</h4>
        <img src="{loc['img']}" width="100%" style="border-radius: 5px;">
    </div>
    """
    folium.Marker(
        location=[loc['lat'], loc['lon']],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color="purple", icon="info-sign")
    ).add_to(m)

# Extract the map components
m.render()
map_html = m._parent.render() # Calls full HTML string of the map

# Create a wrapper that includes the site's CSS/Nav
full_page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital CV | Ajeet Krishnasamy</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@xz/fonts@1/serve/meslo-lg.min.css">

    <link rel="stylesheet" href="css/main.css">
</head>
<body>

<nav class="top-nav">
    <a href="index.html" style="color: var(--purple);">[ 01. Home ]</a>
    <a href="projects.html" style="color: var(--cyan);">[ 02. Projects ]</a>
    <a href="travel.html" style="color: var(--green);">[ 03. Travel ]</a>
</nav>

<div class="container">
    <div class="breadcrumb">
        ~ / portfolio / <span style="color: var(--pink);">travel.py</span>
    <div class="map-container">
            {map_data}
    </div>
</div>

</body>
</html>
"""

with open("travel.html", "w", encoding="utf-8") as f:
    f.write(full_page_html)