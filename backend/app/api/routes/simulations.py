from fastapi import APIRouter
from backend.app.schemas.simulation import SimulationRequest
from backend.app.services.simulation_service import SimulationService

router = APIRouter(prefix="/simulations", tags=["Simulations"])
service = SimulationService()

@router.post("")
def simulate(request: SimulationRequest):
    return service.simulate(request)
