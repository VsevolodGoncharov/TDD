import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Маруся слышала про крутое новое приложение со списком неотложных дел.
        # Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')

        # Она видит, что заголовок и шапка страницы говорят о списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Она набирает в текстовом поле "Прополоть репу"
        inputbox.send_keys('Прополоть репу')

        # Когда она нажимает enter, страница обновляется,
        # и теперь страница содержит "1: Прополоть репу" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Прополоть репу' for row in rows),
            'Новый элемент списка не появился в таблице'
        )

        # Текстовое поле по-прежнему приглашает её добавить ещё один элемент.
        # Она вводит "Помыть кобылу"
        self.fail('Закончить тест!')

        # Страница снова обновляется, и теперь показывает оба элемента

        # Марусе интересно, запомнит ли сайт её список дел.
        # Далее она видит, что сайт сгенерировал для неё уникальный URL-адрес
        # об этом выводится небольшой текст с объяснениями

        # Она посещает этот URL-адрес - её список по-прежнему там

        # Удовлетворенная, она снова едёт месить тесто


if __name__ == '__main__':
    unittest.main(warnings='ignore')
