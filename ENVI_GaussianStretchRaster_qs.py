def runfunction(data_num):

    data_sets = ["s3://receiving-dgcs-tdgplatform-com/055026839010_01_003",
                 "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003",
                  "s3://receiving-dgcs-tdgplatform-com/055026839010_01_003"]

    data = data_sets[data_num]


    try:
# Quickstart **Example Script Run in Python using the gbdxTools InterfaceExample producing a single band vegetation mask from a tif file.
# First Initialize the Environment
        from gbdxtools import Interface
        gbdx = Interface()
        import datetime
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

        t1 = datetime.datetime.now()
        workflow.execute()
        t2 = datetime.datetime.now()

        while envitask != workflow.
        status = workflow.status["state"]
        wf_id = workflow.id

# print wf_id
# print status

    except:

        wf_id = 0
        status = 'failed'

    finally:

        return {'wfid': wf_id, 'wfst': status}


if __name__ == "__main__":
    runfunction()
