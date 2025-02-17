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
