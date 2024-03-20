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
  - scripts/pre_era.py: python script to extract meteorological forcing data at given grid pixels
  - scripts/pre_statics.py: python script to extract static features at given grid pixels
  
# Reference
