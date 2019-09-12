# Examining glacier speed from 2013 to 2019 using the [GoLIVE](https://nsidc.org/data/NSIDC-0710) data set

A paper on glacier surges


## Project overview

The science objective in two parts: Where and when is valley glacier ice flowing at uncharacteristic speed? And: Is the moderate-term (six year) trend in valley glacier ice speed consistent with current understanding of
mass balance trends? 

In a bit more detail: Glaciers have annual variation in flow speed on the order of perhaps 20-30%. However, some glaciers become detached (floated above) their beds and _surge_, often moving at 400%+ of typical speed. That's interesting as it says something about both accumulation of snow and about bed conditions. Even the cursory analysis given here managed to turn up a surge on a small glacier east of Seward glacier.

The study site considered here is a region in southeast Alaska (Wrangell-St. Elias range) which is known to be in rapid retreat in response to increasing temperature \[Citation needed\]. If the ice is thinning then it has less driving stress and should slow down. Maybe that deceleration is apparent in the data.

I started with only a rudimentary understanding of data formats and Python data manipulation tools. These _golive_ notebooks are consequently self-tutorials on `xarray` and related machinery.


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


## Notebooks

These notebooks _golive1_, _golive2_ and _golive3_ demonstrate working with a moderately large geospatial dataset, the Global Land Ice Velocity Extraction from Landsat 8 data, aka [GoLIVE](https://nsidc.org/data/NSIDC-0710). In passing we also demonstrate bootstrapping Python file transfer over FTP, chart plotting, [xarray](http://xarray.pydata.org/en/stable/) and [dask](https://docs.dask.org/en/latest/) in relation to NetCDF-format files, and the [Pangeo](https://pangeo.io/) platform. As we proceed with the main narrative some digressive material is relegated to the supporting notebooks.

You can safely run the cells here in sequence. Cells that are compute-intensive are by default disabled
for example by means of `if False:`. This applies for example to large ftp file transfers. 

Some cells rely on pre-installed packages as implied by the first 'utility code' cell. Much 
of this is pre-installed in the JupyterHub environment on many Pangeo deployments; and some additional installs (e.g. utm) 
are invoked using `!pip install`. 

* [golive1](./golive1.ipynb) is a starting point on a data analysis paper (land ice velocity analysis)
* [golive2](./golive2.ipynb) extends golive1 in scope of data considered
* [golive3](./golive3.ipynb) extends golive2 in scope of data
* [golive4](./golive4.ipynb) is a tutorial
* [golive5](./golive5.ipynb) is resources for building the tutorial golive4
* [goliveLibrary.py](./goliveLibrary.ipynb) common utility functions


### The program for these GoLIVE notebooks

* Learn about GoLIVE _somehow_ (word of mouth discovery)
* Arrive thereby at the GoLIVE [home page](https://nsidc.org/data/NSIDC-0710) and the GoLIVE [map interface](https://nsidc.org/app/golive)
* Select a region and discover its Landsat 8 Path-Row frame
  * Arrive at the corresponding FTP server URL - now we can get data
  * Get a bunch of data. 
    * Each result is built from two source images and has therefore four characteristics
      * Path: Which Landsat orbital track the image pair is from
      * Row: Which Landsat row the image pair is from
      * Date: The date of the first of the two images in the pair
      * Interval: A number of days from the first to second image as a multiple of 16 days; up to 96 days
    * Each result is three files: A NetCDF file (`.nc`), a geotif (`.tif`) and a png (`.png`)

How to analzye the data? This grows progressively more sophisticated in the golive1/2/3 notebooks. At first: 

* Glacier transects: lateral _crossing the river_ at a limited set of times
* Deconstruct NetCDF files as `xarray` `Datasets` containing `DataArrays` 
  * Produce a set of transect speed profiles in time series (golive1 [notebook](./golive1.ipynb))

Subsequent notebooks work from the full time-sequence scale; and from six row-path
source locations in a single UTM zone. 


## The GoLIVE dataset

> Scambos, T., M. Fahnestock, T. Moon, A. Gardner, and M. Klinger. 2016. Global Land Ice Velocity Extraction from Landsat 8 (GoLIVE), Version 1. Landsat 8 Path 63 Row 18 all times. Boulder, Colorado USA. NSIDC: National Snow and Ice Data Center. doi: https://doi.org/10.7265/N5ZP442B. Data accessed: November 2018 - January 2019


The [GoLIVE data selection interface](https://nsidc.org/app/golive) hosted at NSIDC provides
a view of many overlapping Path/Row frames in our region of interest, southeast Alaska.
The glacier ice of this region moves with surface speed on the order of a few meters per day
in the glacier center, reducing to near-zero at glacier margins.


The source data files give speed of ice on glaciers in meters per day at 300-meter postings across
the Landsat frame. These speeds are derived by correlating surface features between two viewings. 
For GoLIVE purposes, Landsat repeat-viewings come in multiples of 16 days and are carried out 
all the way from 16 days to 32, 48, 64, 80 and 96 days. Often these comparisons are not possible
due to clouds, however. For more on Landsaat 8: 

- [Wikipedia on Landsat 8](https://en.wikipedia.org/wiki/Landsat_8)
- [USGS on Landsat 8](https://landsat.usgs.gov/landsat-8)
- [NASA on Landsat 8](https://landsat.gsfc.nasa.gov/landsat-8/mission-details/)


### NASA, GoLIVE and ITS LIVE

* NASA has a system called EOSDIS (Earth observing system Data and Information System) where datasets are provided by domain centers called DAACs (Distributed Active Archive Centers) (more [info](https://ieeexplore.ieee.org/abstract/document/528217) on this data hosting infrastructure)

* NSIDC (National Snow and Ice Data Center) hosts a cryosphere DAAC...
  * ...but the GoLIVE data are not technically _within_ the DAAC
  * ...rather GoLIVE is provided by NSIDC as a somewhat independent resource
  
* The DAACs in turn are unified under a NASA discovery mechanism called the Common Metadata Repository (CMR)

* The GoLIVE successor project ITS LIVE (Inter-Mission Time Series of Land Ice Velocity and Elevation) will be available through the CMR via affiliation with NASA MEaSUREs 
  * More on [MEaSUREs](https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects) (Making Earth System Data Records for Use in Research Environments)

* Question: Can the geoscience community improve this machinery for discoverability and use?
  * Notebooks like ones in this repo are intended to help


### Remarks on data discovery

The NASA CMR shows NSIDC as a DAAC with (Dec 2018) 343 collections (a fascinating list). However GoLIVE is not among them; that is, GoLIVE is not discoverable via CMR/GIBS. This point should become moot when ITS LIVE - a superset of GoLIVE - appears in CMR.
 
The 'word of mouth' nature of certain datasets is often decried as lost opportunity. GoLIVE certainly falls in that category by not being available in the CMR, for perhaps both top-down and bottom-up historical reasons. First there seems to be no top-down mechanism in place to couple NASA machinery to Principle Investigator-supplied data. Secondly bottom-up or grass roots discoverability paths for bespoke datasets are also not established at the individual NASA DAACs.   

GoLIVE is novel as a data resource: A large-scale PI-sourced dataset processed at NSIDC. Anticipating DAAC compatibility, the GoLIVE data products are nominally HDF5 netCDF4 CF 1.6 compliant, although the analysis given here raises some questions on this point. 

GoLIVE was funded as a NASA cryosphere research proposal: Successfully completed but with an 
indeterminate future. As of January 2019: There are nominal continuing costs associated with 
processing, storage and access mechanisms for GoLIVE that are not resolved. 

As noted, GoLIVE will be succeeded by a new [MEaSUREs](https://earthdata.nasa.gov/community/community-data-system-programs/measures-projects) product called the Inter-Mission Time Series Land Ice Velocity and Elevation (ITS LIVE) project. Noting that this will add surface elevation data, ITS LIVE is entering its first year and will span many observing platforms. Velocities will be produced, for example, from the complete available Landsat sequence (4, 5, 7, 8, possibly 9), and elevations will be produced from Synthetic Aperture Radars including [Sentinal S1A/B/C/D](https://en.wikipedia.org/wiki/Sentinel-1). Postings will be registered to a common grid to facilitate time-series comparison across sensors. Via MEaSUREs this effort will incorporate into the NASA DAAC/EOSDIS structure.


### A note on the two types of coordinates involved

The LANDSAT8 satellite follows repeated orbital paths. These are assigned numbers like 63. Each path is then broken into a numbered sequence of rows. As with paths the rows are assigned numbers like 18. Hence Path 63 Row 18 is a particular image that is *very* approximately 100 km x 100 km; a square degree give or take. From one result-file to another the coregistration is not perfect. Let's assume it is greater than 90% overlap; and `xarray` will manage the not-quite-perfect registration without complaint; but this brings us to the actual coordinates we will use for pixels in these images.

The pixels of these images are in a geographic Coordinate Reference System (CRS) rather than in the satellite _path-row_ raster coordinates. This is essential to permit us to compare pixels at the same geographic location between multiple velocity field images. The CRS uses the Universal Transverse Mercator (UTM) projection. UTM gives a rectangular approximation to a localized region on the earth's surface. The local coordinates are in meters, expressed as y- and x-axes and are respectively northing and easting. We also have the zone in which these coordinates fall. Approximately six LANDSAT path/row images will be found to rest in a single UTM Zone in this work. This allows us to compose a larger image from six source images. This is done in subsequent notebooks. 

The last remark to make on this is that the coordinate (1147, 3942) in zone 7V can be confused with (1147, 3942) in zone 8V unless we take care to differentiate them. The zone is a crucial context.






