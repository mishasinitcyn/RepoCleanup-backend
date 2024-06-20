from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import httpx

class IssueTag(BaseModel):
    id: int
    label: str
    
class Issue(BaseModel):
    id: int
    # issue_number: int
    # issue_url: str
    state: str
    # issue_author: str
    # issue_label: str
    title: str
    body: str

    class Config:
        extra = "ignore"

app = FastAPI()
origins = [
    "http://localhost:4200"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CLASSIFIER_URL = "http://127.0.0.1:8080/classify_spam"

@app.post("/classify_spam", response_model=List[IssueTag])
async def classify_spam(issues: List[Dict]):
    extracted_issues = []
    for issue in issues:
        extracted_issue = {
            "id": issue["id"],
            "state": issue["state"],
            "title": issue["title"],
            "body": issue["body"]
        }
        extracted_issues.append(extracted_issue)
    
    print(extracted_issues)
    async with httpx.AsyncClient() as client:
        response = await client.post(CLASSIFIER_URL, json=extracted_issues)
        response.raise_for_status()
        issue_tags = response.json()
    return issue_tags
    #return [{"id": 1, "label": "spam"}]

# uvicorn main:app --reload