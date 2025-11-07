"""
Part 1: Baseline Coverage Analysis with Branch Coverage
This script runs tests with both line and branch coverage collection.
"""
import subprocess
import json
import os
import xml.etree.ElementTree as ET
from pathlib import Path

def run_coverage():
    """Run pytest with coverage including branch coverage"""
    print("="*70)
    print("PART 1: BASELINE COVERAGE ANALYSIS (WITH BRANCH COVERAGE)")
    print("="*70)
    print("\nRunning tests with coverage...\n")
    
    # Create coverage reports directory
    os.makedirs("coverage_reports/html", exist_ok=True)
    
    # Run pytest with both line and branch coverage
    cmd = [
        "pytest",
        "tests/",
        "--cov=solutions",
        "--cov-branch",  # Enable branch coverage
        "--cov-report=term-missing",
        "--cov-report=html:coverage_reports/html",
        "--cov-report=xml:coverage_reports/coverage.xml",
        "--cov-report=json:coverage_reports/coverage.json",
        "-v"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    
    return result.returncode == 0

def parse_json_coverage():
    """Parse JSON coverage report to extract line and branch coverage"""
    json_path = "coverage_reports/coverage.json"
    
    if not os.path.exists(json_path):
        print(f"Warning: {json_path} not found")
        return None
    
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    coverage_data = {}
    
    # Extract file-level coverage
    for filename, file_data in data['files'].items():
        if 'solutions' in filename and filename.endswith('.py'):
            problem_name = os.path.basename(filename).replace('.py', '')
            
            summary = file_data['summary']
            
            coverage_data[problem_name] = {
                'line_coverage': summary.get('percent_covered', 0),
                'branch_coverage': summary.get('percent_covered_display', 'N/A'),
                'num_statements': summary.get('num_statements', 0),
                'missing_lines': summary.get('missing_lines', 0),
                'num_branches': summary.get('num_branches', 0),
                'missing_branches': summary.get('num_partial_branches', 0)
            }
    
    # Get totals
    totals = data['totals']
    coverage_data['TOTAL'] = {
        'line_coverage': totals.get('percent_covered', 0),
        'branch_coverage': totals.get('percent_covered_display', 'N/A'),
        'num_statements': totals.get('num_statements', 0),
        'missing_lines': totals.get('missing_lines', 0),
        'num_branches': totals.get('num_branches', 0),
        'missing_branches': totals.get('num_partial_branches', 0)
    }
    
    return coverage_data

def parse_xml_coverage():
    """Parse XML coverage report as backup for branch coverage"""
    xml_path = "coverage_reports/coverage.xml"
    
    if not os.path.exists(xml_path):
        print(f"Warning: {xml_path} not found")
        return None
    
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    coverage_data = {}
    
    # Parse each class (file)
    for package in root.findall('.//package'):
        for cls in package.findall('class'):
            filename = cls.get('filename', '')
            if 'solutions' in filename and filename.endswith('.py'):
                problem_name = os.path.basename(filename).replace('.py', '')
                
                lines = cls.findall('lines/line')
                total_lines = len(lines)
                covered_lines = sum(1 for line in lines if line.get('hits', '0') != '0')
                
                # Count branches
                total_branches = 0
                covered_branches = 0
                for line in lines:
                    branch = line.get('branch')
                    if branch == 'true':
                        total_branches += 1
                        # Branch coverage format: "covered/total"
                        condition_coverage = line.get('condition-coverage', '0% (0/0)')
                        if 'hits' in line.attrib and line.get('hits', '0') != '0':
                            covered_branches += 1
                
                line_cov = (covered_lines / total_lines * 100) if total_lines > 0 else 0
                branch_cov = (covered_branches / total_branches * 100) if total_branches > 0 else 100
                
                coverage_data[problem_name] = {
                    'line_coverage': round(line_cov, 1),
                    'branch_coverage': round(branch_cov, 1),
                    'num_statements': total_lines,
                    'missing_lines': total_lines - covered_lines,
                    'num_branches': total_branches,
                    'missing_branches': total_branches - covered_branches
                }
    
    return coverage_data

def generate_summary_table(coverage_data):
    """Generate a formatted summary table"""
    print("\n" + "="*70)
    print("DETAILED COVERAGE SUMMARY")
    print("="*70)
    print(f"{'Problem':<15} {'Line %':<10} {'Branch %':<12} {'Missing Lines':<15} {'Missing Branches':<15}")
    print("-"*70)
    
    problems = sorted([k for k in coverage_data.keys() if k != 'TOTAL'])
    
    for problem in problems:
        data = coverage_data[problem]
        line_cov = f"{data['line_coverage']:.1f}%"
        
        # Handle branch coverage
        branch_cov = data.get('branch_coverage', 'N/A')
        if isinstance(branch_cov, (int, float)):
            branch_cov = f"{branch_cov:.1f}%"
        
        missing_lines = data.get('missing_lines', 0)
        missing_branches = data.get('missing_branches', 0)
        
        print(f"{problem:<15} {line_cov:<10} {branch_cov:<12} {missing_lines:<15} {missing_branches:<15}")
    
    # Print total
    if 'TOTAL' in coverage_data:
        print("-"*70)
        data = coverage_data['TOTAL']
        line_cov = f"{data['line_coverage']:.1f}%"
        branch_cov = data.get('branch_coverage', 'N/A')
        if isinstance(branch_cov, (int, float)):
            branch_cov = f"{branch_cov:.1f}%"
        print(f"{'TOTAL':<15} {line_cov:<10} {branch_cov:<12} {data.get('missing_lines', 0):<15} {data.get('missing_branches', 0):<15}")
    
    print("="*70)

def generate_interpretations(coverage_data):
    """Generate one-line interpretations for each problem"""
    print("\n" + "="*70)
    print("COVERAGE INTERPRETATIONS")
    print("="*70)
    
    problems = sorted([k for k in coverage_data.keys() if k != 'TOTAL'])
    
    for problem in problems:
        data = coverage_data[problem]
        line_cov = data['line_coverage']
        branch_cov = data.get('branch_coverage', 0)
        if isinstance(branch_cov, str):
            branch_cov = 0  # Default if N/A
        
        # Generate interpretation
        interpretation = ""
        if line_cov < 50:
            interpretation = "Very low coverage - many code paths untested"
        elif line_cov < 70:
            interpretation = "Moderate coverage - significant testing gaps remain"
        elif line_cov < 85:
            interpretation = "Good coverage - some edge cases may be untested"
        else:
            interpretation = "Excellent coverage - most code paths tested"
        
        # Add branch-specific notes
        if isinstance(data.get('branch_coverage'), (int, float)):
            if branch_cov < line_cov - 10:
                interpretation += "; low branch coverage indicates untested conditionals"
            elif data.get('missing_branches', 0) > 0:
                interpretation += f"; {data['missing_branches']} branch(es) untested"
        
        print(f"{problem}: {interpretation}")
    
    print("="*70)

def main():
    # Run tests with coverage
    if not run_coverage():
        print("\n⚠ Warning: Some tests may have failed")
    
    # Try JSON first, fall back to XML
    coverage_data = parse_json_coverage()
    
    if not coverage_data:
        print("\nFalling back to XML parsing...")
        coverage_data = parse_xml_coverage()
    
    if coverage_data:
        generate_summary_table(coverage_data)
        generate_interpretations(coverage_data)
        
        print("\n" + "="*70)
        print("NEXT STEPS:")
        print("="*70)
        print("1. Review the coverage summary above")
        print("2. Open coverage_reports/html/index.html for detailed line-by-line analysis")
        print("3. Select 2 problems with lowest coverage for Part 2")
        print("4. Calculate selection metric: |%test_passed - %branch_coverage| × %test_passed")
        print("="*70)
    else:
        print("\n⚠ Error: Could not parse coverage data")

if __name__ == "__main__":
    main()