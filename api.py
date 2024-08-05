from repair import Customer, Device, Job

from fastapi import FastAPI

app = FastAPI(
    title='RepairShop'
    summary='Manage repairs online'
    description="""
    Keep a thorough level of communication between the business and its customers by:
    Updating the status of the job
    Add notes as equipment is diagnosed and solutions are proposed
    Adding price estimates as they are found
    Add a special notification if a call is needed to speak about the job
    """
    )