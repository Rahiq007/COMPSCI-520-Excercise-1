"""
Exercise 3 Setup Script
Creates the complete directory structure and copies necessary files
"""

import os
import shutil
from pathlib import Path

def create_directory_structure():
    """Create all necessary directories for Exercise 3"""
    
    directories = [
        'prompts',
        'specifications',
        'tests',
        'coverage_reports',
        'solutions'  # We'll copy from Exercise 2
    ]
    
    print("="*80)
    print("CREATING EXERCISE 3 DIRECTORY STRUCTURE")
    print("="*80)
    
    for dir_name in directories:
        os.makedirs(dir_name, exist_ok=True)
        print(f"✅ Created: {dir_name}/")
    
    print("\n" + "="*80)
    print("DIRECTORY STRUCTURE CREATED")
    print("="*80)

def copy_solutions_from_exercise2():
    """Copy solution files from Exercise 2"""
    
    print("\n" + "="*80)
    print("COPYING SOLUTIONS FROM EXERCISE 2")
    print("="*80)
    
    exercise2_path = input("\nEnter path to your Exercise 2 directory: ").strip()
    
    if not os.path.exists(exercise2_path):
        print(f"❌ Path not found: {exercise2_path}")
        print("⚠️  You'll need to copy solutions manually later")
        return False
    
    solutions_src = os.path.join(exercise2_path, 'solutions')
    
    if not os.path.exists(solutions_src):
        print(f"❌ Solutions directory not found: {solutions_src}")
        print("⚠️  You'll need to copy solutions manually later")
        return False
    
    # Copy HumanEval_54 and HumanEval_2
    problems = ['HumanEval_54.py', 'HumanEval_2.py']
    
    for problem_file in problems:
        src_file = os.path.join(solutions_src, problem_file)
        dst_file = os.path.join('solutions', problem_file)
        
        if os.path.exists(src_file):
            shutil.copy2(src_file, dst_file)
            print(f"✅ Copied: {problem_file}")
        else:
            print(f"❌ Not found: {problem_file}")
    
    return True

def create_gitignore():
    """Create .gitignore file"""
    
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
dist/
build/

# Virtual Environment
.venv/
venv/
ENV/

# Testing
.pytest_cache/
.coverage
htmlcov/
*.cover
.hypothesis/

# Coverage Reports
coverage_reports/*.html
coverage_reports/*.xml
!coverage_reports/README.md

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.bak
*_backup.py
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("\n✅ Created: .gitignore")

def create_coverage_readme():
    """Create README for coverage_reports directory"""
    
    readme_content = """# Coverage Reports

This directory contains HTML and XML coverage reports.

## Files (gitignored):
- `*.html` - Human-readable coverage reports
- `*.xml` - Machine-readable coverage data

## To regenerate:
```bash
pytest tests/test_HumanEval_54_spec_guided.py --cov=solutions --cov-branch --cov-report=html -v
```

Open `htmlcov/index.html` in your browser to view.
"""
    
    os.makedirs('coverage_reports', exist_ok=True)
    with open('coverage_reports/README.md', 'w') as f:
        f.write(readme_content)
    
    print("✅ Created: coverage_reports/README.md")

def create_project_structure_doc():
    """Create a document showing the project structure"""
    
    structure = """# Exercise 3 Project Structure

```
exercise3/
├── README.md                              # Main documentation
├── exercise3_workflow.py                  # Interactive guide
├── .gitignore                            # Git ignore rules
│
├── PHASE 1: Problem Description Extraction
├── extract_problem_descriptions.py
├── problem_descriptions.json
│
├── PHASE 2: Specification Generation (Part 1)
├── part1_generate_spec_prompts.py
├── prompts/
│   ├── spec_generation_HumanEval_54.txt
│   └── spec_generation_HumanEval_2.txt
├── specifications/
│   ├── HumanEval_54_generated.py         # LLM output
│   ├── HumanEval_54_corrected.py         # After review
│   ├── HumanEval_2_generated.py
│   └── HumanEval_2_corrected.py
│
├── PHASE 3: Specification Evaluation
├── spec_evaluation_template.py
│
├── PHASE 4: Test Generation (Part 2)
├── part2_generate_test_prompts.py
├── prompts/
│   ├── test_generation_HumanEval_54.txt
│   └── test_generation_HumanEval_2.txt
├── tests/
│   ├── test_HumanEval_54_spec_guided.py
│   └── test_HumanEval_2_spec_guided.py
│
├── PHASE 5: Coverage Comparison
├── part2_compare_coverage.py
├── coverage_comparison_results.json
│
├── solutions/                             # From Exercise 2
│   ├── HumanEval_54.py
│   └── HumanEval_2.py
│
└── coverage_reports/                      # Generated reports
    ├── README.md
    └── *.html (gitignored)
```

## Workflow

1. **Setup**: Run `python exercise3_setup.py` (this script)
2. **Extract**: Run `python extract_problem_descriptions.py`
3. **Generate Specs**: Run `python part1_generate_spec_prompts.py`
4. **Use LLM**: Copy prompts to LLM, get specifications
5. **Evaluate**: Edit `spec_evaluation_template.py`
6. **Generate Tests**: Run `python part2_generate_test_prompts.py`
7. **Use LLM**: Copy prompts to LLM, get test cases
8. **Compare**: Run `python part2_compare_coverage.py`

## Files to Submit

### GitHub:
- All Python files
- All prompts
- All specifications (generated and corrected)
- All test files
- Solutions
- README.md

### PDF Report:
- Part 1: Prompts, accuracy, corrections
- Part 2: Test prompts, coverage table, insights
"""
    
    with open('PROJECT_STRUCTURE.md', 'w') as f:
        f.write(structure)
    
    print("✅ Created: PROJECT_STRUCTURE.md")

def main():
    print("="*80)
    print("EXERCISE 3 SETUP")
    print("="*80)
    print("\nThis script will:")
    print("  1. Create directory structure")
    print("  2. Copy solutions from Exercise 2")
    print("  3. Create .gitignore")
    print("  4. Create documentation files")
    
    response = input("\nProceed? (y/n): ").strip().lower()
    if response != 'y':
        print("Setup cancelled.")
        return
    
    # Create directories
    create_directory_structure()
    
    # Copy solutions
    copy_solutions_from_exercise2()
    
    # Create supporting files
    create_gitignore()
    create_coverage_readme()
    create_project_structure_doc()
    
    print("\n" + "="*80)
    print("SETUP COMPLETE!")
    print("="*80)
    
    print("\n📁 Directory structure created:")
    print("   ✅ prompts/")
    print("   ✅ specifications/")
    print("   ✅ tests/")
    print("   ✅ coverage_reports/")
    print("   ✅ solutions/")
    
    print("\n📄 Files created:")
    print("   ✅ .gitignore")
    print("   ✅ PROJECT_STRUCTURE.md")
    print("   ✅ coverage_reports/README.md")
    
    print("\n🚀 Next steps:")
    print("   1. Review README.md for complete instructions")
    print("   2. Run: python exercise3_workflow.py")
    print("   3. Or follow manual steps in README.md")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    main()