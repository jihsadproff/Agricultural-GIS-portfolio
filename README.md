# Agricultural-GIS-portfolio
Spatial Python pipeline and time-series NDVI crop health monitoring over farm fields in Kwara State, Nigeria.

PROJECT 1:MULTI CRITERIA LAND SUITABILITY EVALUATION MATRIX

--THE PROBLEM: Agribusinesses require automated terrain auditing to locate optimal crop expansion zones and minimize machinery/erosion risks before purchasing land.

--THE SOLUTION: Developed a pure Python script using 'rasterio' and 'NumPy' to ingest Digital Elevation Models (DEMs). Built a structural matrix convolution using coordinate gradient steps ('np.gradient') and trigonometric algorithms ('np.arctan') to calculate slopes in degrees across millions of pixels.

--THE MECHANISM: Applied binary array masking logic ('slope > 15') to instantly map agricultural exclusion fields. Used boolean vector mathematical mean functions ('np.mean`) to output macro-level landscape statistics.
