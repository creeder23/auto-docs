def runfunction():

    try:

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

        print wf_id
        print status

        status = 'failed'

    except:

        wf_id = 0
        status = 'failed'

    finally:

        return {'wfid': wf_id, 'wfst': status}


if __name__ == "__main__":
    runfunction()
