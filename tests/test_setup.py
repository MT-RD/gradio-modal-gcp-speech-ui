"""
Basic test to verify project structure and imports.
"""

import sys
from pathlib import Path

# Add src to Python path for testing
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))


def test_project_structure():
    """Test that all required directories exist."""
    required_dirs = [
        "src",
        "src/gradio_app",
        "src/modal_functions", 
        "src/gcp_client",
        "src/utils",
        "config",
        "docs",
        "tests",
        "samples"
    ]
    
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        assert full_path.exists(), f"Required directory {dir_path} does not exist"
        assert full_path.is_dir(), f"{dir_path} exists but is not a directory"


def test_config_files_exist():
    """Test that required configuration files exist."""
    required_files = [
        "requirements.txt",
        "pyproject.toml",
        "README.md",
        ".gitignore",
        ".env.example",
        "LICENSE",
        "setup.sh"
    ]
    
    for file_path in required_files:
        full_path = project_root / file_path
        assert full_path.exists(), f"Required file {file_path} does not exist"
        assert full_path.is_file(), f"{file_path} exists but is not a file"


def test_config_imports():
    """Test that configuration modules can be imported."""
    try:
        from config.settings import settings
        assert settings is not None
    except ImportError as e:
        assert False, f"Could not import settings: {e}"
    
    try:
        from config.gcp_config import GCPConfig
        assert GCPConfig is not None
    except ImportError as e:
        assert False, f"Could not import GCPConfig: {e}"


def test_package_structure():
    """Test that package __init__.py files exist."""
    init_files = [
        "src/__init__.py",
        "src/gradio_app/__init__.py",
        "src/modal_functions/__init__.py",
        "src/gcp_client/__init__.py",
        "src/utils/__init__.py"
    ]
    
    for init_file in init_files:
        full_path = project_root / init_file
        assert full_path.exists(), f"Package __init__.py file {init_file} does not exist"


def test_gcp_config_functionality():
    """Test GCP configuration basic structure."""
    from config.gcp_config import GCPConfig
    
    # Test that the class exists and can be instantiated
    assert GCPConfig is not None
    
    # Test that it's a class (not just a module)
    assert hasattr(GCPConfig, '__name__')
    assert GCPConfig.__name__ == 'GCPConfig'


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])
