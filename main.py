from kernel.animation_kernel import AnimationKernel

from agents.director.director_agent import DirectorAgent
from agents.project.project_agent import ProjectAgent
from agents.character.character_agent import CharacterAgent
from agents.vision.vision_agent import VisionAgent
from agents.reference.reference_agent import ReferenceAgent
from agents.motion.motion_agent import MotionAgent

from providers.gemini_vision_provider import GeminiVisionProvider

from core.character_dna import CharacterDNA


def main():
    print("=" * 50)
    print("      INBETWEENER AI")
    print("        Day 11")
    print("=" * 50)

    # Kernel
    kernel = AnimationKernel()

    # Provider
    vision_provider = GeminiVisionProvider()

    # Agents
    director = DirectorAgent()
    project_agent = ProjectAgent()
    character_agent = CharacterAgent()
    vision_agent = VisionAgent(vision_provider)
    reference_agent = ReferenceAgent()
    motion_agent = MotionAgent()

    # Register Agents
    kernel.register_agent(director)
    kernel.register_agent(project_agent)
    kernel.register_agent(character_agent)
    kernel.register_agent(vision_agent)
    kernel.register_agent(reference_agent)
    kernel.register_agent(motion_agent)

    kernel.list_agents()
    kernel.start()

    # Project
    project = project_agent.create_project(
        "Bipo Episode 1",
        fps=24
    )

    # Scene
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
    keyframe1 = project_agent.add_keyframe(
        opening_scene,
        frame_number=1,
        image_path="assets/keyframes/frame_0001.png",
        description="Standing"
    )

    keyframe2 = project_agent.add_keyframe(
        opening_scene,
        frame_number=24,
        image_path="assets/keyframes/frame_0024.png",
        description="Landing"
    )

    # Vision Analysis
    print("\nAnalyzing First Keyframe...")
    vision_result = vision_agent.analyze_keyframe(
        keyframe1.image_path
    )

    print(f"Pose: {vision_result.pose}")
    print(f"Expression: {vision_result.expression}")

    # Reference Analysis
    print("\nAnalyzing Reference Animation...")

    reference = reference_agent.analyze_reference(
        source="Reference Jump Animation",
        total_frames=48,
        fps=24
    )

    print(f"Reference: {reference.source}")

    # Motion Planning
    print("\nCreating Motion Blueprint...")
    print("----------------------------")

    motion_plan = motion_agent.create_motion_plan(
        keyframe1,
        keyframe2,
        reference
    )

    print("\n=== Motion Blueprint ===")

    print(f"Start Frame      : {motion_plan.start_frame}")
    print(f"End Frame        : {motion_plan.end_frame}")
    print(f"In-betweens      : {motion_plan.total_inbetweens}")
    print(f"Motion Type      : {motion_plan.motion_type}")
    print(f"Timing           : {motion_plan.timing}")
    print(f"Spacing          : {motion_plan.spacing}")
    print(f"Arc              : {motion_plan.arc}")

    print("\nMotion Notes")

    for note in motion_plan.notes:
        print(f"- {note}")

    print("\nPipeline Complete!")

    print("""
Keyframes
     │
     ▼
Vision Agent
     │
     ▼
Reference Agent
     │
     ▼
Motion Agent
     │
     ▼
Motion Blueprint
""")


if __name__ == "__main__":
    main()