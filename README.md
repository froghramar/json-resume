# JSON Resume Generator

This project generates a formatted resume from a JSON file, with schema validation.

## Setup Instructions

1. **Clone or download the repository.**

2. **Create and activate a virtual environment:**

   On Windows (bash):
   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the generator script:**
   ```bash
   python generate_resume.py
   ```

## Files
- `sample_resume.json`: Example resume data.
- `resume_schema.json`: JSON schema for validation.
- `generate_resume.py`: Script to validate and generate resume.

## Customization
- Edit `sample_resume.json` to update your resume details.
- The script outputs a plain text resume. For HTML or other formats, ask for enhancements!
