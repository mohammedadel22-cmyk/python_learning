# 01. Python Basics

Exercises and command-line applications covering foundational Python I/O and string formatting concepts.

## Topics Covered
* Comments and code documentation
* Output formatting with `print()`, `sep`, and `end`
* Escape sequences (`\n`, `\t`, `\\`, `\"`, `\'`)
* Multi-line strings and string repetition (`*`)
* Variables and user input handling via `input()`

## Files & Projects

1. **`hello.py`**[cite: 7, 8]
   * Introductory practice script testing comments, escape characters, variables, and basic `input()` prompts[cite: 3].
2. **`id_card_generator.py`**[cite: 8]
   * Interactive CLI tool that collects attendee details and generates a formatted **Tech Conference 2026 Pass** using tab alignment, `sep`, and `end`[cite: 8].
3. **`shipping_system.py`**
   * **International Shipping Waybill & Commercial Invoice Generator** — a multi-section CLI system that builds dynamic tracking codes (`sep="-"` with `end=""`) and dynamic Windows file paths.

## How to Run

From the main repository directory, run any script using:

```bash
python3 01.python_basics/hello.py
python3 01.python_basics/id_card_generator.py
python3 01.python_basics/shipping_system.py