from selenium import webdriver

def main():
    browser = webdriver.Firefox()
    browser.get("https://jjoaovitor7.github.io/")
    dataHora = browser.find_element_by_class_name("data-hora")
    print(dataHora.text)

if __name__ == "__main__":
    main()