"""
Library generator implementation
"""

import os
from pathlib import Path
from .templates import get_templates


class LibraryGenerator:
    """Generates Python libraries with CLI entry points"""
    
    def __init__(self, project_name, output_dir="."):
        self.project_name = project_name
        self.output_dir = Path(output_dir)
        self.project_path = self.output_dir / project_name
        
    def generate(self):
        """Generate the complete library structure"""
        # Create project directory
        self.project_path.mkdir(parents=True, exist_ok=True)
        
        # Get templates
        templates = get_templates(self.project_name)
        
        # Generate all files
        for file_path, content in templates.items():
            full_path = self.project_path / file_path
            
            # Create parent directories if needed
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write file
            with open(full_path, 'w') as f:
                f.write(content)
                
        # Make the main module executable
        main_module_path = self.project_path / self.project_name / "__main__.py"
        if main_module_path.exists():
            os.chmod(main_module_path, 0o755)
