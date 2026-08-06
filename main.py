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

    # Display Registered Agents
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

    # Register Character
    character_agent.add_character(bipo)

    # Add Keyframes
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

    print("\nAnalyzing First Keyframe...")
    print("---------------------------")

    result = vision_agent.analyze_keyframe(
        opening_scene.keyframes[0].image_path
    )

    print("\n=== AI Analysis ===")

    print(f"Character        : {result.character_name}")
    print(f"Pose             : {result.pose}")
    print(f"Expression       : {result.facial_expression}")
    print(f"Camera           : {result.camera_angle}")
    print(f"Movement         : {result.movement_direction}")
    print(f"Confidence       : {result.confidence}")

    print("\nAnimator Analysis")
    print("-----------------")

    print(f"Line of Action   : {result.line_of_action}")
    print(f"Balance          : {result.balance}")
    print(f"Silhouette       : {result.silhouette}")
    print(f"Squash/Stretch   : {result.squash_stretch}")
    print(f"Anticipation     : {result.anticipation}")
    print(f"Follow Through   : {result.follow_through}")
    print(f"Appeal           : {result.appeal}")
    print(f"Staging          : {result.staging}")

    print("\nObservations")
    print("------------")

    for observation in result.observations:
        print(f"- {observation}")

    print("\nProject Summary")
    print("---------------")
    print(f"Project : {project.name}")
    print(f"FPS     : {project.fps}")
    print(f"Scenes  : {len(project.scenes)}")
    print(f"Current : {opening_scene.name}")
    print(f"Frames  : {len(opening_scene.keyframes)}")

    print("8\nDay 9 Complete!")


if __name__ == "__main__":
    main()