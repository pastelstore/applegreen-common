import httpx

from fastapi import HTTPException

from applegreen_common.constant.constant import STORE_API_URI


async def is_store_owner(store_id: str, token: str) -> bool:
    """
    판매자의 상점인지 확인(store id 위변조 방지)
    """
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{STORE_API_URI}/stores/{store_id}", headers=headers)
            response.raise_for_status()  # HTTP 상태 코드 오류 발생 시 예외 처리

        if response.status_code == 200:
            return True

    except httpx.HTTPStatusError:
        raise HTTPException(status_code=403, detail="Unauthorized access.")

    except httpx.ConnectError:
        raise HTTPException(status_code=502, detail="Failed to connect to store service.")

    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Store service request timed out.")

    except httpx.RequestError:
        raise HTTPException(status_code=500, detail="An error occurred while requesting store service.")

    return False
