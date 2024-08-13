import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style
import time
import os


from app.func import get_country_by_code


class TrendBot:
    def __init__(self, country_code="tr"):
        self.tamamlanma_suresi = 0
        self.country_code = country_code
        self.setup_selenium()

    def setup_selenium(self):
        logging.info("Selenium WebDriver ayarlanıyor...")
        self.chrome_install = ChromeDriverManager().install()
        self.folder = os.path.dirname(self.chrome_install)
        self.chromedriver_path = os.path.join(self.folder, "chromedriver.exe")
        self.service = Service(self.chromedriver_path)
        # self.service = Service(ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")
        self.options.add_argument("--disable-gpu")
        logging.info("Selenium başarıyla ayarlandı...")

    def retrieve_trending_topics(self):
        try:
            start_time = time.time()
            country = get_country_by_code(self.country_code)
            country_slug = country["slug"]

            with webdriver.Chrome(service=self.service, options=self.options) as driver:
                # Siteyi Ara
                driver.get(f"https://getdaytrends.com/{country_slug}/")
                wait = WebDriverWait(driver, 10)
                # Elementi Bul
                trend_items = wait.until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, ".card-body .table-hover .main a")
                    )
                )

                trends = [
                    item.text.strip() for item in trend_items[:15]
                ]  # 15 Hashtag getir
                if trends:
                    print(f"{Fore.MAGENTA}author: {Style.RESET_ALL} Ban0")
                    end_time = time.time()
                    self.tamamlanma_suresi = end_time - start_time
                    print(
                        f"{Fore.MAGENTA}tamamlanma süresi: {Style.RESET_ALL} {self.tamamlanma_suresi:.2f} saniye"
                    )
                    print(f"{Fore.MAGENTA}hashtags: {Style.RESET_ALL}")
                    for trend in trends:
                        print(f"  {Fore.CYAN}{trend}{Style.RESET_ALL}")
                else:
                    print("Üzgünüm, şu anda trend olan hashtag'leri alamıyorum.")
                return trends
        except Exception as e:
            logging.error("Failed to retrieve trending topics: %s", str(e))
            return []

    def run(self):
        logging.info("İnfaz başlatıldı...")
        trends = self.retrieve_trending_topics()
        logging.info("İnfaz tamamlandı.")
        return trends
