import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        # Capture Login
        print("Capturing Registration Page...")
        await page.goto("http://localhost:3000/signup")
        await page.wait_for_timeout(3000)
        await page.screenshot(path="docs/assets/screenshot-login.png", full_page=True)

        # Login to capture dashboard
        print("Logging in...")
        await page.fill("input[name='fullName']", "Adarsh")
        await page.fill("input[name='username']", "adarsh123")
        await page.fill("input[type='date']", "1990-01-01")
        await page.fill("input[name='email']", "test@example.com")
        await page.fill("input[name='password']", "password123")
        await page.click("button:has-text('Initialize Node')")
        
        # Wait for dashboard to load
        print("Capturing Dashboard...")
        await page.wait_for_url("http://localhost:3000/dashboard", timeout=10000)
        await page.wait_for_timeout(5000)  # Wait for charts to render
        await page.screenshot(path="docs/assets/screenshot-dashboard.png", full_page=True)
        
        # Capture Copilot
        print("Capturing Copilot...")
        await page.click("text='Chat'") # Click chat tab
        await page.wait_for_timeout(2000)
        await page.fill("textarea", "Analyze this patient's vitals")
        await page.click("button[type='submit']")
        await page.wait_for_timeout(4000)
        await page.screenshot(path="docs/assets/screenshot-copilot.png", full_page=True)

        await browser.close()

asyncio.run(main())
