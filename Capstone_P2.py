import pytest
from time import sleep
from selenium import webdriver
from Test_Data import OHRM_Data
from Test_Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class Test_OrangeHRM():

    @pytest.fixture
    def Web_Page_Booting(self):
        self.driver = webdriver.Firefox(service=Service (GeckoDriverManager().install()))
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        yield
        self.driver.close()
    
    # Test Case for Menu Search
    def test_TC_PIM_01 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_1).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_1).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_2).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_2).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_3).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')
            
            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_3).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_4).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_4).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_5).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_5).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_6).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_6).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_7).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_7).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_8).upper())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

            Menu_Search = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Menu_Search_Locator)))
            Menu_Search.send_keys((OHRM_Data.OHRM_TEST_Data().Input_8).lower())
            if self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SearchResult_locator).is_displayed():
                print('Menu Fetched')

        except NoSuchElementException:
            print('Element Missing')

    # Test Case PIM User Management
    def test_TC_PIM_02 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            Admin = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Admin_locator)))
            self.action.move_to_element(Admin).click(Admin).perform()

            # User Management 
            User_Management = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().UserManagement_locator)))
            self.action.move_to_element(User_Management).click(User_Management).perform()
            Users = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Users_locator)))
            self.action.move_to_element(Users).click(Users).perform()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().UserRole_dd_locator)))
            Admin_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().UserRole_dd_locator).text
            if Admin_dd.__contains__("Admin"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Admin'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().UserRole_dd_locator)))
            ESS_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().UserRole_dd_locator).text
            if ESS_dd.__contains__("ESS"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='ESS'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().status_locator)))
            Enabled_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().status_locator).text
            if Enabled_dd.__contains__("Enabled"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Enabled'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().status_locator)))
            Disabled_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().status_locator).text
            if Disabled_dd.__contains__("Enabled"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Disabled'", self.value)

        except NoSuchElementException:
            print('Element Missing')

    # Test Case to Check whether the User is able to Add and Create Login for the New Employee
    def test_TC_PIM_03 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()

            # Adding an Employee in PIM
            Add_Tab = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().AddEmp_locator)))
            self.action.move_to_element(Add_Tab).click(Add_Tab).perform()
            Add_Emp = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().Add_fn_locator)))
            Add_Emp.send_keys(OHRM_Data.OHRM_TEST_Data().FirstName)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().Add_mn_locator).send_keys(OHRM_Data.OHRM_TEST_Data().MiddleName)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().Add_ln_locator).send_keys(OHRM_Data.OHRM_TEST_Data().LastName)
            clear_input = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Emp_ID_locator)))
            self.action.move_to_element(clear_input).double_click(clear_input).send_keys(Keys.DELETE).perform()
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Emp_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)

            # Creating Login for the New Employee
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Create_login_locator).click()
            Emp_Login = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Login_id_locator)))
            Emp_Login.send_keys(OHRM_Data.OHRM_TEST_Data().Login_ID)
            C_Login_P = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Login_pass_locator)))
            C_Login_P.send_keys(OHRM_Data.OHRM_TEST_Data().Login_password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Login_confpass_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Login_password)
            sleep(2)
            Submit = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Add_Emp_Submit_locator)))
            Submit.click()
            print('New Employee Data and Login Created Successfully')

        except NoSuchElementException:
            print('Element Missing')     

    # Test Case to Edit Employee Details
    def test_TC_PIM_04 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()

            # Employee List
            EmployeeList = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().EmpolyeeList_locator)))
            self.action.move_to_element(EmployeeList).click(EmployeeList).perform()

            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

        except NoSuchElementException:
            print('Element Missing')

    # Test Case for Personal Details
    def test_TC_PIM_05 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()

            # Employee List
            EmployeeList = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().EmpolyeeList_locator)))
            self.action.move_to_element(EmployeeList).click(EmployeeList).perform()

            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Personal Details
            NickName = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().NickName_locator)))
            NickName.send_keys(OHRM_Data.OHRM_TEST_Data().NickName)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().DLN_locator).send_keys(OHRM_Data.OHRM_TEST_Data().DLN)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().DLNE_locator).send_keys(OHRM_Data.OHRM_TEST_Data().DLNE)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SSN_locator).send_keys(OHRM_Data.OHRM_TEST_Data().SSN)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SIN_locator).send_keys(OHRM_Data.OHRM_TEST_Data().SIN)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Nationality_dd_locator)))
            Indian_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().status_locator).text
            if Indian_dd.__contains__("Indian"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Indian'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().MatrialS_dd_locator)))
            Single_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().MatrialS_dd_locator).text
            if Single_dd.__contains__("Single"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Single'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().DOB_locator).send_keys(OHRM_Data.OHRM_TEST_Data().DOB)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Male_locator).click()
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().PD_Save1_locator).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().BG_dd_locator)))
            A_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().BG_dd_locator).text
            if A_dd.__contains__("A+"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='A+'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().PD_Save2_locator).click()

        except NoSuchElementException:
            print('Element Missing')
    
    # Test Case for Contact Details
    def test_TC_PIM_06 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Contact Details
            ContactDetails = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().ContactD_locator)))
            self.action.move_to_element(ContactDetails).click(ContactDetails).perform()
            Address = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Street_locator)))
            Address.send_keys(OHRM_Data.OHRM_TEST_Data().Street)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().City_locacator).send_keys(OHRM_Data.OHRM_TEST_Data().City)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().State_locator).send_keys(OHRM_Data.OHRM_TEST_Data().State)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Pincode_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Pincode)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Country_dd_locator)))
            India_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Country_dd_locator).text
            if India_dd.__contains__("India"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='India'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Mobile_locator).send_keys(OHRM_Data.OHRM_TEST_Data().MobileNo)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Email_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Email)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().CD_Save_locator).click()            
            
        except NoSuchElementException:
            print('Element Missing')

    # Test Case for Emergency Contact
    def test_TC_PIM_07 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Emergency Contact
            EmergencyContactDetails = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().EmergencyC_locator)))
            self.action.move_to_element(EmergencyContactDetails).click(EmergencyContactDetails).perform()
            EC_Add = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().EC_Add_locator)))
            EC_Add.click()
            EC_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().EC_Name_locator)))
            EC_Name.send_keys(OHRM_Data.OHRM_TEST_Data().EC_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().EC_Relation_locator).send_keys(OHRM_Data.OHRM_TEST_Data().EC_Relation)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().EC_Mobile_locator).send_keys(OHRM_Data.OHRM_TEST_Data().EC_MobileNo)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().EC_Save_locator).click()            
            
        except NoSuchElementException:
            print('Element Missing')

    # Test Case Dependent Details
    def test_TC_PIM_08 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Dependent Details
            Dependents = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Dependents_locator)))
            self.action.move_to_element(Dependents).click(Dependents).perform()
            Dependent_Add = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Dependent_Add_locator)))
            Dependent_Add.click()
            Dependent_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Dependent_Name_locator)))
            Dependent_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Dependent_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Dependent_RDD_locator).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Dependent_RDD_locator)))
            Child_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Dependent_RDD_locator).text
            if Child_dd.__contains__("Child"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Child'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Dependent_DOB_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Dependent_DOB)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Dependent_Save_locator).click()

        except NoSuchElementException:
            print('Element Missing')

    # Test Case Job Details
    def test_TC_PIM_09 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Job Details
            Job = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Job_locator)))
            self.action.move_to_element(Job).click(Job).perform()
            Job_JD = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Joined_Date_locator)))
            Job_JD.send_keys(OHRM_Data.OHRM_TEST_Data().Job_JD)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Job_TitleDD_locator)))
            CEO_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Job_TitleDD_locator).text
            if CEO_dd.__contains__("Chief Executive Officer"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Chief Executive Officer'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().JobC_DD_locator)))
            Testing_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().JobC_DD_locator).text
            if Testing_dd.__contains__("Testing"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Testing'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().SubUnit_DD_locator)))
            QA_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SubUnit_DD_locator).text
            if QA_dd.__contains__("Quality Assurance"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Quality Assurance'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Job_locationDD_locator)))
            JLocation_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Job_locationDD_locator).text
            if JLocation_dd.__contains__("Texas R&D"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Texas R&D'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().JobStatusDD_locator)))
            JStatus_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().JobStatusDD_locator).text
            if JStatus_dd.__contains__("Part time Job"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Part time Job'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().JobToggle_locator).click()
            Contract_SD = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Contract_SD_locator)))
            Contract_SD.send_keys(OHRM_Data.OHRM_TEST_Data().ContractSD)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Contract_ED_locator).send_keys(OHRM_Data.OHRM_TEST_Data().ContractED)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().JobSave_locator).click()

        except NoSuchElementException:
            print('Element Missing')

    # Test Case for Termination
    def test_TC_PIM_10 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Termination
            Job = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Job_locator)))
            self.action.move_to_element(Job).click(Job).perform()
            Terminate = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Terminate_locator)))
            self.action.move_to_element(Terminate).click(Terminate).perform()
            TerminateDate = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().TerminateDate_locator)))
            TerminateDate.send_keys(OHRM_Data.OHRM_TEST_Data().TerminateDate)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().TerminateReasonDD_locator)))
            TR_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().TerminateReasonDD_locator).text
            if TR_dd.__contains__("Retired"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Retired'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().TerminationSave_locator).click()

        except NoSuchElementException:
            print('Element Missing')

    # Test Case for Employee Activation 
    def test_TC_PIM_11 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Activate Emp
            Activate = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().ActivateEmployment_locator)))
            self.action.move_to_element(Activate).click(Activate).perform()

        except NoSuchElementException:
            print('Element Missing')

    # Test Case for Salary Details
    def test_TC_PIM_12 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Salary Details
            Salary = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Salary_locator)))
            self.action.move_to_element(Salary).click(Salary).perform()
            SalaryAdd = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().SalaryAdd_locator)))
            self.action.move_to_element(SalaryAdd).click(SalaryAdd).perform()
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SalaryComponent_locator).send_keys(OHRM_Data.OHRM_TEST_Data().SalaryComponent)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PayFreqDD_locator)))
            PF_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().PayFreqDD_locator).text
            if PF_dd.__contains__("Monthly"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Monthly'", self.value)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().CurrencyDD_locator)))
            inr_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().CurrencyDD_locator).text
            if inr_dd.__contains__("Indian Rupee"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Indian Rupee'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Amount_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Amount)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SalaryToggle_locator).click()
            
            AccountNo = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().AccountNo_locator)))
            AccountNo.send_keys(OHRM_Data.OHRM_TEST_Data().AccountNo)
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().AccountTypeDD_locator)))
            SVA_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().AccountTypeDD_locator).text
            if SVA_dd.__contains__("Savings"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Savings'", self.value)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().RoutingNo_locator).send_keys(OHRM_Data.OHRM_TEST_Data().RoutingNo)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Amount2_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Amount)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().SalarySave_locator).click()

        except NoSuchElementException:
            print('Element Missing')

    # Test Case for Tax Details
    def test_TC_PIM_13 (self, Web_Page_Booting):
        try:
            self.driver.get(OHRM_Data.OHRM_TEST_Data().url)
            OHRM_USERNAME = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.html_locators().username_locator)))
            OHRM_USERNAME.send_keys(OHRM_Data.OHRM_TEST_Data().username)
            self.driver.find_element(by=By.NAME, value= Locators.html_locators().password_locator).send_keys(OHRM_Data.OHRM_TEST_Data().password)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().signin_locator).click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()
 
            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Searchby_Name_locator)))
            Search_Name.send_keys(OHRM_Data.OHRM_TEST_Data().Delete_Search_Name)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Searchby_ID_locator).send_keys(OHRM_Data.OHRM_TEST_Data().Emp_ID)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().Search_locator).click()
            sleep(2)
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Edit_locator)))
            Edit_data.click()

            # Tax Details
            Tax = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().Tax_locator)))
            self.action.move_to_element(Tax).click(Tax).perform()
            TaxStatus = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().TaxStatusDD_locator)))
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.html_locators().TaxStatusDD_locator)))
            TS_dd = self.driver.find_element(by=By.XPATH, value= Locators.html_locators().TaxStatusDD_locator).text
            if TS_dd.__contains__("Single"):
                self.driver.execute_script("var a=argument[0];a.innerHTML='Single'", self.value)
            
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().TaxExemptions_locator).send_keys(OHRM_Data.OHRM_TEST_Data().TaxException)
            self.driver.find_element(by=By.XPATH, value= Locators.html_locators().TaxSave_locator).click()

        except NoSuchElementException:
            print('Element Missing')

    