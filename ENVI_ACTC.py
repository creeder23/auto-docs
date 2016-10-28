from gbdxtools import Interface
gbdx = Interface()

data1 = "s3://receiving-dgcs-tdgplatform-com/055438828010_01_003"
data2 = "s3://receiving-dgcs-tdgplatform-com/055690224010_01_003"

aoptask1 = gbdx.Task("AOP_Strip_Processor", data=data1, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')
aoptask2 = gbdx.Task("AOP_Strip_Processor", data=data2, enable_acomp=True, enable_pansharpen=False, enable_dra=False, bands='MS')

# Capture AOP task outputs
#orthoed_output = aoptask.get_output('data')

aop2envi1 = gbdx.Task("AOP_ENVI_HDR")
aop2envi1.inputs.image = aoptask1.outputs.data.value

aop2envi2 = gbdx.Task("AOP_ENVI_HDR")
aop2envi2.inputs.image = aoptask2.outputs.data.value

envi_ndvi1 = gbdx.Task("ENVI_SpectralIndex")
envi_ndvi1.inputs.input_raster = aop2envi1.outputs.output_data.value
envi_ndvi1.inputs.file_types = "hdr"
envi_ndvi1.inputs.index = "Normalized Difference Vegetation Index"

envi_ndvi2 = gbdx.Task("ENVI_SpectralIndex")
envi_ndvi2.inputs.input_raster = aop2envi2.outputs.output_data.value
envi_ndvi2.inputs.file_types = "hdr"
envi_ndvi2.inputs.index = "Normalized Difference Vegetation Index"

envi_ACTC = gbdx.Task("ENVI_AutoChangeThresholdClassification")
envi_ACTC.inputs.threshold_method = "Otsu"
envi_ACTC.inputs.file_types = "hdr"
envi_ACTC.inputs.input_raster = envi_ndvi1.outputs.output_raster_uri.value
envi_ACTC.inputs.input_raster = envi_ndvi2.outputs.output_raster_uri.value


workflow = gbdx.Workflow([aoptask1, aoptask2, aop2envi1, aop2envi2, envi_ndvi1, envi_ndvi2, envi_ACTC])

workflow.savedata(
    envi_ACTC.outputs.output_raster_uri,
        location='Benchmark/ENVI_ACTC/test'
)


workflow.execute()

status = workflow.status["state"]
wf_id = workflow.id
