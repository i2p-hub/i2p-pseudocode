# i2p-pseudocode
A syntax highlighter for I2P-style pseudocode in VS Code


## Installation

Run the following commands to install the current version of the extension

### Windows
```PowerShell
Invoke-WebRequest -Uri "https://github.com/i2p-hub/i2p-pseudocode/raw/refs/heads/main/releases/i2p-pseudocode.vsix" -OutFile "i2p-pseudocode.vsix"
code --install-extension i2p-pseudocode.vsix
```

### Mac or Linux
```bash
curl -L -o i2p-pseudocode.vsix https://github.com/i2p-hub/i2p-pseudocode/raw/refs/heads/main/releases/i2p-pseudocode.vsix
code --install-extension i2p-pseudocode.vsix
```

## Acknowledgements

- [Martin Ring's TextMate grammar definitions ](https://raw.githubusercontent.com/martinring/tmlanguage/refs/heads/master/tmlanguage.json)
- [hanzhi713's ibcs-pseudocode](https://github.com/hanzhi713/ibcs-pseudocode) for the idea.
- [ChatGPT](https://chatgpt.com/share/69c150c8-e594-800d-9002-750ba1792995) for help tweaking regular expressions.
