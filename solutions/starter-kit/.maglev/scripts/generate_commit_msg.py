#!/usr/bin/env python3
import subprocess
import sys
import os

def get_staged_files():
    try:
        output = subprocess.check_output(["git", "diff", "--cached", "--name-only"], text=True)
        return [f for f in output.splitlines() if f]
    except subprocess.CalledProcessError:
        return []

def classify_files(files):
    categories = {"CODE": [], "SPEC": [], "DOC": [], "CONFIG": [], "OTHER": []}
    for f in files:
        if f.startswith("specs/"):
            categories["SPEC"].append(f)
        elif f.startswith("docs/"):
            categories["DOC"].append(f)
        elif f.startswith(".maglev/") or f.startswith(".agent/"):
            categories["CONFIG"].append(f)
        elif "/src/" in f or f.endswith(".py") or f.endswith(".java") or f.endswith(".ts"):
            categories["CODE"].append(f)
        else:
            categories["OTHER"].append(f)
    return categories

def determine_sync_status(categories):
    has_code = len(categories["CODE"]) > 0
    has_spec = len(categories["SPEC"]) > 0
    
    if has_code and has_spec:
        return "✅ Synced (Code + Spec)"
    elif has_code and not has_spec:
        return "⚠️ Debt (Code Only - Warning: Did you forget to update specs?)"
    elif not has_code and has_spec:
        return "📄 Pure Spec (Documentation Update)"
    else:
        return "🔧 Config/Other"

def main():
    files = get_staged_files()
    if not files:
        print("No staged files found. Please 'git add' files first.")
        sys.exit(1)
        
    cats = classify_files(files)
    sync_status = determine_sync_status(cats)
    
    print("--- MAGLEV COMMIT CONTEXT ANALYZER ---")
    print(f"Staged Files Analysis:")
    for c, fs in cats.items():
        if fs:
            print(f"  {c}: {len(fs)} files")
            # print(f"    - {fs[0] if len(fs)==1 else str(len(fs)) + ' files'}")

    print(f"\n[SYNC STATUS]: {sync_status}")
    
    # Smart Inference
    inferred_tests = []
    for f in cats["CODE"]:
        if "test" in f.lower() and f.endswith(".py"):
            inferred_tests.append(f)
    if not inferred_tests and len(cats["OTHER"]) > 0:
        # Check other files for tests
        for f in cats["OTHER"]:
             if "test" in f.lower():
                 inferred_tests.append(f)

    print("\n[AI INSTRUCTIONS]")
    print(f"Detected Sync Status: {sync_status}")
    print("Based on the analysis above, generate a commit message using the Maglev Standard.")
    
    missing_info = []
    
    # 1. Test Evidence Check
    if cats["CODE"]:
        if inferred_tests:
            print(f"  ✅ Auto-Detected Tests: {', '.join(inferred_tests)}")
            print("     (Instruction: Fill 'Unit Test' field with these filenames)")
        else:
            print("  ❓ MISSING: No test files staged.")
            missing_info.append("Please provide the name of the Unit Test / Manual Verify that passed.")

    # 2. Spec Missing Check -> Drive Fallback Logic
    if "Debt" in sync_status:
        print("  ⚠️  DEBT DETECTED: Code changed but Spec didn't.")
        print("     Decision Point: Strict Mode vs Fallback Mode")
        missing_info.append("Option A (Recommended): Update Specs now.")
        missing_info.append("Option B (Fallback): Provide a REASON for this debt (e.g., 'Emergency Fix', 'PoC').")

    # 3. UI Check
    if any(f for f in cats["CODE"] if "ui" in f or "frontend" in f or "html" in f):
        print("  ❓ MISSING: UI files changed.")
        missing_info.append("Please provide visual evidence description (e.g. 'Button aligned').")

    if missing_info:
        print("\nACTION REQUIRED: Ask the user to clarify:")
        for q in missing_info:
             print(f"  - {q}")
        
    print("\n[TEMPLATE REFERENCE]")
    print(".maglev/protocols/commit_standard.md")
    print("\n[FALLBACK INSTRUCTION]")
    print("If user chooses Option B, append this to the message:")
    print("## ⚠️ Fallback")
    print("- [Debt]: {User_Reason}")

if __name__ == "__main__":
    main()
