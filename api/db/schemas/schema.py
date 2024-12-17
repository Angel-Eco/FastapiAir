from pydantic import BaseModel, Field
from typing import Optional

class LocationUpdateSchema(BaseModel):
    MPOrderID: str = Field(..., description="Order ID")
    ID: str = Field(..., description="Unique ID")
    Latitude: float = Field(..., description="Latitude")
    Longitude: float = Field(..., description="Longitude")
    Uncertainty: Optional[float] = Field(None, description="Uncertainty of location")
    Street1: Optional[str] = Field(None, description="Street line 1")
    Street2: Optional[str] = Field(None, description="Street line 2")
    Neighborhood: Optional[str] = Field(None, description="Neighborhood")
    City: Optional[str] = Field(None, description="City")
    State: Optional[str] = Field(None, description="State")
    Postal: Optional[str] = Field(None, description="Postal code")
    Country: Optional[str] = Field(None, description="Country")
    LocationDateTimeUTC: Optional[str] = Field(None, description="Location date time in UTC")
    ApproxLocationDateTimeInLocalTime: Optional[str] = Field(None, description="Approximate location date time")
    DataSource: Optional[str] = Field(None, description="Data source")
    MPTrackingRequestID: Optional[str] = Field(None, description="Tracking request ID")
    Locator: Optional[str] = Field(None, description="Locator")