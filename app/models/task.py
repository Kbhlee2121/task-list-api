from flask import current_app
from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    # Default is not required
    completed_at = db.Column(db.DateTime, default=None, nullable=True)
    # ForeignKey to link Goal
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)
    # goal = db.relationship("Goal", back_populates='tasks')

    def to_dict(self):
        
        response_dict =  {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": bool(self.completed_at),
            }
        
        if self.goal_id:
            response_dict["goal_id"] = self.goal_id
        return response_dict