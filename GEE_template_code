var region = ee.Geometry.Rectangle([78.9, 20.9, 79.3, 21.3]);
Map.centerObject(region, 10);

var image2010 = ee.ImageCollection("LANDSAT/LT05/C02/T1_L2")
  .filterBounds(region)
  .filterDate('2010-01-01', '2010-12-31')
  .select(['SR_B3', 'SR_B4'])
  .median()
  .multiply(0.0000275).add(-0.2);

var ndvi2010 = image2010.normalizedDifference(['SR_B4', 'SR_B3']).rename('NDVI_2010');

var image2025 = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
  .filterBounds(region)
  .filterDate('2025-01-01', '2025-12-31')
  .select(['SR_B4', 'SR_B5'])
  .median()
  .multiply(0.0000275).add(-0.2);

var ndvi2025 = image2025.normalizedDifference(['SR_B5', 'SR_B4']).rename('NDVI_2025');

var ndviChange = ndvi2025.subtract(ndvi2010).rename('NDVI_Change');

Map.addLayer(ndvi2010, {min: 0, max: 1, palette: ['white', 'green']}, 'NDVI 2010');
Map.addLayer(ndvi2025, {min: 0, max: 1, palette: ['white', 'green']}, 'NDVI 2025');
Map.addLayer(ndviChange, {min: -0.5, max: 0.5, palette: ['red', 'white', 'green']}, 'NDVI Change 2010-2025');

var samplePoints = ndviChange.sample({
  region: region,
  scale: 30,
  numPixels: 5000,
  geometries: true
});

Export.table.toDrive({
  collection: samplePoints,
  description: 'Nagpur_Manganese_NDVI_Change_Samples',
  fileFormat: 'CSV'
});
