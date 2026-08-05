from kernel.animation_kernel import AnimationKernel

from agents.director.director_agent import DirectorAgent
from agents.project.project_agent import ProjectAgent
from agents.character.character_agent import CharacterAgent
from agents.vision.vision_agent import VisionAgent

from providers.mock_vision_provider import MockVisionProvider

from core.character_dna import CharacterDNA


def main():
    print("=" * 50)
    print("      INBETWEENER AI")
    print("         Day 9")
    print("=" * 50)

    # Create Kernel
    kernel = AnimationKernel()

    # Create AI Provider
    vision_provider = MockVisionProvider()

    # Create Agents
    director = DirectorAgent()
    project_agent = ProjectAgent()
    character_agent = CharacterAgent()
    vision_agent = VisionAgent(vision_provider)

    # Register Agents
    kernel.register_agent(director)
    kernel.register_agent(project_agent)
    kernel.register_agent(character_agent)
    kernel.register_agent(vision_agent)

    # Display Agents
    kernel.list_agents()

    # Start System
    kernel.start()

    # Create Project
    project = project_agent.create_project(
        "Bipo Episode 1",
        fps=24
    )

    # Create Scene
    opening_scene = project_agent.create_scene(
        "Opening Scene"
    )

    # Create Character
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

    character_agent.add_character(bipo)

    # Add Keyframes
    project_agent.add_keyframe(
        opening_scene,
        1,
        "assets/keyframes/frame_0001.png",
        "Standing"
    )

    project_agent.add_keyframe(
        opening_scene,
        12,
        "assets/keyframes/frame_0012.png",
        "Jump"
    )

    project_agent.add_keyframe(
        opening_scene,
        24,
        "assets/keyframes/frame_0024.png",
        "Landing"
    )

    print("\nAnalyzing First Keyframe...")
    print("---------------------------")

    result = vision_agent.analyze_keyframe(
        opening_scene.keyframes[0].image_path
    )

    print("\n=== AI Analysis ===")
    print(f"Character : {result.character_name}")
    print(f"Pose      : {result.pose}")
    print(f"Expression: {result.facial_expression}")
    print(f"Camera    : {result.camera_angle}")
    print(f"Movement  : {result.movement_direction}")
    print(f"Confidence: {result.confidence}")

    print("\nObservations")

    for observation in result.observations:
        print(f"- {observation}")


if __name__ == "__main__":
    main()