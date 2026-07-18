# AI Commit Labeler

> AI-assisted GitHub commit annotation tool with human-in-the-loop verification.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Under%20Development-orange)

---

## Overview

AI Commit Labeler is an open-source tool that helps developers and researchers annotate GitHub commits efficiently.

Instead of manually labeling every commit, the tool provides an AI-generated suggestion, confidence score, and explanation. A human reviewer can then accept or override the suggestion, enabling fast and reliable dataset creation.

This approach combines the speed of Large Language Models with the reliability of human verification.

---

## Features

- AI-assisted commit labeling
- Human-in-the-loop verification
- Confidence score for every prediction
- Explanation for each suggested label
- Resume labeling sessions
- CSV dataset export
- Beautiful command-line interface
- Designed for Machine Learning dataset creation

---

## Planned Labels

| Label | Description |
|--------|-------------|
| LOW_VALUE | Documentation, formatting, dependency updates, trivial changes |
| USEFUL | Bug fixes, features, refactoring, performance improvements |
| UNCERTAIN | Requires human judgment |

---

## Future Features

- Multiple LLM support
- OpenAI integration
- Anthropic integration
- Ollama support
- Batch annotation
- GitHub API integration
- Hugging Face dataset export
- JSON export
- Interactive dashboard
- Annotation statistics

---

## Project Status

This project is currently under active development.

Version: **0.1.0**

---

## License

MIT License