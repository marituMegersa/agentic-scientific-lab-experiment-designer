from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.scientific_lab_experiment_designer.schemas import AgenticScientificLabExperimentDesignerSessionCreate, AgenticScientificLabExperimentDesignerSessionResponse
from app.domain.scientific_lab_experiment_designer.service import AgenticScientificLabExperimentDesignerService

router = APIRouter(prefix="/api/v1/scientific_lab_experiment_designer", tags=["Agentic Scientific Lab Experiment Designer Domain"])

@router.post("/sessions", response_model=AgenticScientificLabExperimentDesignerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticScientificLabExperimentDesignerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Scientific Lab Experiment Designer.
    """
    return AgenticScientificLabExperimentDesignerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticScientificLabExperimentDesignerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticScientificLabExperimentDesignerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
