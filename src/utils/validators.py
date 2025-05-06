import re
from config.app_config import MAX_UPLOAD_SIZE_MB

def validate_password(password):
    """Validate password meets security requirements."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"
    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one number"
    return True, None

def validate_email(email):
    """Validate email format."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_signup_fields(name, email, password, confirm_password):
    """Validate all signup form fields."""
    if not all([name, email, password, confirm_password]):
        return False, "Please fill in all fields"
        
    if not validate_email(email):
        return False, "Please enter a valid email address"
        
    if password != confirm_password:
        return False, "Passwords do not match"
        
    is_valid, error_msg = validate_password(password)
    if not is_valid:
        return False, error_msg
        
    return True, None

def validate_pdf_file(file):
    """Validate PDF file size and type."""
    if not file:
        return False, "No file uploaded"
        
    # Check file size
    file_size_mb = file.size / (1024 * 1024)
    if file_size_mb > MAX_UPLOAD_SIZE_MB:
        return False, f"File size ({file_size_mb:.1f}MB) exceeds the {MAX_UPLOAD_SIZE_MB}MB limit"
        
    # Check file type
    if file.type != 'application/pdf':
        return False, "Invalid file type. Please upload a PDF file"
        
    return True, None

def validate_pdf_content(text):
    """Validate if the PDF content appears to be a medical report."""
    # Common medical report indicators
    medical_terms = [
        'blood', 'test', 'report', 'laboratory', 'lab', 'patient', 'specimen',
        'reference range', 'analysis', 'results', 'medical', 'diagnostic',
        'hemoglobin', 'wbc', 'rbc', 'platelet', 'glucose', 'creatinine'
    ]
    
    # Validate minimum text length
    if len(text.strip()) < 50:
        return False, "Extracted text is too short. Please ensure the PDF contains valid text."
    
    # Check for medical terms
    text_lower = text.lower()
    term_matches = sum(1 for term in medical_terms if term in text_lower)
    
    if term_matches < 3:
        return False, "The uploaded file doesn't appear to be a medical report. Please upload a valid medical report."
    
    return True, None