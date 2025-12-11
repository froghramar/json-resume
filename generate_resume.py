
import json
import sys
from jsonschema import validate, ValidationError
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


# Load resume JSON and schema
with open('sample_resume.json', 'r', encoding='utf-8') as f:
    resume = json.load(f)
with open('resume_schema.json', 'r', encoding='utf-8') as f:
    schema = json.load(f)

# Validate resume
try:
    validate(instance=resume, schema=schema)
except ValidationError as e:
    print(f"Validation error: {e.message}")
    sys.exit(1)


def render_html(resume, template_path="resume_template.html"):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_path)
    return template.render(**resume)

def generate_pdf_from_html(html_content, output_path="resume.pdf"):
    HTML(string=html_content).write_pdf(output_path)

if __name__ == "__main__":
    html = render_html(resume)
    with open("resume.html", "w", encoding="utf-8") as f:
        f.write(html)
    generate_pdf_from_html(html)
