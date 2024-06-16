import asyncio
from base64 import b64encode

from httpx import AsyncClient, AsyncHTTPTransport, HTTPStatusError


class TokenManager:
    """Manages Logto API token."""

    def __init__(
        self,
        logto_endpoint: str,
        m2m_app_id: str,
        m2m_app_secret: str,
    ) -> None:
        self.logto_endpoint = logto_endpoint
        self.m2m_app_id = m2m_app_id
        self.m2m_app_secret = m2m_app_secret
        self.token_info: dict[str, str] = {
            "token_type": "",
            "access_token": "",
        }

    async def fetch_token_info(self) -> dict:
        """Fetches token info from Logto."""
        async with AsyncClient(
            transport=AsyncHTTPTransport(retries=10),
            base_url=self.logto_endpoint,
        ) as client:
            response = await client.post(
                "/oidc/token",
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": f"Basic {b64encode(f'{self.m2m_app_id}:{self.m2m_app_secret}'.encode()).decode()}",
                },
                data={
                    "grant_type": "client_credentials",
                    "resource": "https://default.logto.app/api",
                    "scope": "all",
                },
            )
        try:
            response.raise_for_status()
        except HTTPStatusError as e:
            print(
                "\n\nFailed to fetch Logto Management API token:\n------\n",
                response.json(),
                end="\n\n",
            )
            raise e
        return response.json()

    async def refresh_token_periodically(self):
        """Refreshes token periodically."""
        while True:
            self.token_info = await self.fetch_token_info()
            await asyncio.sleep(
                3000
            )  # Refresh every 3000 seconds, for a buffer before 3600 seconds expiry

    def get_auth_header(self) -> str:
        """Returns the Logto authorization header."""
        return f"{self.token_info['token_type']} {self.token_info['access_token']}"
