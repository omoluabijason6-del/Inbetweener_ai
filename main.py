from kernel.animation_kernel import AnimationKernel
from kernel.animation_kernel import AnimationKernel

from agents.director.director_agent import DirectorAgent
from agents.project.project_agent import ProjectAgent
from agents.character.character_agent import CharacterAgent
from core.character_dna import CharacterDNA


def main():
    print("=" * 50)
    print("      INBETWEENER AI")
    print("         Day 7")
    print("=" * 50)

    # Create Kernel
    kernel = AnimationKernel()

    # Create Agents
    director = DirectorAgent()
    project_agent = ProjectAgent()
    character_agent = CharacterAgent()

    # Register Agents
    kernel.register_agent(director)
    kernel.register_agent(project_agent)
    kernel.register_agent(character_agent)

    # Show Registered Agents
    kernel.list_agents()

    # Start System
    kernel.start()

    # Create Project
    project = project_agent.create_project(
        name="Bipo Episode 1",
        fps=24
    )

    # Create Scene
    opening_scene = project_agent.create_scene(
        "Opening Scene"
    )

    # Create Character DNA
    bipo = CharacterDNA(
        name="Bipo",
        head_shape="Circle",
        eye_shape="Oval",
        body_height=4,
        outline_style="Black",
        colors=[
            "Yellow",
            "Blue",
            "White"
        ]
    )

    # Load Character
    character_agent.add_character(bipo)

    # Add Keyframes
    project_agent.add_keyframe(
        opening_scene,
        frame_number=1,
        image_path="assets/keyframes/frame_0001.png",
        description="Bipo standing"
    )

    project_agent.add_keyframe(
        opening_scene,
        frame_number=12,
        image_path="assets/keyframes/frame_0012.png",
        description="Bipo jumps"
    )

    project_agent.add_keyframe(
        opening_scene,
        frame_number=24,
        image_path="assets/keyframes/frame_0024.png",
        description="Bipo lands"
    )

    print("\nProject")
    print("-------")
    print(project)

    print("\nScenes")
    print("------")

    for scene in project.scenes:
        print(f"\nScene: {scene.name}")

        for keyframe in scene.keyframes:
            print(
                f"Frame {keyframe.frame_number} | "
                f"{keyframe.description} | "
                f"{keyframe.image_path}"
            )


if __name__ == "__main__":
    main()