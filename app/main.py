from fastapi import FastAPI

app = FastAPI(
    title="InterVerse API",
    version="0.1.0",
    description="Cloud backend for InterVerseSG, Unreal Engine, and Meta Quest.",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "InterVerse API",
        "version": "0.1.0",
        "status": "online",
    }


@app.get("/healthz")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
