## [0.1.3]

- Fixed inconsistent syntax highlighting for function names in CALL expressions
   - Function names now correctly use the function scope when appearing on the right-hand side of assignments (e.g., LET x = CALL func()).
- Added call-expressions pattern to ensure function calls are recognized within expressions.
- Updated pattern precedence so function names are matched before generic identifiers.
- Ensured consistent highlighting behavior across standalone calls and embedded expressions.

## [0.1.2]

- Fixed comment parsing issue where subsequent lines were incorrectly highlighted as comments
   - Resolved scope bleed caused by comment pattern not terminating correctly.
- Improved handling of inline comments (# ...) within statements.
- Added support for tagged comments:
   - TODO, FIXME, NOTE, BUG, HACK, XXX
- Minor regex refinements to improve stability across multi-line files.

## [0.1.1]

- Improved placeholder (<...>) highlighting for instructional scaffolding
   - Ensured placeholder content is scoped distinctly from identifiers.
- Refined delimiter handling for parentheses, brackets, and braces.
- Enhanced keyword coverage for control flow:
   - Added consistent highlighting for FROM, TO, STEP, IN, DO
- Adjusted identifier vs constant detection to better align with naming conventions.

## [0.1.0]

- Initial release
- Core syntax highlighting for I2P-style pseudocode:
   - Program structure (START, END)
   - Input/output (GET, PUT)
   - Assignment (LET)
   - Function calls (CALL)
   - Conditionals (IF, ELSEIF, ELSE, ENDIF)
   - Loops (WHILE, FOR, FOREACH, DO)
- Support for:
   - Variables (snake_case)
   - Constants (UPPER_CASE)
   - Functions (entity.name.function)
- Basic support for:
   - Strings (single-line and triple-quoted)
   - Numeric and boolean literals
   - Operators (arithmetic, comparison, logical)
- Comment support using #
- Initial TextMate grammar structure and VS Code integration
- Extension metadata and configuration setup (package.json, language configuration)