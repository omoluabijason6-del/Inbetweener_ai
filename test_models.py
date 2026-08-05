from core.task import Task
from core.project import Project
from core.character_dna import CharacterDNA

task = Task(id=1, name="Test Task")

project = Project(name="Demo")

dna = CharacterDNA(
    name="Bipo",
    head_shape="Circle",
    eye_shape="Oval",
    body_height=4,
    outline_style="Black",
    colors=["Yellow", "Blue", "White"]
)

print(task)
print(project)
print(dna)