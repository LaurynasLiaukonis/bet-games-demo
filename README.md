# Automated Betting Game Script

This Python script uses [Playwright](https://playwright.dev/docs/intro) to automate a betting game on a demo website. It performs the following key actions:

## Features

- Launches a Chromium browser in non-headless mode.
- Navigates to the demo betting website.
- Clicks on the **Mini Game** section.
- Locates and interacts with an iframe containing the game.
- Increases the bet amount by clicking a plus button.
- Waits for the **"Place your bets"** game message.
- Checks if the bet amount is greater than zero.
- If the bet amount is valid, randomly selects and clicks a betting option (**Dealer**, **Tie**, or **Player**).
- Includes error handling with screenshot capture.
- Uses [pytest](https://docs.pytest.org/) for test execution.

---

## Installation

1. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
2. Install Playwright by following the official instructions in the [Playwright documentation](https://playwright.dev/docs/intro).

---

## Usage

To run the script, use the following command:

```bash
pytest test_betgames.py