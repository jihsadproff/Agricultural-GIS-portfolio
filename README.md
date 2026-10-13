# Agricultural-GIS-portfolio
Spatial Python pipeline and time-series NDVI crop health monitoring over farm fields in Kwara State, Nigeria.

PROJECT 1:MULTI CRITERIA LAND SUITABILITY EVALUATION MATRIX

--THE PROBLEM: Agribusinesses require automated terrain auditing to locate optimal crop expansion zones and minimize machinery/erosion risks before purchasing land.

--THE SOLUTION: Developed a pure Python script using 'rasterio' and 'NumPy' to ingest Digital Elevation Models (DEMs). Built a structural matrix convolution using coordinate gradient steps ('np.gradient') and trigonometric algorithms ('np.arctan') to calculate slopes in degrees across millions of pixels.

--THE MECHANISM: Applied binary array masking logic ('slope > 15') to instantly map agricultural exclusion fields. Used boolean vector mathematical mean functions ('np.mean`) to output macro-level landscape statistics.


PROJECT 2: AUTOMATED Climate CLIMATE  RISK AND DROUGHT MONITORING ENGINE
  
--THE PROBLEM : Crop insurance firms and NGOs require swift macro-level climate auditing to identify historical weather anomalies and trigger index-based financial payouts.

--THE SOLUTION: Built a Python processing script using 'Pandas' to intake multi-decade localized rainfall matrices across Kwara State.

--THE GIS MECHANISM: Applied advanced aggregation logic ('.groupby()' and '.transform("mean")') to establish localized climate benchmarks. Programmed the standard Rainfall Anomaly Index (RAI) vector formula to isolate extreme drought years where data values dropped below critical thresholds.
