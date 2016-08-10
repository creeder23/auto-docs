# ENVI_SpectralSubspaceBackgroundStatistics

### Description
This task removes anomalous pixels and can be used prior to calculating background statistics. When the true background is better characterized with subspace background, the spectral detection methods achieve greater target-to-background separation. This can potentially improve detection results, particularly in scenes that contain a lot of clutter or man-made objects.

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
# Quickstart example for ENVI_SpectralSubspaceBackgroundStatistics.
```

### Inputs
The following table lists all taskname inputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
file_types|False|None| |GBDX Option. Comma seperated list of permitted file type extensions. Use this to filter input files -- Value Type: STRING[*]
threshold|False|None| |Specify the fraction of the background to use for calculating the subspace background statistics. The data type is floating-point. The allowable range is 0.500 to 1.000 (the entire image). -- Value Type: DOUBLE
input_raster|True|None| |Specify a raster for computing subspace background statistics. -- Value Type: ENVIRASTER

### Outputs
The following table lists all taskname outputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
task_meta_data|False|None| |GBDX Option. Output location for task meta data such as execution log and output JSON
covariance|False|None| |This is the covariance matrix of the subspace background, returned as a double-precision array [number of bands, number of classes]. -- Value Type: DOUBLE[*, *]
eigenvalues|False|None| |The eigenvalues of the subspace background. -- Value Type: DOUBLE[*]
mean|False|None| |The mean of the subspace background, one for each input bands. -- Value Type: DOUBLE[*]

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
