import pytest
import os
import ast

def test_python_syntax_integrity():
    # Recursively find all python files in the directory
    base_dir = os.path.dirname(os.path.dirname(__file__))
    python_files = []
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
                
    # Assert that all files compile into valid ASTs without SyntaxErrors
    for py_file in python_files:
        with open(py_file, 'r', encoding='utf-8') as f:
            source = f.read()
        try:
            ast.parse(source, filename=py_file)
        except SyntaxError as e:
            pytest.fail(f"Syntax error in {py_file}: {e}")
