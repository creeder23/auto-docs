# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
from gbdxtools import Interface
gbdx = Interface()

aop2envi = gbdx.Task("AOP_ENVI_HDR")
aop2envi.inputs.image = 's3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/SI/AOP/055026839010_01/'

envi_ndvi = gbdx.Task("ENVI_SpectralIndices")
envi_ndvi.inputs.input_raster = aop2envi.outputs.output_data.value
envi_ndvi.inputs.file_types = "hdr"
# Specify a string/list of indicies to run on the input_raster variable.  The order of indicies wi
envi_ndvi.inputs.index = '["Normalized Difference Vegetation Index", "WorldView Soil Index"]'

workflow = gbdx.Workflow([aop2envi, envi_ndvi])
workflow.savedata(
	aop2envi.outputs.output_data,
	location='Auto-docs/ENVI/SIS'
)

workflow.savedata(
	envi_ndvi.outputs.output_raster_uri,
	location='Auto-docs/ENVI/SIS'
)

print workflow.execute()
