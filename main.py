from fastapi import FastAPI
from typing import Optional
from db import Database

# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# origins = [
# 	"http://localhost:3000"
# ]
#
# app.add_middleware(
# 	CORSMiddleware,
# 	allow_origins=origins,
# 	allow_credentials=True,
# 	allow_methods=["*"],
# 	allow_headers=["*"],
# )


@app.get("/query_books")
async def get_books(search_string: Optional[str] = None, fields: Optional[str] = None):
	if search_string and fields:
		fields_tuple = tuple(fields.split(","))

		db = Database()
		result = db.query_books(search_string, fields_tuple)
		return result
	else:
		return {"error": "You must provide a search string and at least one field to search."}
