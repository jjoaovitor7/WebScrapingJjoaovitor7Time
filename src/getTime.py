from selenium import webdriver

def getTime():
    browser = webdriver.Firefox()
    browser.get("https://jjoaovitor7.github.io/")
    dataHora = browser.find_element_by_class_name("data-hora").find_element_by_tag_name("p")
    return dataHora.text

if __name__ == "__main__":
    print(getTime())
