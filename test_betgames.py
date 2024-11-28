from playwright.sync_api import sync_playwright, expect
import pytest
import random
import time

def test_minigame_bet():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False
        )
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto("https://demo.betgames.tv", timeout=5000)
            page.wait_for_load_state("networkidle", timeout=5000)
            
            page.locator('[title="Mini Game"]').click()
            page.wait_for_load_state("networkidle", timeout=5000)
        
            iframe = page.frame_locator('iframe[src*="demo-widget.betgames.tv"]')
            
            plus_button = iframe.locator('[data-qa="button-bet-amount-increase"]')
            plus_button.wait_for(state="visible", timeout=5000)
            plus_button.click()

            betting_options = [
                "betting-option-dealer", 
                "betting-option-tie", 
                "betting-option-player"
            ]

            game_message_locator = iframe.locator('[data-qa="area-game-message"]')
            expect(game_message_locator).to_have_text("Place your bets", timeout=120000)

            bet_amount_input = iframe.locator('[data-qa="input-bet-amount"]')
            bet_amount = float(bet_amount_input.get_attribute("value"))

            if bet_amount > 0:
                selected_option = random.choice(betting_options)
        
                betting_option = iframe.locator(f'[data-qa="{selected_option}"]')
                betting_option.click()
                print(f"Clicked betting option: {selected_option}")
            else:
                print("Bet amount is 0, cannot proceed with betting")

            page.wait_for_timeout(2000)

        except Exception as e:
            page.screenshot(path=f"minigame-error-screenshot-{time.time()}.png")
            print(f"Minigame test failed with error: {str(e)}")
            raise e
        finally:
            context.close()
            browser.close()

if __name__ == '__main__':
    pytest.main(['-v', __file__])