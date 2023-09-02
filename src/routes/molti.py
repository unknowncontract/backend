from src.services.molti_service import MoltiService
from dependency_injector.wiring import Provide, inject
from src.core.container import Container
from fastapi import APIRouter, Depends
import xmltodict
import json

router = APIRouter(
    prefix="/molti",
    tags=['molti']
)

@router.get("")
@inject
async def findLocalePrice(
  LAWD_CD: str,
  DEAL_YMD: str,
  service: MoltiService = Depends(Provide[Container.molti_service])
):
  result = await service.getLocalePrice(LAWD_CD, DEAL_YMD)
  jsonString = json.dumps(xmltodict.parse(result.text))

  return json.loads(jsonString)