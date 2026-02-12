#!/usr/bin/env python3
import os
import argparse
import sys

# Configuration
IGNORE_DIRS = {
    'node_modules', '.git', '.idea', '.vscode', '__pycache__', 
    'dist', 'build', 'coverage', '.venv', 'venv'
}
ANCHOR_FILES = {
    'package.json', 'pom.xml', 'go.mod', 'Cargo.toml', 
    'requirements.txt', 'README.md', 'Dockerfile', 'Makefile'
}
DEFAULT_MAX_DEPTH = 5
DEFAULT_MAX_LINES = 200

def is_ignored(path):
    parts = path.split(os.sep)
    for part in parts:
        if part in IGNORE_DIRS:
            return True
    return False

def get_readme_summary(dir_path):
    readme_path = os.path.join(dir_path, 'README.md')
    if os.path.exists(readme_path):
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        return line[:100]  # First non-header line, truncated
                    if line and line.startswith('#') and len(line) > 2:
                         return line.lstrip('#').strip()[:100] # Fallback to header if description missing
        except Exception:
            pass
    return ""

def scan_project(root_dir, max_depth):
    structure = []
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # In-place modification to filter traversal
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith('.')]
        
        rel_path = os.path.relpath(dirpath, root_dir)
        if rel_path == '.':
            depth = 0
        else:
            depth = rel_path.count(os.sep) + 1

        if depth > max_depth:
            continue
            
        # Check for anchors
        anchors_found = [f for f in filenames if f in ANCHOR_FILES]
        
        # We record directory if it's Root, or has Anchors, or is a direct child of Root (to show structure)
        if depth == 0 or anchors_found or depth == 1:
            summary = get_readme_summary(dirpath)
            structure.append({
                'path': rel_path,
                'depth': depth,
                'name': os.path.basename(dirpath) if depth > 0 else 'ROOT',
                'anchors': anchors_found,
                'summary': summary
            })
            
    return structure

def estimate_tokens(structure):
    # Rough estimation: 1 line = ~10 tokens (Markdown overhead + content)
    line_count = len(structure) * 2 # Safety margin
    estimated_tokens = line_count * 10
    return line_count, estimated_tokens

def generate_markdown(structure, max_lines):
    lines = []
    lines.append("# 代码仓库地图 (Repository Map)\n")
    lines.append("> **快照**: 由 Smart Cartographer 生成。仅显示包含关键文件 (Anchors) 的模块。\n")
    lines.append("## 目录结构 (Directory Structure)\n")
    
    for item in structure:
        if len(lines) >= max_lines:
            lines.append(f"\n... (已截断: 超过 {max_lines} 行限制)")
            break
            
        indent = "    " * item['depth']
        
        # Icon selection
        icon = "📂"
        if 'package.json' in item['anchors']: icon = "📦"
        elif 'go.mod' in item['anchors']: icon = "🐹"
        elif 'pom.xml' in item['anchors']: icon = "☕"
        
        name_part = f"{indent}- {icon} `{item['name']}/`"
        
        desc_part = ""
        if item['summary']:
            desc_part = f" - *{item['summary']}*"
        
        lines.append(f"{name_part}{desc_part}")
        
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Maglev Smart Cartographer")
    parser.add_argument('--root', default='.', help='Project root directory')
    parser.add_argument('--estimate', action='store_true', help='Estimate tokens only')
    parser.add_argument('--generate', action='store_true', help='Generate Markdown output')
    parser.add_argument('--max-depth', type=int, default=DEFAULT_MAX_DEPTH, help='Max traversal depth')
    parser.add_argument('--max-lines', type=int, default=DEFAULT_MAX_LINES, help='Max output lines')
    
    args = parser.parse_args()

    # Smart fallback logic
    root_to_scan = args.root
    if root_to_scan == '.' and os.path.exists('code_storages'):
        root_to_scan = 'code_storages'
        print(f"INFO: Auto-selecting '{root_to_scan}' as scan target.")
    
    if not os.path.exists(root_to_scan):
        print(f"Error: Path {root_to_scan} does not exist.")
        if root_to_scan == 'code_storages':
             print("Tip: Are you running in a standard Maglev project? Try creating 'code_storages/' or specify --root.")
        sys.exit(1)

    structure = scan_project(root_to_scan, args.max_depth)
    
    if args.estimate:
        count, tokens = estimate_tokens(structure)
        print(f"REPORT: Found {len(structure)} significant modules/directories.")
        print(f"ESTIMATE: ~{tokens} Tokens (Output size: ~{len(structure)} lines).")
        print("ACTION: Reply 'Yes' or 'Go' to generate file.")
        
    if args.generate:
        content = generate_markdown(structure, args.max_lines)
        print(content)

if __name__ == '__main__':
    main()
