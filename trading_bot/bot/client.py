import hmac, hashlib, time, requests, logging

logger = logging.getLogger("trading_bot")

class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self, key, secret):
        if not key or not secret:
            raise ValueError("Keys missing in env")
        self.key = key
        self.secret = secret
        self.header = {"X-MBX-APIKEY": self.key}

    def _sign(self, query):
        return hmac.new(
            self.secret.encode("utf-8"),
            query.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

    def send_signed_request(self, method, path, params=None):
        params = params or {}
        params["timestamp"] = int(time.time() * 1000)
        
        query = "&".join([f"{k}={v}" for k, v in params.items()])
        sig = self._sign(query)
        
        url = f"{self.BASE_URL}{path}?{query}&signature={sig}"
        logger.info(f"Req: {method} {path} | {params}")
        
        try:
            resp = requests.request(method, url, headers=self.header)
            data = resp.json()
            
            if resp.status_code != 200:
                logger.error(f"Err: {resp.status_code} | {data}")
                return {"error": True, "code": resp.status_code, "message": data}
            
            logger.info(f"Resp: {data}")
            return data
        except Exception as e:
            logger.exception(f"Fail: {str(e)}")
            return {"error": True, "message": str(e)}
