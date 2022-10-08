from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from pyexpat import model
from sqlalchemy.orm import Session
import models, schemas

def create_event(db: Session, event: schemas.EventRequest):
    db_event = models.Event(name=event.name, completed=event.completed)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def read_events(db: Session, completed: bool):
    if completed is None:
        return db.query(models.Event).all()
    else:
        return db.query(models.Event).filter(models.Event.completed == completed).all()

def read_event(db: Session, id: int):
    return db.query(models.Event).filter(models.Event.id == id).first()

def update_event(db:Session, id: int, event: schemas.EventRequest):
    db_event = db.query(models.Event).filter(models.Event.id == id).first()
    if db_event is None:
        return None
    db.query(models.Event).filter(models.Event.id == id).update({
        'name': event.name,
        'completed': event.completed
    })
    db.commit()
    db.refresh(db_event)
    return db_event

def delete_event(db:Session, id: int):
    db_event = db.query(models.Event).filter(models.Event.id == id).first()
    if db_event is None:
        return None
    db.query(models.Event).filter(models.Event.id == id).delete()
    db.commit()
    return True
                   
