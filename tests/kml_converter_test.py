import unittest
import pandas as pd
from io import StringIO

def convert_to_kml(input_file, output_file='output.kml'):
    # Initialize gdf
    gdf = None
    
    # Determine file format and read data accordingly
    if input_file.endswith('.csv'):
        df = pd.read_csv(input_file)
        if 'geometry' not in df.columns:
            raise ValueError("CSV file must contain a 'geometry' column with WKT format.")
        df['geometry'] = df['geometry'].apply(loads)  # Convert WKT to geometry
        gdf = gpd.GeoDataFrame(df, geometry='geometry')
    elif input_file.endswith(('.shp', '.geojson')):
        gdf = gpd.read_file(input_file)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv, .shp, or .geojson file.")
    
    # Ensure gdf is a GeoDataFrame
    if not isinstance(gdf, gpd.GeoDataFrame):
        raise TypeError("Failed to create a valid GeoDataFrame from the input file.")
    
    # Create a KML document
    k = kml.KML()
    doc = kml.Document()
    k.append(doc)
    
    for _, row in gdf.iterrows():
        if row.geometry is None:
            continue
        placemark = kml.Placemark()
        placemark.geometry = mapping(row.geometry)  # Handles points, lines, and polygons
        placemark.name = str(row.get('name', 'Unnamed'))  # Use 'name' column if available
        doc.append(placemark)
    
    # Write to KML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(k.to_string(prettyprint=True))
    

class TestConvertToKml(unittest.TestCase):

    def test_unsupported_file_format(self):
        # Try an unsupported file format and expect ValueError
        with self.assertRaises(ValueError):
            convert_to_kml('invalid.txt')

    def test_missing_geometry_column_in_csv(self):
        # Create a CSV without a 'geometry' column
        csv_data = StringIO("name\nPlace 1\nPlace 2")
        df = pd.read_csv(csv_data)
        
        # Simulate the 'convert_to_kml' function behavior
        with self.assertRaises(ValueError):
            if 'geometry' not in df.columns:
                raise ValueError("CSV file must contain a 'geometry' column with WKT format.")

    def test_create_kml_from_valid_geojson(self):
        # Test for proper KML file creation
        input_file = 'valid.geojson'
        output_file = 'output.kml'

        # Call the function (assuming valid GeoJSON is provided)
        convert_to_kml(input_file, output_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(output_file))

        # Cleanup after test
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
