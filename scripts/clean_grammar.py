"""
clean_grammar.py - Clean academic grammar issues in markdown files.

Usage:
    python clean_grammar.py input.md [output.md]

If output is omitted, overwrites the input file.

Fixes:
  1. Em dashes (—) replaced with context-appropriate punctuation
  2. Contractions expanded to full forms
  3. Reports all changes made
"""

import re
import sys
from pathlib import Path


CONTRACTIONS = {
    "don't":    "do not",
    "doesn't":  "does not",
    "didn't":   "did not",
    "can't":    "cannot",
    "couldn't": "could not",
    "won't":    "will not",
    "wouldn't": "would not",
    "shouldn't":"should not",
    "isn't":    "is not",
    "aren't":   "are not",
    "wasn't":   "was not",
    "weren't":  "were not",
    "hasn't":   "has not",
    "haven't":  "have not",
    "hadn't":   "had not",
    "it's":     "it is",
    "that's":   "that is",
    "there's":  "there is",
    "what's":   "what is",
    "who's":    "who is",
    "let's":    "let us",
    "Don't":    "Do not",
    "Doesn't":  "Does not",
    "Didn't":   "Did not",
    "Can't":    "Cannot",
    "Couldn't": "Could not",
    "Won't":    "Will not",
    "Wouldn't": "Would not",
    "Shouldn't":"Should not",
    "Isn't":    "Is not",
    "Aren't":   "Are not",
    "Wasn't":   "Was not",
    "Weren't":  "Were not",
    "Hasn't":   "Has not",
    "Haven't":  "Have not",
    "Hadn't":   "Had not",
    "It's":     "It is",
    "That's":   "That is",
    "There's":  "There is",
    "What's":   "What is",
    "Who's":    "Who is",
    "Let's":    "Let us",
}


def fix_contractions(text):
    """Replace contractions with full forms. Returns (new_text, list_of_changes)."""
    changes = []
    for contraction, expansion in CONTRACTIONS.items():
        pattern = re.compile(r'\b' + re.escape(contraction) + r'\b')
        matches = pattern.findall(text)
        if matches:
            changes.append(f"  Contraction: '{contraction}' -> '{expansion}' ({len(matches)}x)")
            text = pattern.sub(expansion, text)
    return text, changes


def fix_em_dashes(text):
    """
    Replace em dashes with context-appropriate punctuation.
    This uses heuristics based on surrounding context.
    Returns (new_text, count_replaced).
    """
    count = text.count("\u2014")  # — character

    # Pattern: "word — list item, list item, and list item" -> colon
    # Pattern: "word — word" as parenthetical -> comma
    # Pattern: "phrase — phrase — phrase" as parenthetical pair -> parentheses or commas

    # Strategy: replace paired em dashes with parentheses first,
    # then remaining singles contextually.

    # Pass 1: Paired em dashes -> parentheses
    # Match: "text — parenthetical content — continuation"
    paired = re.compile(r' \u2014 ([^.!?\n\u2014]{5,80}?) \u2014 ')
    while paired.search(text):
        text = paired.sub(r' (\1) ', text, count=1)

    # Pass 2: Em dash before a list (preceded by colon-like context)
    # "noun — item1, item2, item3" -> "noun: item1, item2, item3"
    list_pattern = re.compile(r' \u2014 (\w+[^.!?\n]{0,30},)')
    text = list_pattern.sub(r': \1', text)

    # Pass 3: Em dash joining two independent clauses -> semicolon
    # Heuristic: if the text after the dash starts with a capital letter or pronoun
    clause_pattern = re.compile(r' \u2014 ([A-Z])')
    text = clause_pattern.sub(r'; \1', text)

    # Pass 4: Remaining em dashes -> commas (safest default)
    text = text.replace(' \u2014 ', ', ')
    text = text.replace('\u2014', ', ')

    new_count = text.count("\u2014")
    replaced = count - new_count
    return text, replaced


def clean_file(input_path, output_path=None):
    """Clean a markdown file and report changes."""
    text = Path(input_path).read_text(encoding='utf-8')

    all_changes = []

    # Count initial issues
    em_count = text.count("\u2014")
    contraction_pattern = re.compile(
        r"\b(?:" + "|".join(re.escape(c) for c in CONTRACTIONS.keys()) + r")\b"
    )
    contraction_count = len(contraction_pattern.findall(text))

    print(f"Input:  {input_path}")
    print(f"  Em dashes found:    {em_count}")
    print(f"  Contractions found: {contraction_count}")

    # Fix contractions
    text, contraction_changes = fix_contractions(text)
    all_changes.extend(contraction_changes)

    # Fix em dashes
    text, em_replaced = fix_em_dashes(text)
    if em_replaced:
        all_changes.append(f"  Em dashes replaced: {em_replaced}")

    # Verify
    remaining_em = text.count("\u2014")
    remaining_contr = len(contraction_pattern.findall(text))

    if output_path is None:
        output_path = input_path

    Path(output_path).write_text(text, encoding='utf-8')

    print(f"\nOutput: {output_path}")
    print(f"  Em dashes remaining:    {remaining_em}")
    print(f"  Contractions remaining: {remaining_contr}")

    if all_changes:
        print("\nChanges:")
        for c in all_changes:
            print(c)
    else:
        print("\n  No changes needed.")

    return remaining_em == 0 and remaining_contr == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_grammar.py input.md [output.md]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    success = clean_file(input_file, output_file)
    sys.exit(0 if success else 1)
