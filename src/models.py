class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
