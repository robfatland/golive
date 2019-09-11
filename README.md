# Examining glacier speed from 2013 to 2019 using the [GoLIVE](https://nsidc.org/data/NSIDC-0710)  data set

A paper on glacier surges


## Project overview

The science objective in two parts: Where and when is valley glacier ice flowing at uncharacteristic speed?
And: Is the moderate-term (six year) trend in valley glacier ice speed consistent with current understanding of
mass balance trends? 

In a bit more detail: Glaciers have annual variation in flow speed on the order of perhaps 20-30%. However, some glaciers become detached (floated above) their beds and _surge_, often moving at 400%+ of typical speed. That's interesting as it says something about both accumulation of snow and about bed conditions. Even the cursory analysis given here managed to turn up a surge on a small glacier east of Seward glacier.

The study site considered here is a region in southeast Alaska (Wrangell-St. Elias range) which is known to be in rapid retreat in response to increasing temperature \[Citation needed\]. If the ice is thinning then it has less driving stress and should slow down. Maybe that deceleration is apparent in the data.

I started with only a rudimentary understanding of data formats and Python data manipulation tools. These `golive` notebooks are consequently self-tutorials on `xarray` and related machinery.


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


## A note on the two types of coordinates involved

The LANDSAT8 satellite follows repeated orbital paths. These are assigned numbers like 63. Each path is then broken into a numbered sequence of rows. As with paths the rows are assigned numbers like 18. Hence Path 63 Row 18 is a particular image that is *very* approximately 100 km x 100 km; a square degree give or take. From one result-file to another the coregistration is not perfect. Let's assume it is greater than 90% overlap; and `xarray` will manage the not-quite-perfect registration without complaint; but this brings us to the actual coordinates we will use for pixels in these images.

The pixels of these images are in a geographic Coordinate Reference System (CRS) rather than in the satellite _path-row_ raster coordinates. This is essential to permit us to compare pixels at the same geographic location between multiple velocity field images. The CRS uses the Universal Transverse Mercator (UTM) projection. UTM gives a rectangular approximation to a localized region on the earth's surface. The local coordinates are in meters, expressed as y- and x-axes and are respectively northing and easting. We also have the zone in which these coordinates fall. Approximately six LANDSAT path/row images will be found to rest in a single UTM Zone in this work. This allows us to compose a larger image from six source images. This is done in subsequent notebooks. 


The last remark to make on this is that the coordinate (1147, 3942) in zone 7V can be confused with (1147, 3942) in zone 8V unless we take care to differentiate them. The zone is a crucial context.



