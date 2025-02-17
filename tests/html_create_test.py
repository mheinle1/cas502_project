import unittest
import os

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


class TestGenerateHtml(unittest.TestCase):

    def test_html_file_creation(self):
        # Call the function
        generate_html('valid.kml', 'output.html')
        
        # Assert the file is created
        self.assertTrue(os.path.exists('output.html'))
        
        # Cleanup
        os.remove('output.html')

    def test_html_structure(self):
        # Generate HTML
        generate_html('valid.kml', 'output.html')
        
        # Read the file and check if key content is present
        with open('output.html', 'r') as file:
            html_content = file.read()        
        # Simple checks for key elements
        self.assertIn('<div id="map"></div>', html_content)
        self.assertIn('leaflet.js', html_content)
        
        # Cleanup
        os.remove('output.html')

    def test_custom_output_file_name(self):
        kml_file = 'valid.kml'
        custom_output_html = 'custom_output.html'
        
        # Call the function with a custom output file name
        generate_html(kml_file, custom_output_html)
        
        # Check if the custom HTML file was created
        self.assertTrue(os.path.exists(custom_output_html))
        
        # Cleanup after the test
        if os.path.exists(custom_output_html):
            os.remove(custom_output_html)

if __name__ == '__main__':
    unittest.main()
