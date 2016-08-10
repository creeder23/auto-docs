# ENVI_AutoChangeThresholdClassification

### Description
This task uses pre-defined thresholding techniques to automatically classify change detection between two images

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
# Quickstart example for ENVI_AutoChangeThresholdClassification.
```

### Inputs
The following table lists all taskname inputs.
Mandatory (optional) settings are listed as Required = True (Required = False).

  Name  |  Required  |  Default  |  Valid Values  |  Description  
--------|:----------:|-----------|----------------|---------------
file_types|False|None| |GBDX Option. Comma seperated list of permitted file type extensions. Use this to filter input files -- Value Type: STRING[*]
input_raster|True|None| |Specify a raster on which to threshold. -- Value Type: ENVIRASTER
output_raster_uri_filename|False|None| |Outputor OUTPUT_RASTER. -- Value Type: ENVIURI
change_type|False|None| |The type of change to consider for change of interest. -- Value Type: STRING
threshold_method|False|None| |Specify the thresholding method. Otsu (default): A histogram shape-based method that is based on discriminate analysis. It uses the zero- and the first-order cumulative moments of the histogram for calculating the value of the thresholding level. Tsai: A moment-based method. It determines the threshold so that the first three moments of the input image are preserved in the output image. Kapur: An entropy-based method. It considers the thresholding image as two classes of events, with each class characterized by Probability Density Function (PDF). The method then maximizes the sum of the entropy of the two PDFs to converge on a single threshold value. Kittler: A histogram shape-based method. It approximates the histogram as a bimodal Gaussian distribution and finds a cutoff point. The cost function is based on the Bayes classification rule. -- Value Type: STRING

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
