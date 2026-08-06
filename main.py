from kernel.animation_kernel import AnimationKernel

from agents.director.director_agent import DirectorAgent
from agents.project.project_agent import ProjectAgent
from agents.character.character_agent import CharacterAgent
from agents.vision.vision_agent import VisionAgent
from agents.reference.reference_agent import ReferenceAgent

from providers.mock_vision_provider import MockVisionProvider

from core.character_dna import CharacterDNA


def main():
    print("=" * 50)
    print("      INBETWEENER AI")
    print("        Day 10")
    print("=" * 50)

    # Kernel
    kernel = AnimationKernel()

    # Providers
    vision_provider = MockVisionProvider()

    # Agents
    director = DirectorAgent()
    project_agent = ProjectAgent()
    character_agent = CharacterAgent()
    vision_agent = VisionAgent(vision_provider)
    reference_agent = ReferenceAgent()

    # Register Agents
    kernel.register_agent(director)
    kernel.register_agent(project_agent)
    kernel.register_agent(character_agent)
    kernel.register_agent(vision_agent)
    kernel.register_agent(reference_agent)

    kernel.list_agents()

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

    # Character
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

    # Keyframes
    project_agent.add_keyframe(
        opening_scene,
        frame_number=1,
        image_path="assets/keyframes/frame_0001.png",
        description="Standing"
    )

    project_agent.add_keyframe(
        opening_scene,
        frame_number=12,
        image_path="assets/keyframes/frame_0012.png",
        description="Jump"
    )

    project_agent.add_keyframe(
        opening_scene,
        frame_number=24,
        image_path="assets/keyframes/frame_0024.png",
        description="Landing"
    )

    # Analyze First Keyframe
    print("\nAnalyzing First Keyframe...")
    print("---------------------------")

    keyframe_result = vision_agent.analyze_keyframe(
        opening_scene.keyframes[0].image_path
    )

    print("\nVision Result")
    print("-------------")

    print(f"Character : {keyframe_result.character_name}")
    print(f"Pose      : {keyframe_result.pose}")
    print(f"Expression: {keyframe_result.facial_expression}")

    # Analyze Reference Animation
    print("\nAnalyzing Reference Animation...")
    print("-------------------------------")

    reference = reference_agent.analyze_reference(
        source="Reference Jump Animation",
        total_frames=48,
        fps=24
    )

    print("\nReference Analysis")
    print("------------------")

    print(f"Source : {reference.source}")
    print(f"Frames : {reference.total_frames}")
    print(f"FPS    : {reference.fps}")

    print("\nAnimation Principles")

    for principle in reference.animation_principles:
        print(f"- {principle}")

    print("\nObservations")

    for observation in reference.observations:
        print(f"- {observation}")

    print("\nDay 10 Part 2 Complete!")


if __name__ == "__main__":
    main()