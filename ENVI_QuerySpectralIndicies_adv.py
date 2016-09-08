from gbdxtools import Interface
gbdx = Interface()

aop2envi = gbdx.Task("AOP_ENVI_HDR")
aop2envi.inputs.image = 's3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/SI/AOP/055026839010_01/'
aop2envi.domain = "ondemand"


envi_query = gbdx.Task("ENVI_QuerySpectralIndices")
envi_query.inputs.input_raster = aop2envi.outputs.output_data.value
envi_query.inputs.file_types = "hdr"
envi_query.domain = "ondemand"

envi_SI = gbdx.Task("ENVI_SpectralIndices")
envi_SI.inputs.input_raster = aop2envi.outputs.output_data.value
envi_SI.inputs.file_types = "hdr"
envi_SI.domain = "ondemand"

# Specify a string/list of indices to run on the input_raster variable.  The order of indices will determine the band order of the tif

#envi_SI.inputs.index = '["available_indices"]'
envi_SI.inputs.index = envi_query.outputs.available_indices.value

workflow = gbdx.Workflow([aop2envi, envi_query, envi_SI])

workflow.savedata(
	envi_SI.outputs.output_raster_uri,
	location='Auto-docs/ENVI/Query/ENVI_SI'
)

workflow.execute()
status = workflow.status["state"]
wf_id = workflow.id
