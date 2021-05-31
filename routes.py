from fastapi import APIRouter
from microblog import blog_routes

routes = APIRouter()

routes.include_router(blog_routes.router, prefix="/blog")
