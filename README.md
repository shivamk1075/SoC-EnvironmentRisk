# SoC-EnvironmentRisk

# Topic 1
NDVI (Normalized Difference Vegetation Index)
NDVI shows how green or healthy the vegetation is by comparing how much red light is absorbed and how much near-infrared light is reflected by plants.

Higher values (close to +1) indicate healthy vegetation, while lower or negative values point to barren land, built-up areas, or water.

NDBI (Normalized Difference Built-up Index)
NDBI helps identify urban or built-up areas by measuring the contrast between shortwave infrared and near-infrared reflectance.

Higher values suggest man-made surfaces like buildings and roads, while lower values usually represent vegetation or water bodies.

# Topic 2
- Start with `Geocode_List.py`, it reads mining names from `data.xlsx`, searches Wikipedia for coordinates, extracts them using regex, converts to decimal, and saves to `Harshvardhan_coords.csv`.  
- These coordinates are used in `sample_task1.ipynb`, which connects to Google Earth Engine and defines a 5×5 km mining area plus 14 km surroundings for each mine.  
- It exports 10 images per mine to Google Drive like NDVI maps for 2020 and 2024, urban fraction, land-use, and true color scenes.  
- `Annonated.py` reads these `.tif` files, resizes them, adds a white background, and pastes legends if needed. It creates final PNGs with proper labels in `task1/`.  
- `task2_dataScrap.ipynb` reads satellite images and calculates forest loss, average distance to nearby forest, urban growth, land-use change, and finds the nearest forest using reverse geocoding.  
- It also adds temperature and air quality values from MODIS and Sentinel-5P for both mine and forest points.  
- All results are saved to `zone_features_with_forest.csv` and enriched to `zone_features_enriched.csv`.

# Topic 3: Resources

### Hands-on Learning

- **Machine Learning (Codebasics)**  
  [Watch on YouTube](https://youtu.be/i_LwzRVP7bg?si=XzBY1XZMLbkDQHyq)

- **TensorFlow Project Example**  
  [Watch on YouTube](https://youtu.be/VtRLrQ3Ev-U?si=35fxQsChnnU1I3zs)

### Pandas

- **Cheat Sheet (Datacamp)**  
  [View PDF](https://media.datacamp.com/legacy/image/upload/v1676302204/Marketing/Blog/Pandas_Cheat_Sheet.pdf)

- **Tutorial (CodeWithHarry)**  
  [Watch on YouTube](https://youtu.be/RhEjmHeDNoA?si=r0cOV8U6zYUBRsqa)

### Deep Learning

There are two major frameworks:

- **TensorFlow Playlist**  
  [Watch Playlist](https://youtube.com/playlist?list=PLhhyoLH6IjfxVOdVC1P1L5z5azs0XjMsb&si=Xn0LTOONl5vmH_2h)

- **PyTorch Playlist**  
  [Watch Playlist](https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4)

### Theory and Conceptual Understanding

- **Andrew Ng's Machine Learning Specialization (Coursera)**  
  [Go to Course](https://www.coursera.org/specializations/machine-learning-introduction)

You can audit the course for free and access all lectures. Only assignments are locked. Financial aid is also available.
