from sqlalchemy import text

def test_delete_teacher(session):
    email = "test_delete_teacher@example.com"
    
    session.execute(text("DELETE FROM teachers WHERE email = :email"), {"email": email})
    session.commit()
    
    teacher_id = session.execute(
        text("INSERT INTO teachers (name, email) VALUES (:name, :email) RETURNING id"),
        {"name": "Test Teacher", "email": email}
    ).scalar_one()
    session.commit()
    
    deleted = session.execute(
        text("DELETE FROM teachers WHERE id = :id"), {"id": teacher_id}
    ).rowcount
    session.commit()
    
    assert deleted == 1
    
    remaining = session.execute(
        text("SELECT count(*) FROM teachers WHERE id = :id"), {"id": teacher_id}
    ).scalar_one()
    assert remaining == 0

    