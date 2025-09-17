# Copilot Instructions for TIL Repository

This repository is a multi-language "Today I Learned" (TIL) collection. Each language or topic is organized in its own subdirectory. The structure is intentionally simple to maximize flexibility and ease of contribution.

## Project Structure
- `python study/`: Python scripts and experiments. Example: `turtle.py`, `exam.py`.
- `java study/`: Java source files, organized by topic or week. Example: `src/연습문제/exam4a.java`.
- `flutter study/`: Flutter/Dart experiments. Example: `test.dart`.

## Key Conventions
- **No unified build system**: Each language folder is self-contained. There is no global build or test command.
- **Naming**: Folder and file names may use spaces and non-ASCII (e.g., Korean) characters. Handle paths carefully in scripts.
- **No enforced code style**: Each file may follow its own conventions. Do not auto-format across the whole repo.
- **No cross-language dependencies**: Assume each folder is independent unless a README in that folder says otherwise.

## Developer Workflows
- **Python**: Run scripts directly (e.g., `python3 exam.py`). No requirements.txt or virtualenv by default.
- **Java**: Compile with `javac` from the `src` directory. Example: `javac src/연습문제/exam4a.java`.
- **Flutter/Dart**: Run Dart files with `dart run` or use Flutter tools as needed.

## Patterns & Examples
- When adding new topics, create a new folder at the root level.
- When adding new files, use descriptive names and keep them in the appropriate language/topic folder.
- Do not assume the presence of tests or CI/CD unless a future update adds them.

## Integration Points
- No external services or APIs are integrated by default.
- If you add dependencies, document them in a README within the relevant folder.

## Special Notes
- This repo is for personal learning and experimentation. Prioritize clarity and simplicity over optimization or abstraction.
- If you automate anything (scripts, build tools), document usage in the relevant folder's README.

---

For questions or unclear conventions, check the top-level README or the folder-specific README (if present).