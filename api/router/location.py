from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException
#from schema import LocationUpdate
from api.db.schemas.schema import LocationUpdateSchema
from starlette import status

router = APIRouter(
    prefix='/location-updates',
    tags=['Location'],
    responses={status.HTTP_404_NOT_FOUND: {"message":"no encontrado"}}
)

@router.get("/")
async def get_location_updates(params: LocationUpdateSchema = Depends()):
    """
    Endpoint to handle GET requests for Location Updates webhook from MacroPoint.
    """
    # Log the received data
    print("Received Location Update:")
    for key, value in params.dict().items():
        print(f"{key}: {value}")

    # Check required fields (this is already enforced by Pydantic)
    if not all([params.MPOrderID, params.ID, params.Latitude, params.Longitude]):
        raise HTTPException(status_code=400, detail="Missing required parameters")

    # Send back a response
    response = {
        "status": "success",
        "message": "Location update received successfully",
        "data": params.dict()
    }

    return response