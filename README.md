# Resume Tailoring Agent

A local Python CLI agent that uses your `resume_agent.md` instructions to:
1. Read a LaTeX resume.
2. Read a JD from TXT/MD/PDF.
3. Perform the requested gap analysis.
4. Generate the full tailored LaTeX resume.
5. Save the complete response and extracted LaTeX output.

## 1. Requirements

- Python 3.10+
- An OpenAI API key
- A `.tex` resume
- A JD in `.txt`, `.md`, or `.pdf`

## 2. Create virtual environment (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## 4. Configure API key

Copy `.env.example` to `.env` and put your API key in it:

```text
OPENAI_API_KEY=your_real_key
OPENAI_MODEL=gpt-5.6-luna
```

Never commit `.env` to Git.

## 5. Add input files

Put your files in `input/`:

```text
input/
  resume.tex
  jd.pdf
```

The resume must be `.tex` because the agent is designed to preserve the existing LaTeX structure.

## 6. Run

From the project root:

```powershell
python -m app.main --resume input/resume.tex --jd input/jd.pdf
```

Or:

```powershell
.\.venv\Scripts\python.exe -m app.main --resume input/resume.tex --jd input/jd.pdf
```

## 7. Output

The agent creates:

```text
output/
  agent_response.md
  tailored_resume.tex
```

`agent_response.md` contains the full six-section analysis requested by the prompt.

`tailored_resume.tex` contains the extracted final LaTeX block.

## 8. Important

This first version does not automatically compile the LaTeX into PDF. Once the agent is working correctly, add a LaTeX compilation/validation step as the next stage.
