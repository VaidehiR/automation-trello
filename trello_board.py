import unittest
from trello_setting import browser
from trello_setting import TrelloSetUp
import pdb
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from trello_setting import log
from selenium.webdriver.common.keys import Keys

class Board(TrelloSetUp):

    def activity_bar(self) :

        menu = browser.find_element_by_css_selector('#content > div > div.board-main-content > div.board-header.u-clearfix.js-board-header > div.board-header-btns.mod-right > a.board-header-btn.mod-show-menu.js-show-sidebar > span.board-header-btn-text.u-text-underline')
        
        if menu.is_displayed() :
            menu.click()
        else :
            print('Menu is already shown') 

    # @unittest.skip('board_creation')
    def test_01_board_creation(self):

        
        create_new = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.header-btn-icon.icon-lg.icon-add.light')))

        create_new.click()
        log.info('creating new board')
        sleep(5)
        create_board = browser.find_element_by_css_selector('.js-new-board')
        create_board.click()

        board_title = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/form/div/div/div[1]/input')
        board_title.send_keys('Auto Test Board')

        # make board Public
        browser.find_element_by_css_selector(
            '.subtle-chooser-trigger.unstyled-button.vis-chooser-trigger').click()
        browser.find_element_by_xpath(
            '/html/body/div[5]/div/div[2]/div/ul/li[2]/a').click()

        # create board
        create_board_button = browser.find_element_by_css_selector('.primary')
        create_board_button.click()
        
        log.info('Board created')

    # @unittest.skip('board_list')
    def test_02_board_list(self):

        sleep(10) 
        try :
            trello_back = browser.find_element_by_xpath('//*[@id="header"]/div[1]/a/span')
        except NoSuchElementException :
            return false
        print('Back button is {}'.format(trello_back))
        log.info('Back button is {}'.format(trello_back))        
       
        ActionChains(browser).move_to_element(trello_back).click().perform()
        trello_back.click()
        # print list of already present boards and check if newly created board is present in the list
        sleep(10)
        log.info('list of boards -')
        n = 0
        msg = False
        board_title = browser.find_elements_by_css_selector(
            '#content > div > div.js-boards-page > div > div > div:nth-child(1) > ul > li:nth-child(n) > a > span.board-tile-details.is-badged > span')
        for element in board_title:
            print(element.text)
            log.info(element.text)
            if 'Auto Test Board' == element.text:
                msg = element.text
            else:
                n = n + 1

        if msg:
            print(msg)
            print('Verified - Board created')

    def select_board(self) :

        # select any board        
        select_board = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH , '/html/body/div[3]/div[2]/div/div[2]/div/div/div[1]/ul/li[2]')))
        select_board.click()

      
    # @unittest.skip('list_creation')  
    def test_03_list_creation(self ):

        self.select_board()
        # add list
        add_list = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#board > div.js-add-list.list-wrapper.mod-add.is-idle > form > span')))
        add_list.click()
        # add list title
        add_title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#board > div.js-add-list.list-wrapper.mod-add > form > input')))
        add_title.send_keys('list 1')
        # save list title
        browser.find_element_by_css_selector(
            '#board > div.js-add-list.list-wrapper.mod-add > form > div > input').click()
        log.info('list created')
         # add list title
        browser.find_element_by_css_selector(
            '#board > div.js-add-list.list-wrapper.mod-add > form > input').send_keys('list 3')
        # save list title
        browser.find_element_by_css_selector(
            '#board > div.js-add-list.list-wrapper.mod-add > form > div > input').click()
        log.info('list created')


    # @unittest.skip('card_creation')
    def test_04_card_creation(self):

        # add card in 1st child--1st list
        sleep(5)
        add_card=browser.find_element_by_css_selector(
            '#board > div:nth-child(1) > div > a')
        add_card.click()
        card_title=browser.find_element_by_css_selector(
            '#board > div.js-list.list-wrapper > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.list-card.js-composer > div > textarea')
        
        card_title.send_keys('card 1A')
        add_button=browser.find_element_by_css_selector(
            '#board > div:nth-child(1) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.cc-controls.u-clearfix > div:nth-child(1) > input')
        add_button.click()
        # add another card
        card_title=browser.find_element_by_css_selector(
            '#board > div:nth-child(1) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.list-card.js-composer > div > textarea')
        card_title.send_keys('card 1B')
        add_button=browser.find_element_by_css_selector(
            '#board > div:nth-child(1) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.cc-controls.u-clearfix > div:nth-child(1) > input')
        add_button.click()

        # add card in 2nd child--2nd list
        add_card=browser.find_element_by_css_selector(
            '#board > div:nth-child(2) > div > a')
        add_card.click()
        card_title=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR ,'#board > div:nth-child(2) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.list-card.js-composer > div > textarea')))
        card_title.send_keys('card 2A')
        add_button=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR ,'#board > div:nth-child(2) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.cc-controls.u-clearfix > div:nth-child(1) > input')))
        add_button.click()
        # add another card
        card_title=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR ,'#board > div:nth-child(2) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.list-card.js-composer > div > textarea')))
        card_title.send_keys('card 2B')
        add_button=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR ,'#board > div:nth-child(2) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.cc-controls.u-clearfix > div:nth-child(1) > input')))
        add_button.click()
        log.info('4 cards created')

    # @unittest.skip('drag_drop_cards')
    def test_05_drag_drop_cards(self):

        element=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#board > div:nth-child(1) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > a:nth-child(2) > div.list-card-details")))
            
        target=browser.find_element_by_css_selector(
            "#board > div:nth-child(2) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > a:nth-child(2) > div.list-card-details")

        action_chains=ActionChains(browser)
        action_chains.drag_and_drop(element, target).perform()
        
        # check cards inside new list
        cards_in_list = browser.find_elements_by_xpath('//*[@id="board"]/div[2]/div/div[2]')
        log.info('updated card list :')
        n = 0
        for cards in cards_in_list :
            print(cards.text)
            log.info(cards.text)
            if 'card 2C' == cards.text:
                print('card is dropped in second list')
                log.info('card is dropped in second list')
            else:
                n = n + 1

        browser.find_element_by_css_selector('#board > div:nth-child(2) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > div > div.cc-controls.u-clearfix > div:nth-child(1) > a').click()

    # @unittest.skip('check_activity_after_card_dropped')   
    def test_06_check_activity_after_card_dropped(self) :
        self.activity_bar()

        activity = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > div.js-menu-action-list > div:nth-child(1) > div.phenom-desc')
        print('Recent activity {}'.format(activity.text))
        log.info('Recent activity {}'.format(activity.text))

    # @unittest.skip('change_list_title')
    def test_07_change_list_title(self) :
        
        list_title = browser.find_element_by_css_selector('#board > div:nth-child(2) > div > div.list-header.js-list-header.u-clearfix.is-menu-shown.is-subscribe-shown > div.list-header-target.js-editing-target')
        list_title.click()

        change_title = browser.find_element_by_css_selector('#board > div:nth-child(2) > div > div.list-header.js-list-header.u-clearfix.is-menu-shown.is-subscribe-shown > textarea')
        change_title.send_keys('list 2')
        change_title.send_keys(Keys.ENTER)

        
        updated_title = list_title.text
        print('title is {}'.format(list_title.text))
        sleep(5)
        # self.assertEqual(' list 2' , updated_title)
        
    # @unittest.skip('update_card_title')
    def test_08_update_card_title(self) :
        # temporary code starts
        # temporary code for the hovering issue 
        sleep(10) 
        try :
            trello_back = browser.find_element_by_xpath('//*[@id="header"]/div[1]/a/span')
        except NoSuchElementException :
            return false
        print('Back button is {}'.format(trello_back))
        log.info('Back button is {}'.format(trello_back))        
       
        ActionChains(browser).move_to_element(trello_back).click().perform()
        trello_back.click()
        
        self.select_board()
        # temporary code ends

        log.info('change title of the card')
        element_to_hover_over = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH , '//*[@id="board"]/div[2]/div/div[2]/a[3]')))                                                                                                           
        print('elment is {}'.format(element_to_hover_over))
        hover = ActionChains(browser).move_to_element(element_to_hover_over)
        
        print('hover on element')
        log.info('hover on element')        
        hover.perform()
          
        focuse_elem = browser.switch_to.active_element
        print('focus elem is {}'.format(focuse_elem.text))
        print('hover perform')
        log.info('hover perform')  
        
        edit = browser.find_element_by_xpath('//*[@id="board"]/div[2]/div/div[2]/a[3]/span')        
        edit.click()  

        textfield = browser.find_element_by_css_selector('body > div.quick-card-editor > div > div.list-card.list-card-quick-edit.js-stop > div.list-card-details > textarea')
        textfield.clear()
        textfield.send_keys('card 2C')

        save_button = browser.find_element_by_css_selector('body > div.quick-card-editor > div > input')
        save_button.click()

        # check title is updated
        updated_title = browser.find_element_by_css_selector('#board > div:nth-child(2) > div > div.list-cards.u-fancy-scrollbar.u-clearfix.js-list-cards.js-sortable.ui-sortable > a:nth-child(3) > div.list-card-details > span')
        title = updated_title.text
        print('check title is updated')        
        self.assertEqual('card 2C' , title)
        log.info('title is updated')

    # @unittest.skip('archive_list')
    def test_09_archive_list(self) :

        log.info('archive list')
        list_menu = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#board > div:nth-child(1) > div > div.list-header.js-list-header.u-clearfix.is-menu-shown > div.list-header-extras > a > span')))
        list_menu.click()

        archive = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'body > div.pop-over.is-shown > div > div:nth-child(2) > div > div > div > ul:nth-child(5) > li > a')))
        archive.click()
        # check show menu is open
        # go to menu 
        menu = browser.find_element_by_css_selector('#content > div > div.board-main-content > div.board-header.u-clearfix.js-board-header > div.board-header-btns.mod-right > a.board-header-btn.mod-show-menu.js-show-sidebar > span.board-header-btn-text.u-text-underline')
        if menu.is_displayed() :
            menu.click()
        else :
            print('Menu is already shown')        
        # goto more
        more = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > ul > li:nth-child(5) > a')
        more.click()

        archived_items = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > ul:nth-child(1) > li:nth-child(4) > a')
        archived_items.click()

        switch_to_list = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.archive-controls-switch.quiet-button.js-switch-section')))
        
        switch_to_list.click()
        sleep(5)
        n = 0
       
        archive_lists = browser.find_elements_by_css_selector(
            '#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > div.archive-content.js-archive-content > div')
         
        for list in archive_lists:
            print(list.text)
            if 'list 1' == list.text:
                print('list 1 archived successfully')
            else:
                n = n + 1 

        log.info('list is present in archive items')

        archive_back = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-header.js-board-menu-title.is-in-frame > div > a.board-menu-header-back-button.icon-lg.icon-back.js-pop-widget-view')   
        archive_back.click()

        back_to_menu = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-header.js-board-menu-title.is-in-frame > div > a.board-menu-header-back-button.icon-lg.icon-back.js-pop-widget-view')
        back_to_menu.click()

    # @unittest.skip('change_board_color')
    def test_10_change_board_color(self) :        

        menu = browser.find_element_by_css_selector('#content > div > div.board-main-content > div.board-header.u-clearfix.js-board-header > div.board-header-btns.mod-right > a.board-header-btn.mod-show-menu.js-show-sidebar > span.board-header-btn-text.u-text-underline')
        if menu.is_displayed() :
            menu.click()
        else :
            print('Menu is already shown')

        log.info('change board background color')
        board_background = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > ul > li.board-menu-navigation-item.mod-background > a')))
        board_background.click()
        
        color_list = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , '.board-backgrounds-section-tile.board-backgrounds-colors-tile.js-bg-colors')))
        color_list.click()

        select_color =WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH , '//*[@id="content"]/div/div[2]/div/div/div[2]/div/div/div[5]/div')))
        select_color.click()
        log.info('board background color changed')

        go_back = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-header.js-board-menu-title.is-in-frame > div > a.board-menu-header-back-button.icon-lg.icon-back.js-pop-widget-view')
        go_back.click()

        back_to_menu = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-header.js-board-menu-title.is-in-frame > div > a.board-menu-header-back-button.icon-lg.icon-back.js-pop-widget-view')
        back_to_menu.click()

    # @unittest.skip('favourite_board')
    def test_11_favourite_board(self) :

        log.info('make board favourite')
        star = browser.find_element_by_css_selector('#content > div > div.board-main-content > div.board-header.u-clearfix.js-board-header > div.board-header-btns.mod-left > a.board-header-btn.js-star-board > span')
        star.click()

        log.info('check favourite boards list')
        board_list = browser.find_element_by_css_selector('#header > div.header-boards-button > a > span.header-btn-icon.icon-lg.icon-board.light')
        board_list.click()
        sleep(5)
        star_board_list = browser.find_elements_by_xpath('//*[@id="boards-drawer"]/div/div[2]/div[1]/div/div[1]/div/div[2]/ul')

        n = 0
        for board in star_board_list :
            print(board.text)
            if 'Auto Test Board' == board.text:
                print('Now Auto Test Board is your favourite board')
            else:
                n = n + 1   

        log.info('board is present in favourite boards list') 


    # @unittest.skip('add_member')
    def test_12_add_member(self) :

        menu = browser.find_element_by_css_selector('#content > div > div.board-main-content > div.board-header.u-clearfix.js-board-header > div.board-header-btns.mod-right > a.board-header-btn.mod-show-menu.js-show-sidebar > span.board-header-btn-text.u-text-underline')
        if menu.is_displayed() :
            menu.click()
        else :
            print('Menu is already shown')

        invite = browser.find_element_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > a.button-link.mod-full.js-simple-add-members.js-open-manage-board-members')
        invite.click()

        search_member = browser.find_element_by_css_selector('body > div.pop-over.is-shown > div > div:nth-child(2) > div > div > div > div.search-with-spinner > input')
        search_member.send_keys("vaidehi30")
        sleep(5)
        
        select_member = browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div/div[7]/ul/div[1]')
        select_member.click()

        n = 0
        member_list = browser.find_elements_by_css_selector('#content > div > div.board-menu.js-fill-board-menu > div > div > div.board-menu-content.u-fancy-scrollbar.js-board-menu-content-wrapper > div > div.js-all-members > div.board-menu-member-section.js-list-members.is-partial-row > div.u-clearfix.js-list.js-list-draggable-board-members')
        for members in member_list:
            print(members.text)
            if 'Vaidehi (vaidehi30)' == members.text:
                print('member added successfully')
            else:
                n = n + 1 

    
  


if __name__ == '__main__':
    unittest.main()
