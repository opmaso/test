from BaseApp import BasePage
from selenium.webdriver.common.by import By


class SeacrhLocators:
    LOCATOR_ELEMENTS_ICON = (By.CLASS_NAME, 'avatar.mx-auto.white')
    LOCATOR_SIDEBAR_ICON = (By.ID, 'item-1')
    LOCATOR_TOGGLE_BUTTON = (By.CLASS_NAME, "rct-icon.rct-icon-expand-close")
    LOCATOR_DROPDOWN_ITEMS_COLLAPSED = (By.CLASS_NAME, "rct-node.rct-node-parent.rct-node-collapsed")
    LOCATOR_DOWNLOADS_ITEMS = (By.CLASS_NAME, 'rct-node.rct-node-leaf')
    LOCATOR_CHECKBOXES = (By.CLASS_NAME, 'rct-icon.rct-icon-uncheck')
    RESULT = (By.ID, 'result')
    

class SearchHelper(BasePage):     

    def click_on_element_icon(self):
        element_icon = self.find_elements(SeacrhLocators.LOCATOR_ELEMENTS_ICON)
        element_icon[0].click()
        return element_icon

    def click_on_sidebar_icon(self):
        sidebar_icon = self.find_element(SeacrhLocators.LOCATOR_SIDEBAR_ICON)
        sidebar_icon.click()
        return sidebar_icon

    def click_on_toggle_icon(self):
        toggle_button = self.find_element(SeacrhLocators.LOCATOR_TOGGLE_BUTTON)
        toggle_button.click()
        return toggle_button

    def sum_dropdown_items(self):
        all_items = len(self.find_elements(SeacrhLocators.LOCATOR_DROPDOWN_ITEMS_COLLAPSED))
        return all_items

    def click_on_toggle_icons(self):
        toggle_button = self.find_elements(SeacrhLocators.LOCATOR_TOGGLE_BUTTON)
        toggle_button[2].click()
        return toggle_button

    def sum_downloads_items(self):
        all_items = len(self.find_elements(SeacrhLocators.LOCATOR_DOWNLOADS_ITEMS))
        return all_items

    def click_on_checkbox(self):
        checkbox_button = self.find_elements(SeacrhLocators.LOCATOR_CHECKBOXES)
        checkbox_button[4].click()
        return checkbox_button

    def text_from_result(self):
        result_text = self.find_element(SeacrhLocators.RESULT).text
        return result_text
