# SomoBench
Benchmark datasets for machine learning in soil moisture modeling

# What is SomoBench

# About this repository

  - scripts/somobench.py: python script to directly use SomoBench data
    - one year has three .netcdf files; 1) meteorological forcing data, 2) static features, and 3) upscaled soil moisture
     
  - scripts/pre_soilm.py: python script to prepare SomoBench data at a grid pixel using ISMN raw data
    - download soil moisture data from [https://www.ismn.](https://ismn.earth) (log-in required) > DATA ACCESS
    - data can be extracted using ISMN github ()
    - see the example files in .
      
  - scripts
    - down_era5.py: to download daily ERA5 data using the CDS API service.
    - extract_era5.py: to extract meteorological forcing data from ERA5 at given grid pixels
    - extract_statics.py: to extract static features at given grid pixels
  
# Reference
