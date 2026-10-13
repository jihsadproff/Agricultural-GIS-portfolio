import numpy as np
import matplotlib.pyplot as plt
import rasterio

def run_land_suitability_analysis(raster_path="land_analysis.tif"):
    """
    Executes a Multi-Criteria Evaluation (MCE) terrain suitability matrix
    that is used to isolate agricultural exclusion zones based on slope incline thresholds.
    """
    print("Initializing Geospatial Terrain Processing Pipeline...")

    # 1. Load the raw DEM data matrix
    try:
        with rasterio.open(raster_path) as src:
            dem_array = src.read(1)
            pixel_size = src.res[0] # Grabs horizontal pixel metric resolution
    except Exception as e:
        print(f"Raster file read error: {e}. Defaulting to structural matrix simulation...")
        y, x = np.ogrid[-3:3:200j, -3:3:200j]
        dem_array = 200 + (np.sin(x) * np.cos(y) * 150) + (np.random.normal(0, 2, (200,200)))
        pixel_size = 30.0 # Standard NASA SRTM 30-meter grid size

    # 2. Compute Topographic Gradients (Rise over Run)
    dy, dx = np.gradient(dem_array, pixel_size)

    # 3. Calculate Landscape Slope Magnitude in Degrees
    slope_radians = np.arctan(np.sqrt(dx**2 + dy**2))
    slope_degrees = np.degrees(slope_radians)

    # 4. Generate Binary Mask for Unsuitable Land (> 15 Degrees)
    unsuitable_mask = slope_degrees > 15

    # 5. Compute Statistical Proportions
    pct_unsuitable = np.mean(unsuitable_mask) * 100
    pct_safe = 100 - pct_unsuitable

    # 6. Display Analytical Reports
    print(f"\n--- AGRONOMIC LAND SUITABILITY EVALUATION REPORT ---")
    print(f"⚠️ EXCLUSION ZONE: {pct_unsuitable:.2f}% of area is steeper than 15° (UNSUITABLE for row-crops).")
    print(f"✅ AVAILABLE LAND: {pct_safe:.2f}% of area is flat/gentle slopes (SAFE for development).")

    # 7. Render Binary Exclusion Visual Mask
    plt.figure(figsize=(8, 6))
    plt.imshow(unsuitable_mask, cmap="gray")
    plt.title("Agricultural Terrain Suitability Mask (White = Excluded Steeps)")
    plt.xlabel("Grid Cells (X)")
    plt.ylabel("Grid Cells (Y)")
    plt.show()

# Execute the complete pipeline
if __name__ == "__main__":
    run_land_suitability_analysis()
