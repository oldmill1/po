"""
Library generator implementation
"""

import os
import subprocess
import sys
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
        package_name = f"{self.project_name.replace('-', '_').replace(' ', '_').lower()}_lib"
        main_module_path = self.project_path / package_name / "__main__.py"
        if main_module_path.exists():
            os.chmod(main_module_path, 0o755)
            
        # Initialize git repository
        self._init_git_repo()
        
        # Set up virtual environment and install package
        self._setup_venv_and_install()
    
    def _init_git_repo(self):
        """Initialize git repository and make initial commit"""
        try:
            # Change to project directory
            original_cwd = os.getcwd()
            os.chdir(self.project_path)
            
            # Initialize git repository
            subprocess.run(['git', 'init'], check=True, capture_output=True)
            
            # Add all files
            subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
            
            # Make initial commit
            subprocess.run(['git', 'commit', '-m', 'init commit'], check=True, capture_output=True)
            
            # Change back to original directory
            os.chdir(original_cwd)
            
        except subprocess.CalledProcessError as e:
            # Git not available or other error - continue without git
            pass
        except Exception:
            # Any other error - continue without git
            pass
    
    def _setup_venv_and_install(self):
        """Set up virtual environment and install the package"""
        try:
            # Change to project directory
            original_cwd = os.getcwd()
            os.chdir(self.project_path)
            
            # Create virtual environment
            subprocess.run(['python3', '-m', 'venv', '.venv'], check=True, capture_output=True)
            
            # Activate virtual environment and install package
            if os.name == 'nt':  # Windows
                activate_script = '.venv\\Scripts\\activate.bat'
                pip_path = '.venv\\Scripts\\pip'
            else:  # Unix/Linux/macOS
                activate_script = '.venv/bin/activate'
                pip_path = '.venv/bin/pip'
            
            # Install the package in editable mode
            subprocess.run([pip_path, 'install', '-e', '.'], check=True, capture_output=True)
            
            # Change back to original directory
            os.chdir(original_cwd)
            
        except subprocess.CalledProcessError as e:
            # Virtual environment creation or installation failed - continue without it
            pass
        except Exception:
            # Any other error - continue without virtual environment
            pass
