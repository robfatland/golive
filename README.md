# Examining glacier speed from 2013 to 2019 using the [GoLIVE](https://nsidc.org/data/NSIDC-0710)  data set

A paper on glacier surges


## Notebooks

* golive1 is a starting point on a data analysis paper (land ice velocity analysis)
* golive2 extends golive1 in scope of data considered
* golive3 extends golive2 in scope of data
* golive4 is a tutorial
* golive5 is resources for building the tutorial golive4
* goliveLibrary.py is source code; it should be re-factored into notebooks (but it is suggestive of library-building)


## Data

> Scambos, T., M. Fahnestock, T. Moon, A. Gardner, and M. Klinger. 2016. Global Land Ice Velocity Extraction from Landsat 8 (GoLIVE), Version 1. Landsat 8 Path 63 Row 18 all times. Boulder, Colorado USA. NSIDC: National Snow and Ice Data Center. doi: https://doi.org/10.7265/N5ZP442B. Data accessed: November 2018 - January 2019


## Useful references

- [Nature paper on Himalayan speeds by Dehecq and others](https://www.nature.com/articles/s41561-018-0271-9)
- [Scott's GitHub gist on least squares fit to time in xarray](https://gist.github.com/scottyhq/8daa7290298c9edf2ef1eb05dc3b6c60)
- [Scott's blog on pangeo NDVI](https://medium.com/pangeo/cloud-native-geoprocessing-of-earth-observation-satellite-data-with-pangeo-997692d91ca2)
- [Scott's corresponding NDVI Binder](http://binder.pangeo.io/v2/gh/scottyhq/pangeo-example-notebooks/landsat-cog?urlpath=lab/tree/landsat8-cog-ndvi.ipynb)
- [Scott's HIMAT Webinar](http://wiki.esipfed.org/index.php/Interoperability_and_Technology/Tech_Dive_Webinar_Series#14_Feb_2019:_.22Cloud_Native_Geoprocessing_of_Earth_Observation_Satellite_Data_with_Pangeo.22:_Scott_Henderson_.28University_of_Washington.29)
- [Andrew Tedstone remark on counting occurrences in xarray/dask](http://atedstone.github.io/count-with-xarray/)
- [pangeo](http://pangeo.io)
- [NASA panoply NetCDF explorer](https://www.giss.nasa.gov/tools/panoply/)


<img src="figures/pangeo.png" alt="drawing" width="500"/>