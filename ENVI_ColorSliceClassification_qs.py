#AOP strip processor has input values known to complete the Spectral Index task
from gbdxtools import Interface
gbdx = Interface()


data = 's3://receiving-dgcs-tdgplatform-com/055605759010_01_003'

aoptask = gbdx.Task("AOP_Strip_Processor", data=data, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')

# Capture AOP task outputs
#orthoed_output = aoptask.get_output('data')

envi_hdr = gbdx.Task("Build_ENVI_HDR")
envi_hdr.inputs.image = aoptask.outputs.data.value

#hdr file used to compute spectral index

envi_ndvi = gbdx.Task("ENVI_SpectralIndex")
envi_ndvi.inputs.input_raster = envi_hdr.outputs.output_data.value
envi_ndvi.inputs.file_types = "hdr"
envi_ndvi.inputs.index = "Normalized Difference Vegetation Index"

#spectral index file used in color slice classification task

envi_color = gbdx.Task('ENVI_ColorSliceClassification', input_raster=envi_ndvi.outputs.output_raster_uri.value)
envi_color.file_types = 'hdr'


workflow = gbdx.Workflow([aoptask, envi_hdr, envi_ndvi, envi_color])

workflow.savedata(
  envi_ndvi.outputs.output_raster_uri,
  location='Benchmark/color_slice/NDVI'
)

workflow.savedata(
  envi_color.outputs.output_raster_uri,
  location='Benchmark/color_slice/Color16'
)

workflow.execute()

print workflow.execute()
print workflow.id
print workflow.status
