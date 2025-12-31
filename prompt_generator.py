from langchain_core.prompts import PromptTemplate

research_template = PromptTemplate(
    input_variables=[
        "domain",
        "topic",
        "section",
        "style",
        "year_range",
        "citation_style"
    ],
    template="""
You are an expert academic researcher in {domain}.

TASK:
Write ONLY the {section} section of a research paper on the topic:
"{topic}"

STYLE:
- Writing style: {style}
- Reference year range: {year_range}

STRICT RULES:
- Do NOT include bibliography
- Do NOT include references
- Do NOT add section headings
- Do NOT cite papers explicitly
- Write in continuous academic paragraphs
Output ONLY the requested content.
"""
)

research_template.save("template.json")