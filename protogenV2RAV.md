# protogenV2RAV

### Description
This task requires a single input 'raster' that is an 8-band WorldView 2/3 image that has been atmospherically compensated. It returns a binary mask raster image with 255: foreground, 0: background.

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
from gbdxtools import Interface
gbdx = Interface()
data = "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003"
aoptask2 = gbdx.Task('AOP_Strip_Processor', data=data, bands='MS', enable_acomp=True, enable_pansharpen=False,
                     enable_dra=False)  # creates acomp'd multispectral image
gluetask = gbdx.Task('gdal-cli')  # move aoptask output to root where prototask can find it
gluetask.inputs.data = aoptask2.outputs.data.value
gluetask.inputs.execution_strategy = 'runonce'
gluetask.inputs.command = """mv $indir/*/*.tif $outdir/"""
prototask = gbdx.Task('protogenV2RAV')
prototask.inputs.raster = gluetask.outputs.data.value
workflow = gbdx.Workflow([aoptask2, gluetask, prototask])
workflow.savedata(
    prototask.outputs.data,
    location='Doctest/RAV/test'
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
raster|True|None| |Name of the geo-coded image file that will be processed. Supported formats: TIF, TIL, VRT raster images.

### Outputs
The following table lists all taskname outputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
data|True|None| |The output directory of text file

**Output structure**

Explain output structure via example.


### Advanced
Include example(s) with complicated parameter settings and/or example(s) where the task is used as part of a workflow involving other GBDX tasks.

```python
from gbdxtools import Interface
gbdx = Interface()
data = "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003"
aoptask2 = gbdx.Task('AOP_Strip_Processor', data=data, bands='MS', enable_acomp=True, enable_pansharpen=False,
                     enable_dra=False)  # creates acomp'd multispectral image
gluetask = gbdx.Task('gdal-cli')  # move aoptask output to root where prototask can find it
gluetask.inputs.data = aoptask2.outputs.data.value
gluetask.inputs.execution_strategy = 'runonce'
gluetask.inputs.command = """mv $indir/*/*.tif $outdir/"""
prototask = gbdx.Task('protogenV2RAV')
prototask.inputs.raster = gluetask.outputs.data.value
workflow = gbdx.Workflow([aoptask2, gluetask, prototask])
workflow.savedata(
    prototask.outputs.data,
    location='Doctest/RAV/test'
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
