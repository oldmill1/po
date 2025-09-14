"""
CLI interface for po
"""

import os
import sys
from pathlib import Path
import click
from .generator import LibraryGenerator


@click.command()
@click.option('--project-name', '-n', prompt='Project name', help='Name of the project to create')
@click.option('--output-dir', '-o', prompt='Output directory', default='~/dev', help='Directory where the project will be created')
def main(project_name, output_dir):
    """
    Generate a Python library with CLI entry point.
    
    This tool creates a complete Python library structure that can be installed
    with pip and used as a command-line tool.
    
    Examples:
        po -n my-tool                    # Creates in ~/dev directory (default)
        po -n my-tool -o ~/projects     # Creates in ~/projects directory
        po -n my-tool -o .              # Creates in current directory
        po -n my-tool -o ../new-proj    # Creates in ../new-proj directory
    """
    try:
        # Expand user home directory and resolve the path
        expanded_output_dir = os.path.expanduser(output_dir)
        generator = LibraryGenerator(project_name, expanded_output_dir)
        generator.generate()
        
        # Show the full path where the project was created
        project_path = Path(expanded_output_dir).resolve() / project_name
        click.echo(f"")
        click.echo(f"╔══════════════════════════════════════════════════════════════╗")
        click.echo(f"║                    🚀 LIBRARY GENERATED! 🚀                ║")
        click.echo(f"╚══════════════════════════════════════════════════════════════╝")
        click.echo(f"")
        click.echo(f"🎯 Project: {project_name}")
        click.echo(f"📂 Location: {project_path}")
        click.echo(f"")
        click.echo(f"🔧 AUTO-SETUP COMPLETE:")
        click.echo(f"   ✅ Virtual environment created (.venv)")
        click.echo(f"   ✅ Package installed in editable mode")
        click.echo(f"   ✅ Git repository initialized")
        click.echo(f"")
        click.echo(f"🎮 READY TO USE:")
        click.echo(f"   cd '{project_path}'")
        click.echo(f"   source .venv/bin/activate")
        click.echo(f"   {project_name} --help")
        click.echo(f"")
        click.echo(f"💡 Pro tip: Everything is set up and ready to go!")
        click.echo(f"   (Remember to push to remote when ready!)")
        click.echo(f"")
    except Exception as e:
        click.echo(f"❌ Error generating library: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
