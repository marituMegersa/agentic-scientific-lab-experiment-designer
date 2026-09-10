from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.scientific_lab_experiment_designer.models import AgenticScientificLabExperimentDesignerSession, AgenticScientificLabExperimentDesignerItem
from app.domain.scientific_lab_experiment_designer.schemas import AgenticScientificLabExperimentDesignerSessionCreate, AgenticScientificLabExperimentDesignerItemCreate

class AgenticScientificLabExperimentDesignerService:
    @staticmethod
    def create_session(db: Session, data: AgenticScientificLabExperimentDesignerSessionCreate) -> AgenticScientificLabExperimentDesignerSession:
        db_obj = AgenticScientificLabExperimentDesignerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticScientificLabExperimentDesignerSession:
        return db.query(AgenticScientificLabExperimentDesignerSession).filter(AgenticScientificLabExperimentDesignerSession.id == session_id).first()
