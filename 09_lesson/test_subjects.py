from sqlalchemy import text

def test_update_subject(session):
    original = "Lesson09_Original"
    updated = "Lesson09_Updated"
    
    session.execute(text("DELETE FROM subjects WHERE name IN (:o, :u)"), {"o": original, "u": updated})
    session.commit()
    
    try:
        subject_id = session.execute(
            text("INSERT INTO subjects (name) VALUES (:name) RETURNING id"),
            {"name": original}
        ).scalar_one()
        session.commit()
        
        updated_rows = session.execute(
            text("UPDATE subjects SET name = :new WHERE id = :id"),
            {"new": updated, "id": subject_id}
        ).rowcount
        session.commit()
        
        assert updated_rows == 1
        
        name_in_db = session.execute(
            text("SELECT name FROM subjects WHERE id = :id"), {"id": subject_id}
        ).scalar_one()
        assert name_in_db == updated
    finally:
        session.execute(text("DELETE FROM subjects WHERE id = :id"), {"id": subject_id})
        session.commit()

        