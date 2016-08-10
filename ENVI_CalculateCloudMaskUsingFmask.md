# ENVI_CalculateCloudMaskUsingFmask

### Description
This task calculates a cloud mask for the following sensors: Landsat 4-5 TM, Landsat 7 ETM+, Landsat 8, and Sentinel-2.

This task can be run with Python using [gbdxtools](https://github.com/DigitalGlobe/gbdxtools) or through the [GBDX Web Application](https://gbdx.geobigdata.io/materials/)

### Table of Contents
 * [Quickstart](#quickstart) - Get started!
 * [Inputs](#inputs) - Required and optional task inputs.
 * [Outputs](#outputs) - Task outputs and output structure.
 * [Advanced](#advanced) - Additional information for advanced users.
 * [Issues](#issues) - Current or past known issues.
 * [Background](#background) - Background information.
 * [Contact](#contact) - Contact information.

### Quickstart

Quick start example.

```python
# Quickstart example for ENVI_CalculateCloudMaskUsingFmask.
```

### Inputs
The following table lists all taskname inputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
file_types|False|None| |GBDX Option. Comma seperated list of permitted file type extensions. Use this to filter input files -- Value Type: STRING[*]
input_reflectance_raster|True|None| |Specify a raster containing the multispectral bands, calibrated to top-of-atmosphere (TOA) reflectance. -- Value Type: ENVIRASTER
input_cirrus_raster|False|None| |Specify a cirrus band raster, calibrated to top-of-atmosphere (TOA) reflectance. -- Value Type: ENVIRASTER
input_brightness_temperature_raster|False|None| |Specify a thermal band raster, calibrated to brightness temperatures. -- Value Type: ENVIRASTER
cloud_threshold|False|None| |Specify a floating-point threshold for cloud probability over clear-land and clear-water regions. -- Value Type: DOUBLE
kernel_size|False|None| |Specify the number of pixels along one side of a square kernel. The default value is 7 (to create a 7 x 7 array). Cloud regions are dilated by this kernel size before output. -- Value Type: UINT
output_raster_uri_filename|False|None| |Outputor OUTPUT_RASTER. -- Value Type: ENVIURI

### Outputs
The following table lists all taskname outputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
task_meta_data|False|None| |GBDX Option. Output location for task meta data such as execution log and output JSON
output_raster_uri|True|None| |Outputor OUTPUT_RASTER. -- Value Type: ENVIURI

**Output structure**

Explain output structure via example.


### Advanced
Include example(s) with complicated parameter settings and/or example(s) where this task is used as part of a workflow involving other GBDX tasks.


### Issues
List known past/current issues with this task (e.g., version x does not ingest vrt files).


### Background
For background on the development and implementation of this task see [here](Insert link here).


### Contact
List contact information for technical support.
