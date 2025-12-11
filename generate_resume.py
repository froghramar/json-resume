import json
import sys
from jsonschema import validate, ValidationError

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

# Generate formatted resume (plain text)
def generate_resume(resume):
    lines = []
    lines.append(f"Name: {resume['name']}")
    lines.append(f"Email: {resume['contact']['email']}")
    lines.append(f"Phone: {resume['contact']['phone']}")
    lines.append(f"Address: {resume['contact']['address']}")
    lines.append("")
    lines.append(f"Summary: {resume['summary']}")
    lines.append("")
    lines.append("Education:")
    for edu in resume['education']:
        lines.append(f"  - {edu['degree']} from {edu['institution']} ({edu['year']})")
    lines.append("")
    lines.append("Experience:")
    for exp in resume['experience']:
        lines.append(f"  - {exp['title']} at {exp['company']} ({exp['start']} to {exp['end']})")
        lines.append(f"    {exp['description']}")
    lines.append("")
    lines.append("Skills: " + ', '.join(resume['skills']))
    return '\n'.join(lines)

if __name__ == "__main__":
    print(generate_resume(resume))
