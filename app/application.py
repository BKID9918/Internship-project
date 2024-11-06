from Pages.base_page import Page
from Pages.Reelly_filter_function import ReellyFilterFunc

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.Reelly_filter_function = ReellyFilterFunc(driver)
