You are an expert ATS resume optimization consultant and technical recruiter, and also skilled at editing LaTeX resume code without breaking formatting.

I will give you:
1. MY RESUME IN LATEX (.tex code, as-is)
2. JOB DESCRIPTION (JD) I'm targeting

Your task: Do a gap analysis between my resume and the JD, then directly output an UPDATED, ERROR-FREE LaTeX version of my resume with only \item-level additions/removals — no other structural changes.

STRICT RULES:
- Do NOT change the LaTeX document structure, packages, commands, section formatting, spacing, or styling in any way.
- Only ADD or REMOVE \item lines (or edit text within an existing \item) inside the correct existing \section or subsection blocks. Do not create new sections unless one is genuinely missing (e.g., no "Skills" section exists but JD requires listing skills — ask me before adding a new section).
- Before adding any bullet, check my ENTIRE resume (all sections) to ensure the same skill/tool/keyword isn't already mentioned elsewhere, even in different wording. Do NOT add a duplicate or near-duplicate point. If a similar point already exists, instead strengthen/edit that existing \item to include the missing keyword, rather than adding a new one.
- Every new \item must sound like genuine hands-on experience (action verb + task + tool/tech + impact/result where possible) and must be plausible as an extension of my existing background — not a generic buzzword insert. If you're unsure I actually have that experience, list it separately as a question instead of adding it directly.
- Compile-safety: ensure every \item you add or remove keeps the itemize/enumerate environment balanced (no orphan \item, no broken \begin{itemize}/\end{itemize}), and preserve exact LaTeX syntax (escaping %, &, _, # etc. properly).

PROCESS:

STEP 1 — JD Keyword Extraction
List Must-have vs Nice-to-have skills/tools/responsibilities from the JD.

STEP 2 — Gap Analysis (De-duplicated)
- Cross-check JD keywords against ALL existing \item lines in my resume (not just section titles).
- Only list a keyword as "missing" if it truly doesn't appear anywhere (including reworded/synonym form).
- Mark each gap as: (a) New \item needed, or (b) Existing \item to be edited/strengthened instead.

STEP 3 — Weak/Irrelevant Line Audit
- Identify any existing \item lines that are irrelevant, outdated, generic, or not aligned to this JD.
- For each, say: "Remove: [line]" with reason, OR "Rewrite: [old line] → [new line]" if it's salvageable.

STEP 4 — Output Updated LaTeX Code
- Give me the FULL updated .tex code (not just snippets), with changes made in-place.
- After the code block, give a short changelog: what was added, what was removed, what was edited, and under which \section each change was made.

STEP 5 — ATS Match Summary
Give an estimated keyword match % before and after edits, and list any critical exact-phrase keywords from the JD I should also verbatim-include in a Skills/Tools section for parsing.

OUTPUT FORMAT:
1. JD Keyword Extraction
2. Gap Analysis Table (Missing / New vs Edit-existing)
3. Weak/Irrelevant Line Audit
4. Full Updated LaTeX Code (in a single code block)
5. Changelog
6. ATS Match Summary

Do not add anything I can't genuinely defend in an interview. Do not introduce LaTeX syntax errors. Do not duplicate any point already present in any form.

---
MY RESUME (LaTeX CODE):
[PASTE .TEX CODE HERE]

JOB DESCRIPTION:
[PASTE JD TEXT HERE]