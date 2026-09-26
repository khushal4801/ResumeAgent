import argparse
import os
import re
from pathlib import Path

from dotenv import load_dotenv

from app.agent import ResumeAgent
from app.file_parser import read_jd, read_text_file


def extract_latex_code(response_text: str) -> str | None:
    """Extract the first fenced LaTeX block from the model response."""
    match = re.search(
        r"```(?:latex|tex)?\s*(.*?)```",
        response_text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return match.group(1).strip() if match else None


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Tailor a LaTeX resume to a job description using an AI agent."
    )
    parser.add_argument(
        "--resume",
        required=True,
        help="Path to the source .tex resume",
    )
    parser.add_argument(
        "--jd",
        required=True,
        help="Path to JD (.txt, .md, or .pdf)",
    )
    parser.add_argument(
        "--prompt",
        default="prompts/resume_agent.md",
        help="Path to agent instructions",
    )
    parser.add_argument(
        "--output",
        default="output/agent_response.md",
        help="Path for the complete agent response",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        help="OpenAI model",
    )

    args = parser.parse_args()

    resume_path = Path(args.resume)
    if resume_path.suffix.lower() != ".tex":
        raise ValueError(
            "The resume must be a .tex file because the agent is instructed "
            "to preserve and edit the existing LaTeX structure."
        )

    resume_tex = read_text_file(str(resume_path))
    jd_text = read_jd(args.jd)

    if not resume_tex.strip():
        raise ValueError("Resume file is empty.")
    if not jd_text.strip():
        raise ValueError("JD file is empty.")

    print(f"Using model: {args.model}")
    print("Sending resume + JD to the resume agent...")

    agent = ResumeAgent(args.prompt, args.model)
    result = agent.tailor(resume_tex, jd_text)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result, encoding="utf-8")

    latex = extract_latex_code(result)
    if latex:
        latex_path = output_path.with_name("tailored_resume.tex")
        latex_path.write_text(latex, encoding="utf-8")
        print(f"Tailored LaTeX saved to: {latex_path}")

    print(f"Complete agent response saved to: {output_path}")
    print("Done.")


if __name__ == "__main__":
    main()
