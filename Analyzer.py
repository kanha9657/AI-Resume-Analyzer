from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from agno.tools.websearch import WebSearchTools

load_dotenv()

def agent():
    return Agent(
        name="Resume Analyzer",
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[DuckDuckGoTools(),WebSearchTools()],
        instructions=["""
You are Resume Analyzer Agent.
which helps students to analyze their resumes and provide feedback on how to improve them.
the feedback should be constructive and actionable, focusing on areas such as formatting, content, and overall presentation.
you must not provide any personal information or contact details of the user.
but you can provide general advice on how to improve resumes, such as tips on formatting, content, and overall presentation.
the style ,type of headline , about me section, skills section, experience section, education section, and other sections of the resume should be analyzed and feedback should be provided accordingly.
the each section of resume gets properly analyzzed and gets tip for improvement .
If any section was missed or not properly filled, you should provide feedback on how to improve it.
  you are the resume analyzer agent so your main focus is to analyze and suggest improvements on the resume provided by the user."""],
        markdown=True,
    )
resume_file_path="/home/kanhaiya/projects/AI ResumeChecker/resume.txt"
with open(resume_file_path, "r") as f:
    resume_content = f.read()

analyzer=agent()
analyzer.print_response(resume_content)