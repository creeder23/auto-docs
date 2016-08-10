# ENVI_GaussianStretchRaster

### Description
This task accepts a source raster and returns a raster with a Gaussian stretch applied.

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
# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
from gbdxtools import Interface
import json
gbdx = Interface()
#launch workflow ENVI_GaussianStretchRaster -> S3
#example data WV02 image of Denver previously in 1-B format (multiple til files note stretch will be performed on 1 TIL file)
data = "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003"
envitask = gbdx.Task("ENVI_GaussianStretchRaster")
envitask.inputs.file_types='TIL'
envitask.inputs.input_raster=data
#Example Min/Max inputs  see ENVI documentation for information on min max paramater settings
envitask.inputs.min="[180, 210, 120, 90]"
envitask.inputs.max="[800, 1300, 1055, 1100]"

workflow = gbdx.Workflow([ envitask ] )
workflow.savedata(envitask.outputs.task_meta_data, location='ENVI/Gaussian')
workflow.savedata(envitask.outputs.output_raster_uri, location='ENVI/Gaussian')

workflow.execute()
status = workflow.status["state"]
wf_id = workflow.id
# print wf_id
# print status
```

### Inputs
The following table lists all taskname inputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
file_types|False|None| |GBDX Option. Comma seperated list of permitted file type extensions. Use this to filter input files -- Value Type: STRING[*]
input_raster|True|None| |Specify a raster on which to apply gaussian stretch. -- Value Type: ENVIRASTER
brightness|False|None| |Specify an integer value from 0 to 100, indicating the brightness level to display. You can also set this value to a scalar or an array with the same number of elements as the raster has bands. -- Value Type: DOUBLE[*]
max|True|None| |Specify the maximum value to be considered, also known as the white point. If the value is a scalar, it applies to all bands. If it is an array, it must have the same number of elements as the input raster has bands. -- Value Type: DOUBLE[*]
min|True|None| |Specify the minimum value to be considered, also known as the black point. If this value is a scalar, it applies to all bands. If it is an array, it must have the same number of elements as the input raster has bands. -- Value Type: DOUBLE[*]
stddev|False|None| |Specify the standard deviation value for the Gaussian function. -- Value Type: DOUBLE[*]
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
