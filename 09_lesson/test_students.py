from sqlalchemy import text

def test_add_student(session):
    email = "test_add_student@example.com"
    session.execute(text("DELETE FROM students WHERE email = :email"), {"email": email})
    session.commit()
    
    try:
        result = session.execute(
            text("INSERT INTO students (name, email) VALUES (:name, :email) RETURNING id"),
            {"name": "Test Student", "email": email}
        )
        student_id = result.scalar_one()
        session.commit()
        
        row = session.execute(text("SELECT name, email FROM students WHERE id = :id"), {"id": student_id}).one()
        assert row.email == email
        assert row.name == "Test Student"
    finally:
        session.execute(text("DELETE FROM students WHERE email = :email"), {"email": email})
        session.commit()

        