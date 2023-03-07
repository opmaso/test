from DemoPage import SearchHelper


def test_demo(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    assert browser.current_url == 'https://demoqa.com/'
    
    main_page.click_on_element_icon()
    assert browser.current_url == 'https://demoqa.com/elements'
    
    main_page.click_on_sidebar_icon()
    assert browser.current_url == 'https://demoqa.com/checkbox'
    
    main_page.click_on_toggle_icon()
    number_of_dropdown_items = main_page.sum_dropdown_items()
    assert number_of_dropdown_items == 3
    
    main_page.click_on_toggle_icons()
    number_of_downloads_items = main_page.sum_downloads_items()
    assert number_of_downloads_items == 2
    
    main_page.click_on_checkbox()
    result_text = main_page.text_from_result()
    assert result_text == 'You have selected :\nwordFile'
