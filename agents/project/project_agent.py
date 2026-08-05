from core.project import Project
from core.scene import Scene


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

    def create_scene(self, name):
        """
        Create a new scene inside the current project.
        """

        if self.current_project is None:
            raise RuntimeError("No project loaded.")

        scene = Scene(name=name)

        self.current_project.scenes.append(scene)

        print(f"[Project] Scene '{name}' created.")

        return scene

    def get_project(self):
        return self.current_project
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