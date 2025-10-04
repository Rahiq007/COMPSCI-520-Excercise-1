import json

# Load generated code
with open('generated_code/all_generated_code.json', 'r') as f:
    generated_codes = json.load(f)

# Look at first few examples
print("="*70)
print("INSPECTING GENERATED CODE")
print("="*70)

# Check first problem with baseline strategy
for i, (key, data) in enumerate(list(generated_codes.items())[:2]):
    print(f"\n{i+1}. Key: {key}")
    print(f"Problem: {data['problem_id']}")
    print(f"Strategy: {data['strategy']}")
    print(f"LLM: {data['llm']}")
    print("\nExtracted Code:")
    print("-" * 70)
    print(data['extracted_code'][:500])
    print("-" * 70)
    print("\nFull Response Preview:")
    print("-" * 70)
    print(data['response'][:500])
    print("-" * 70)