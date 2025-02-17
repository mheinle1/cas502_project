def generate_html(kml_file, output_html='index.html'):
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leaflet KML Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet-omnivore/0.3.4/leaflet-omnivore.min.js"></script>
    <style>
        #map {{ height: 600px; }}
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        var map = L.map('map').setView([37.7749, -122.4194], 10);
        L.tileLayer('https://tile.openstreetmap.org/{{zoom}}/{{x}}/{{y}}.png', {{
            attribution: '&copy; OpenStreetMap contributors'
        }}).addTo(map);
        var kmlLayer = omnivore.kml('{{kml_file}}').on('ready', function() {{
            map.fitBounds(kmlLayer.getBounds());
        }}).addTo(map);
    </script>
</body>
</html>'''
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"HTML file generated: {output_html}")
