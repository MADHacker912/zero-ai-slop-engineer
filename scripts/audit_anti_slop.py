#!/usr/bin/env python3
"""
Zero AI-Slop Codebase Auditor
Scans project files for AI-generated slop, placeholder code, security leaks,
and bad software engineering practices.
"""

import os
import sys
import re
from pathlib import Path

# ANSI colors
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Ignored directories
IGNORED_DIRS = {
    "node_modules", ".git", ".next", "dist", "build", "coverage",
    ".cache", "__pycache__", ".venv", "venv", ".idea", ".vscode"
}

# Slop detection rules
RULES = [
    {
        "id": "SLOP-001",
        "category": "Design Slop",
        "severity": "HIGH",
        "description": "Generic AI purple/blue gradient backgrounds detected",
        "pattern": re.compile(r"(#667eea|#764ba2|from-purple-500.*to-indigo-500|linear-gradient\(135deg,\s*#667eea)", re.IGNORECASE),
        "exts": [".css", ".scss", ".jsx", ".tsx", ".html", ".vue"]
    },
    {
        "id": "SLOP-002",
        "category": "Fake Implementation",
        "severity": "CRITICAL",
        "description": "Placeholder click handler or empty mock function",
        "pattern": re.compile(r"onClick=\{\(\)\s*=>\s*\{\s*\}\}|onClick=\{\(\)\s*=>\s*alert\(|onClick=\{\(\)\s*=>\s*console\.log\(", re.IGNORECASE),
        "exts": [".jsx", ".tsx", ".vue", ".js", ".ts"]
    },
    {
        "id": "SLOP-003",
        "category": "Code Hygiene",
        "severity": "MEDIUM",
        "description": "Unresolved TODO or FIXME placeholder comments",
        "pattern": re.compile(r"//\s*(TODO|FIXME|PLACEHOLDER|LATER):", re.IGNORECASE),
        "exts": [".js", ".ts", ".jsx", ".tsx", ".py", ".go", ".rs", ".java", ".kt"]
    },
    {
        "id": "SLOP-004",
        "category": "Security Boundary",
        "severity": "CRITICAL",
        "description": "Potential secret or service role key referenced in client code",
        "pattern": re.compile(r"(SUPABASE_SERVICE_ROLE_KEY|DATABASE_URL|ADMIN_SECRET|PRIVATE_KEY)\b"),
        "exts": [".jsx", ".tsx", ".vue", ".svelte", ".html"]
    },
    {
        "id": "SLOP-005",
        "category": "Error Handling",
        "severity": "HIGH",
        "description": "Silently swallowed error / empty catch block",
        "pattern": re.compile(r"catch\s*\([^)]*\)\s*\{\s*\}|except\s+Exception:\s*pass\b"),
        "exts": [".js", ".ts", ".jsx", ".tsx", ".py"]
    },
    {
        "id": "SLOP-006",
        "category": "Design Slop",
        "severity": "MEDIUM",
        "description": "Unrestrained floating blur background blob (slop glow)",
        "pattern": re.compile(r"(filter:\s*blur\([4-9]\d+px\)|backdrop-filter:\s*blur|rounded-full\s+blur-3xl)", re.IGNORECASE),
        "exts": [".css", ".scss", ".jsx", ".tsx", ".html"]
    },
    {
        "id": "SLOP-007",
        "category": "TypeScript Discipline",
        "severity": "MEDIUM",
        "description": "Lazy TypeScript 'any' type escape hatch",
        "pattern": re.compile(r":\s*any\b|<any>|as\s+any\b"),
        "exts": [".ts", ".tsx"]
    }
]

def scan_file(file_path):
    findings = []
    ext = file_path.suffix.lower()
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line_no, line in enumerate(f, 1):
                for rule in RULES:
                    if ext in rule["exts"]:
                        if rule["pattern"].search(line):
                            findings.append({
                                "rule": rule,
                                "file": file_path,
                                "line_no": line_no,
                                "line_content": line.strip()[:100]
                            })
    except Exception as e:
        pass
    return findings

def audit_directory(target_dir):
    print(f"\n{BOLD}{CYAN}═══════════════════════════════════════════════════════════════{RESET}")
    print(f"{BOLD}{CYAN}   🛡️  ZERO AI-SLOP CODEBASE AUDITOR & QUALITY SCANNER{RESET}")
    print(f"{BOLD}{CYAN}═══════════════════════════════════════════════════════════════{RESET}")
    print(f"Scanning target: {BOLD}{target_dir}{RESET}\n")

    target_path = Path(target_dir).resolve()
    if not target_path.exists():
        print(f"{RED}Error: Directory {target_path} does not exist.{RESET}")
        sys.exit(1)

    total_files = 0
    all_findings = []

    for root, dirs, files in os.walk(target_path):
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS and not d.startswith(".")]
        for file in files:
            file_path = Path(root) / file
            total_files += 1
            file_findings = scan_file(file_path)
            all_findings.extend(file_findings)

    print(f"Scanned {BOLD}{total_files}{RESET} files.")

    if not all_findings:
        print(f"\n{GREEN}{BOLD}✅ 100% CLEAN! Zero AI-slop patterns or placeholder defects found.{RESET}\n")
        return 0

    print(f"\n{YELLOW}{BOLD}⚠️  Found {len(all_findings)} potential AI-slop or code quality issues:{RESET}\n")
    
    crit_count = 0
    high_count = 0
    med_count = 0

    for item in all_findings:
        rule = item["rule"]
        sev = rule["severity"]
        if sev == "CRITICAL":
            sev_colored = f"{RED}{BOLD}[CRITICAL]{RESET}"
            crit_count += 1
        elif sev == "HIGH":
            sev_colored = f"{YELLOW}{BOLD}[HIGH]{RESET}"
            high_count += 1
        else:
            sev_colored = f"{CYAN}[MEDIUM]{RESET}"
            med_count += 1

        rel_path = item["file"].relative_to(target_path)
        print(f"  {sev_colored} {BOLD}{rule['id']}{RESET} ({rule['category']})")
        print(f"     Path: {rel_path}:{item['line_no']}")
        print(f"     Issue: {rule['description']}")
        print(f"     Code:  {item['line_content']}\n")

    print(f"{BOLD}Summary:{RESET} {RED}{crit_count} Critical{RESET} | {YELLOW}{high_count} High{RESET} | {CYAN}{med_count} Medium{RESET}")
    if crit_count > 0:
        print(f"\n{RED}{BOLD}❌ Quality Gate FAILED. Address critical issues before merging.{RESET}\n")
        return 1
    return 0

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    sys.exit(audit_directory(path))
