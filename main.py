from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from rag.rag_pipeline import rag_pipeline

app = FastAPI()

# Enable CORS so frontend (HTML/JS) can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠ In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search(query: str):
    try:
        results = rag_pipeline(
            file_path="Data/enriched_properties.csv",
            query=query
        )
        return JSONResponse(content=results)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
