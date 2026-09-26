from pathlib import Path
from openai import OpenAI

class ResumeAgent:
    def __init__(self, prompt_path: str, model: str):
        self.client = OpenAI()
        self.model = model
        self.instructions = Path(prompt_path).read_text(encoding="utf-8")

    def tailor(self, resume_tex: str, jd_text: str) -> str:
        user_input = f"""
IMPORTANT INPUT RULES:
- The resume below is the candidate's source-of-truth LaTeX.
- The JD below is the target job description.
- Follow the instructions in your agent instructions exactly.
- Do not invent experience.
- Return the six requested output sections.

====================
MY RESUME (LATEX)
====================
{resume_tex}

====================
JOB DESCRIPTION
====================
{jd_text}
"""

        response = self.client.responses.create(
            model=self.model,
            instructions=self.instructions,
            input=user_input,
        )

        return response.output_text
