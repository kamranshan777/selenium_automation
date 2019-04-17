__author__ = 'kamran'

class OpenForm():

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"

    def visit(self):
        self.driver.get(self.url)