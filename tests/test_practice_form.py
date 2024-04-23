from selene import browser, have, be
import os

def test_demoqa():
    browser.open("/automation-practice-form")
    browser.element("#firstName").type("kek")
    browser.element("#lastName").type("Kekinskii")
    browser.element("#userEmail").type("kekovich@mail.ru")
    browser.element("//*[text()='Male']/parent::*").click()
    browser.element("#userNumber").type(8985123456)
    browser.element("#dateOfBirthInput").click()
    browser.all(".react-datepicker__year-select>option").element_by(have.text("1990")).click()
    browser.all(".react-datepicker__month-select").element_by(have.text("March")).click()
#   browser.all(".react-datepicker__month-select").all('option')[4].click
#   browser.all(".react-datepicker__month-select").send_keys('May')
    browser.all(".react-datepicker__day").element_by(have.text("10")).click()
    browser.element("#subjectsInput").click().send_keys("math")
    browser.element("#react-select-2-option-0").click()
    browser.element("//*[text()='Sports']/parent::*").click()
    browser.execute_script("window.scrollTo(0,500)")
    browser.element("#uploadPicture").send_keys(os.path.abspath("../picture/pepe.jpeg"))
    browser.element("#currentAddress").type("omsk")
#    browser.element("#currentAddress").perform(command.js.set_value('omskaya street')) test
    browser.element("#state").click()
    browser.element("#react-select-3-option-0").should(be.visible).click()
    browser.element("#city").click()
    browser.element("#react-select-4-option-0").click()
    browser.element("#submit").press_enter()
    browser.element(".modal-header").should(have.text("Thanks for submitting the form"))
    browser.element(".modal-body").should(have.exact_text(
        'Label Values\n' 
        'Student Name kek Kekinskii\n' 
        'Student Email kekovich@mail.ru\n' 
        'Gender Male\n' 
        'Mobile 8985123456\n' 
        'Date of Birth 10 November,1990\n' 
        'Subjects Maths\n' 
        'Hobbies Sports\n'  
        'Picture pepe.jpeg\n' 
        'Address omsk\n' 
        'State and City NCR Delhi'
    ))
    browser.element("#closeLargeModal").press_enter()

"""
Метод для закрытия таба - просили не добавлять функции
def close_tab():
    browser.element("[data-testid=ClearIcon]").click()
"""
def test_complete_todo():
    browser.open("https://app.qa.guru/automation-practice-form/")
    '''
    не реализована проверка текста всплывающего окна
    #browser.config.base_url = "https://app.qa.guru/automation-practice-form/"
    #browser.element(".MuiTypography-root .MuiTypography-body1").should(have.text("Записывайтесь на"))
    
    Убрана проверка всплывающего окна + работа через функцию
    if browser.element("[data-testid=ClearIcon]").should(be.visible):
        close_tab()
    '''
    browser.element("[data-testid=ClearIcon]").should(be.visible).click()
    browser.element('[type="text"][data-testid="firstName"]').type("name")
    browser.element('[type="text"][data-testid="lastName"]').type("surname")
    browser.element('[type="text"][data-testid="email"]').type("mailliam@mail.ru")
    browser.element('[name = "phone"]').type("9992424455")
    browser.element("//*[text()='Language']/parent::*").click()
    browser.all('[role="option"]').element_by(have.exact_text("Russian")).click()
    #browser.execute_script("window.scrollTo(0,200)") //Может пригодится для других размеров окон
    browser.element("[data-testid ='dateOfBirth']").click().type("12111999")
    browser.element("[value='Male']").click()
    '''
    browser.all("[name=gender]").have_value(have.exact_text("Female").click()
    '''
    browser.all('[type="checkbox"]').second.click()
    #browser.execute_script("window.scrollTo(0,200)")  /Может пригодится для других размеров окон
    browser.element("//*[text()='Subjects']/parent::*").click()
    browser.all("[role='option']")[5].click().press_escape()
    browser.element("//*[text()='State']/parent::*").click()
    browser.all("[role='option']")[5].click()
    browser.element("//*[text()='City']/parent::*").click()
    browser.all("[role='option']")[1].click()
    browser.element(".MuiSlider-root input").set_value(value="12")
    browser.element('[data-testid="address"]').type("zoo").press_tab()
    browser.execute_script("window.scrollTo(0,500)")
    browser.element('//*[text()="Submit"]').click()
    browser.element('//*[text()="Thank you for submitting the form"]').should(be.visible)
    browser.all('//*[text()="Thank you for submitting the form"]/parent::*/child::*').should(have.texts(
        "Thank you for submitting the form", "firstName\nname", "lastName\nsurname",
        "email\nmailliam@mail.ru", "gender\nMale", "phone\n+1 999 242 4455", "dateOfBirth\n12/11/1999",
        "subjects\nScience", "hobbies\nReading", "stateCity\nCalifornia, Los Angeles", "slider\n50",
        "language\nRussian", "address\nzoo"))

    '''
    вариант работы с датой через прокликивание (не завершен)
    
    browser.element('[data-testid="CalendarIcon"]').click()
    browser.element(".MuiDateCalendar-root [data-testid='ArrowDropDownIcon']").click()
    #browser.all(".MuiDateCalendar-root").element("[type='button'].MuiPickersYear-yearButton").element(have.value("1990")).click()
    #browser.all("[role='gridcell']").element_by(have.attribute("name", "1" )).click()
    '''