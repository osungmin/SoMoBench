import numpy as np
import cdsapi 
import sys
print("modules imported")

#install Install the CDS API key first
#https://cds.climate.copernicus.eu/api-how-to

c = cdsapi.Client()

for var in ['variable names']:  
  for year in np.arange(2004,2013+1,1):
    for mon in range(12):
      
      kwargs={
        'dataset': 'reanalysis-era5-single-levels',
        'product_type':'reanalysis',
        'variable': var,
        'pressure_level': '-',
        'statistic': 'daily_mean',
        'year': str(year),
        'month': str(mon+1).zfill(2),
        'time_zone': 'UTC+00:00',
        'frequency': '1-hourly ',
        'grid': '0.25/0.25',
        'area': {'lat': [-90, 90], 'lon': [-180,180]}
      }
      
      result = c.service(
        "tool.toolbox.orchestrator.workflow",
        params={
          "realm": "user-apps",
          "project": "app-c3s-daily-era5-statistics",
          "version": "master",
          "kwargs": kwargs,
          "workflow_name": "application"
        })
      
      c.download(result)
