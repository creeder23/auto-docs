# ENVI_QuerySpectralIndices

### Description
This task returns a string array of the spectral indices that can be computed for a given input raster, based on its wavelength metadata.

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
# Quickstart example for ENVI_QuerySpectralIndices.
from gbdxtools import Interface
gbdx = Interface()

aop2envi = gbdx.Task("AOP_ENVI_HDR")
aop2envi.inputs.image = 's3://gbd-customer-data/path_to_image'

envi_query = gbdx.Task("ENVI_QuerySpectralIndices")
envi_query.inputs.input_raster = aop2envi.outputs.output_data.value
envi_query.inputs.file_types = "hdr"

workflow = gbdx.Workflow([aop2envi, envi_query])

workflow.savedata(
  envi_ndvi.outputs.output_raster_uri,
    location='ENVI_QuerySpectralIndices'
)

workflow.execute()
status = workflow.status["state"]
wf_id = workflow.id
```

### Inputs
The following table lists all taskname inputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
file_types|False|None| |GBDX Option. Comma separated list of permitted file type extensions. Use this to filter input files -- Value Type: STRING[*]
input_raster|True|None| |Specify a raster to query for available spectral indices. -- Value Type: ENVIRASTER

### Outputs
The following table lists all taskname outputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
task_meta_data|False|None| |GBDX Option. Output location for task meta data such as execution log and output JSON
available_indices|True|None| |A string array with the spectral indices that can be computed for the input raster. -- Value Type: STRING[*]

**Output structure**

The output of this task is a Json file listing the available indices, based on the bands available in the image file. Alternatively, the output of this task can be used as input for the ENVI Spectral Indices task.  Based on the available_indices output from this task, it is possible specify the list as input for the Spectral Indices task.


### Advanced
```Python

from gbdxtools import Interface
gbdx = Interface()

data = "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003"
aoptask = gbdx.Task('AOP_Strip_Processor', data=data, bands='MS', enable_acomp=True, enable_pansharpen=False, enable_dra=False)    
# creates acomp'd multispectral image

aop2envi = gbdx.Task("AOP_ENVI_HDR")
aop2envi.inputs.image = aoptask.outputs.data.value
aop2envi.domain = "ondemand"


envi_query = gbdx.Task("ENVI_QuerySpectralIndices")
envi_query.inputs.input_raster = aop2envi.outputs.output_data.value
envi_query.inputs.file_types = "hdr"
envi_query.domain = "ondemand"


workflow = gbdx.Workflow([aoptask, aop2envi, envi_query])

workflow.savedata(
  envi_query.outputs.task_meta_data,
    location='Auto-docs/ENVI/Query'
)

workflow.execute()
status = workflow.status["state"]
wf_id = workflow.id

```

### Issues
NA

### Background
For background on the development and implementation of ENVI Query Spectral Indices see [here](http://www.harrisgeospatial.com/docs/ENVIQuerySpectralIndicesTask.html).


### Contact
Document Owner - Carl Reeder - creeder@digitalglobe.com
