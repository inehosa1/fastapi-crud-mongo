from fastapi import Request
from config.jwt import validate_token
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse

class VerifyTokenRoute(APIRoute):
    
    def get_route_handler(self):
        original_route = super().get_route_handler()
        
        async def verify_token_middleware(request:Request):
            try:
                token = request.headers["authorization"].split(" ")[1]
            except:
                return JSONResponse(content={"message": "Token not found"}, status_code=401)
            
            validation_response = validate_token(token, output=False)
            
            if validation_response == None:
                return await original_route(request)
            else:
                return validation_response
            
        return verify_token_middleware
            