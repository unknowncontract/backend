from src.core.config import config
import httpx

class MoltiService:
  async def getLocalePrice(self, LAWD_CD: str, DEAL_YMD: str):
    result = await self.getCurrentPrice(LAWD_CD, DEAL_YMD)

    return result

  async def getCurrentPrice(self, LAWD_CD: str, DEAL_YMD: str):
    serviceKey = config.molti_encoding
    params = {
      "LAWD_CD": LAWD_CD,
      "DEAL_YMD": DEAL_YMD,
      "serviceKey": serviceKey
    }

    response = httpx.get(config.molti_url, params=params)

    return response