
from fastapi import FastAPI, File, HTTPException, UploadFile
from pandas.errors import EmptyDataError, ParserError

from app.analyzer import DataAnalyzer
from app.reader import CSVReader
from app.service import AnalysisService


app = FastAPI(
    title="DataLens API",
    description="API para análise de qualidade de dados",
    version="0.1.0"
)

reader = CSVReader()
analyzer = DataAnalyzer()
service = AnalysisService(reader, analyzer)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyses")
def create_analysis(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="O arquivo precisa ser CSV."
        )

    content = file.file.read()

    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="O arquivo excede 5 MB."
        )

    try:
        result = service.analyze_bytes(content)

    except (EmptyDataError, ParserError, UnicodeError, ValueError):
        raise HTTPException(
            status_code=422,
            detail="Não foi possível analisar o CSV."
        )

    return {
        "filename": file.filename,
        "analysis": result
    }
