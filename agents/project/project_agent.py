from core.project import Project


class ProjectAgent:
    """
    Handles animation projects.
    """

    def __init__(self):
        self.name = "Project Agent"
        self.current_project = None

    def start(self):
        print("[Project] Ready.")

    def create_project(self, name, fps=24):
        self.current_project = Project(
            name=name,
            fps=fps
        )

        print(f"[Project] Created '{name}'")

        return self.current_project

    def get_project(self):
        return self.current_project