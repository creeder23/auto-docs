# ENVI_ClassificationToShapefile

### Description
The task exports one or more classes to a single shapefile. The vectors include separate records for each polygon. 

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
gbdx = Interface()
shptask = gbdx.Task("ENVI_ClassificationToShapefile")
data = ' s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/classification/classification_name.hdr'
shptask.inputs.input_raster = data
shptask.inputs.file_types = "hdr"
workflow = gbdx.Workflow([shptask])
workflow.savedata(
	       shptask.outputs.output_vector_uri,
	          location='Auto-docs/ENVI/SHP'
)
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
input_raster|True|None| |Specify a classification raster from which to generate a shapefile. -- Value Type: ENVIRASTER
export_class_clrs|False|None| |Set this property to export CLASS_CLRS (class colors) as a shapefile attribute for each polygon. The options are true (default) or false. -- Value Type: BOOL
export_classes|False|None| |Specify a string array with class names to export to the shapefile. -- Value Type: STRING[*]
export_area|False|None| |Set this property to export AREA as a shapefile attribute for each polygon. The options are true (default) or false. -- Value Type: BOOL
output_vector_uri_filename|False|None| |Outputor OUTPUT_VECTOR. -- Value Type: ENVIURI

### Outputs
The following table lists all taskname outputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
task_meta_data|False|None| |GBDX Option. Output location for task meta data such as execution log and output JSON
output_vector_uri|True|None| |Outputor OUTPUT_VECTOR. -- Value Type: ENVIURI

**Output structure**

Explain output structure via example.


### Advanced
Include example(s) with complicated parameter settings and/or example(s) where the task is used as part of a workflow involving other GBDX tasks.

```python

# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
from gbdxtools import Interface
gbdx = Interface()
shptask = gbdx.Task("ENVI_ClassificationToShapefile")
data = ' s3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/classification/classification_name.hdr'
shptask.inputs.input_raster = data
shptask.inputs.file_types = "hdr"
workflow = gbdx.Workflow([shptask])
workflow.savedata(
	       shptask.outputs.output_vector_uri,
	          location='Auto-docs/ENVI/SHP'
)
workflow.execute()
status = workflow.status["state"]
wf_id = workflow.id
# print wf_id
# print status
```

### Issues
List known past/current issues with this task (e.g., version x does not ingest vrt files).


### Background
For background on the development and implementation of this task see [here](Insert link here).


### Contact
List contact information for technical support.
