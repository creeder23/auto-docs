def runfunction():

    try:

        from gbdxtools import Interface
        gbdx = Interface()
        aop2envi = gbdx.Task("AOP_ENVI_HDR")
        aop2envi.inputs.image = 's3://gbd-customer-data/7d8cfdb6-13ee-4a2a-bf7e-0aff4795d927/ENVI/SI/AOP/055026839010_01/'

        workflow = gbdx.Workflow([aop2envi])
        workflow.savedata(
            aop2envi.outputs.output_data,
            location='Doctest/hdr/test'
        )
        workflow.execute()
        status = workflow.status["state"]
        wf_id = workflow.id

        ifarted

        # print wf_id
        # print status

    except:

        wf_id = 0
        status = 'failed'

    finally:

        return {'wfid': wf_id, 'wfst': status}


if __name__ == "__main__":
    runfunction()
