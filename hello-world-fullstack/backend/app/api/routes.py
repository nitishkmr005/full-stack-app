def hello_world_route():
    return {"message": "Hello, World!"}

def setup_routes(app):
    @app.get("/hello")
    async def read_root():
        return hello_world_route()