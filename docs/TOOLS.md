# Essential Development Tools and Scripts

A curated list of recommended tools and scripts for software development, organized by functionality.

## File Management and Processing

### Command Line Tools
- [fd](https://github.com/sharkdp/fd) - A simple, fast, and user-friendly alternative to 'find'
  - Installation: `brew install fd`
  - Usage: `fd pattern` to find files/directories matching pattern
  - Features: Smart case sensitivity, regex support, parallel execution

- [ripgrep](https://github.com/BurnSushi/ripgrep) - Recursively search directories using regex patterns
  - Installation: `brew install ripgrep`
  - Usage: `rg pattern` to search for pattern in files
  - Features: Respects .gitignore, automatic filtering of binary files

- [bat](https://github.com/sharkdp/bat) - A cat clone with syntax highlighting and Git integration
  - Installation: `brew install bat`
  - Usage: `bat file.txt` to view file with syntax highlighting
  - Features: Git integration, automatic paging, syntax highlighting

### File Organization
- [organize-cli](https://github.com/ManrajGrover/organize-cli) - Organize files by their extensions
  - Installation: `npm install -g organize-cli`
  - Usage: `organize` in target directory
  - Features: Customizable rules, dry run option

## Text Processing and Documentation

### Markdown Tools
- [pandoc](https://pandoc.org/) - Universal document converter
  - Installation: `brew install pandoc`
  - Usage: `pandoc input.md -o output.pdf`
  - Features: Converts between multiple formats, customizable templates

- [mdbook](https://github.com/rust-lang/mdBook) - Create online books from markdown files
  - Installation: `cargo install mdbook`
  - Usage: `mdbook build` to generate book
  - Features: Live reload, customizable themes, search functionality

### Code Documentation
- [pdoc](https://pdoc3.github.io/pdoc/) - Auto-generate API documentation for Python modules
  - Installation: `pip install pdoc3`
  - Usage: `pdoc --html mymodule`
  - Features: Markdown support, live preview server

## Development Utilities

### Version Control
- [git-delta](https://github.com/dandavison/delta) - Syntax-highlighting pager for git
  - Installation: `brew install git-delta`
  - Configuration: Add to .gitconfig
  - Features: Side-by-side diffs, syntax highlighting, line numbering

- [lazygit](https://github.com/jesseduffield/lazygit) - Terminal UI for git commands
  - Installation: `brew install lazygit`
  - Usage: Run `lazygit` in repository
  - Features: Interactive rebase, stashing, branch management

### Code Quality
- [pre-commit](https://pre-commit.com/) - Framework for managing git pre-commit hooks
  - Installation: `pip install pre-commit`
  - Usage: Create .pre-commit-config.yaml and run `pre-commit install`
  - Features: Language agnostic, configurable hooks

- [black](https://github.com/psf/black) - Python code formatter
  - Installation: `pip install black`
  - Usage: `black .` to format all Python files
  - Features: Deterministic formatting, configuration via pyproject.toml

## Testing and Debugging

### Testing Tools
- [pytest](https://docs.pytest.org/) - Python testing framework
  - Installation: `pip install pytest`
  - Usage: `pytest` to run tests
  - Features: Fixtures, parameterized testing, plugins

- [k6](https://k6.io/) - Modern load testing tool
  - Installation: `brew install k6`
  - Usage: `k6 run script.js`
  - Features: JavaScript API, metrics visualization

### Debugging
- [httpie](https://httpie.io/) - User-friendly command-line HTTP client
  - Installation: `brew install httpie`
  - Usage: `http GET example.com`
  - Features: JSON support, syntax highlighting, sessions

## Development Environment

### Terminal Enhancements
- [tmux](https://github.com/tmux/tmux) - Terminal multiplexer
  - Installation: `brew install tmux`
  - Usage: `tmux` to start session
  - Features: Session management, split panes, customizable

- [fzf](https://github.com/junegunn/fzf) - Command-line fuzzy finder
  - Installation: `brew install fzf`
  - Usage: `Ctrl+R` for history search
  - Features: Vim integration, completion

### Project Management
- [task](https://taskwarrior.org/) - Command-line task management
  - Installation: `brew install task`
  - Usage: `task add "New task"`
  - Features: Tags, priorities, dependencies

## Automation and Scripting

### Task Runners
- [just](https://github.com/casey/just) - Command runner for project-specific tasks
  - Installation: `brew install just`
  - Usage: Create Justfile and run `just command`
  - Features: Shell-agnostic, dependencies between recipes

### Build Tools
- [poetry](https://python-poetry.org/) - Python dependency management and packaging
  - Installation: `curl -sSL https://install.python-poetry.org | python3 -`
  - Usage: `poetry init` to create new project
  - Features: Lock files, virtual environments, publishing

## Monitoring and Performance

### System Monitoring
- [htop](https://htop.dev/) - Interactive process viewer
  - Installation: `brew install htop`
  - Usage: Run `htop`
  - Features: Process management, resource monitoring

- [glances](https://nicolargo.github.io/glances/) - System monitoring tool
  - Installation: `pip install glances`
  - Usage: Run `glances`
  - Features: Web interface, REST API, exports

### Performance Analysis
- [hyperfine](https://github.com/sharkdp/hyperfine) - Command-line benchmarking tool
  - Installation: `brew install hyperfine`
  - Usage: `hyperfine 'command1' 'command2'`
  - Features: Statistical analysis, warmup runs, export to various formats

## Contributing
Feel free to suggest additional tools by creating a pull request. Please include:
- Tool name and description
- Installation instructions
- Basic usage example
- Key features
- Link to official documentation/repository

## License
This curated list is licensed under the MIT License - see the LICENSE file for details.