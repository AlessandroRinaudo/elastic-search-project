from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_cv_all_profile():
    response = client.get("/search_cv")
    assert response.status_code == 200
    # >= 10 because user could have add new CVs
    assert len(response.json()) >= 10


def test_cv_not_found():
    response = client.get("/search_cv?q=javax", json={"q": "javax"})
    assert response.status_code == 200
    assert response.json() == []
    print(response.json())


def test_cv_corejava_profile():
    response = client.get("/search_cv?q=CoreJava")
    assert response.status_code == 200
    assert response.json()[0]["_source"]["info"] == '    SWAPNA SUSAN JOSE \nJUNIOR SOFTWARE TEST ENGINEER \n \nPhone:+91-7034215669                                                            Email: swapnasusan06@gmail.com \n \n \nPROFILE SUMMARY \n \n\uf0b7  10 months of experience in Testing field as a junior test engineer. \n\uf0b7  Expertise  in  Manual  Testing,  Preparing  Test  cases,  Test  data’s,  Test  execution  and \n\nTracking Defects. \n\n\uf0b7  Have  Good  Knowledge  in  Functional,  Negative,  Regression,  System  Integration  (SIT), \n\nand User Acceptance (UAT) testing methods. \n\n\uf0b7  Testing all the possible situations of the application. \n\uf0b7  Worked in Test Planning, Designing Test Cases, Reporting and Tracking Defects. \n\uf0b7  Have  experience  in  working  with  different  software  development  Models  like Waterfall \n\n\uf0b7  Strong in Presentation, Communication and Team Skills. \n\uf0b7  Coping with change in the workplace, providing effective customer service  \n\uf0b7  Co-ordinate  with  Developers,  Testers,  individuals  involved  in  the  project  to  resolve  the \n\n\uf0b7  Quick learner and excellent  team  player, ability  to meet  tight  deadlines  and work under \n\nand Spiral. \n\nidentified issues. \n\npressure. \n\n \nCareer Path \n \n\uf0b7 Worked on Hiworth Solutions as Junior Test Engineer from June 2015 to March 2016 \n \nTechnical Competencies \n \nSoftware Process/Models    : SDLC, STLC, Waterfall, Agile, Manual Testing \nOperating Systems              :   Windows10/8/9, XP \nProgramming Languages     :  C,C++,CoreJava Fundamentals, PHP \nBug Reporting Tool:Jira \nTesting Type    \nDatabase                 \nIDE              :Dreamweaver, Eclipse \nAutomation Tools  \n \nTraining and Certifications \n\uf0b7  Pursuing a certified course on Automation Testing  Tools – Selenium and QTP. \n \n\n:  Manual,Automation \n: My SQL \n\n:   Selenium, QTP \n\n\x0cProjects Summary \n\n \n\n\uf0d8  Silhouettes Boutique  \n\nProject Type   : E-Commerce Application \n\nDeveloped by:Hiworth Solutions \nRole: Software Tester \nDescription \nSilhouettes Boutique is an online shopping boutique which provides a unique platform to \nbring its customers contemporary on-trend pieces as well as timeless classics in a Quick and \nEasy way. Developed in such a way that the customers or anyone using the site can easily \naccess and understand the features and functionalities. \nResponsibilities \n•Done the manual testing of the website after development. \n•   Test Case Preparation based on the Requirement Criteria. \n•   Functionality Testing, Regression testing, Re-testing. (Manual) \n•   Backend Testing and products validation and verification. \n•   Raising and tracking Bugs. \n•   Preparation of test plans and quality reports. \n \n\uf0d8  Northeast Arkansas Federal Credit Union  \n   Project Type   : Banking Software \n      Developed by : Hiworth Solutions \nRole: Software Tester \nDescription \nNEAFCU  is a web-based reliable and flexible credit union in Arkansas which is operated by  \na volunteer board of directors and offers a full-line of services to members including flexible  \nloans, great deposits, personal member services and debit membership applications and it  \nfeatured as a great financial option to consider for both loans and savings products. \n\nResponsibilities  \n•Done the manual testing of the website  after development. \n•   Test Planning, Test case development and Test script execution skills estimation.. \n•Functionality Testing, Regression testing, Re-testing. (Manual) \n •   Bug Tracking and Reporting.  \n•Re-testing of resolved defects \n \n\uf0d8 Arkansas School Board Association  \nProject Type   : Educational Related Software \n     Developed by : Hiworth Solutions \nRole: Software Tester \n \n \nDescription \n\n\x0cThe ARSBA is a private, non-profit, membership organization that provides leadership, \ntraining, advocacy & specialized services to school boards throughout Arkansas. Its \nspecialized services include board development, legal consultations, Workers compensation \ninsurance, model policy services and promote student focused leadership in Public. \nResponsibilities  \n•Done the manual testing of the website after development. \n•    Test Case Preparation based on the Requirement Criteria. \n•    Functionality Testing, Regression testing, Re-testing. (Manual) \n•    Raising and tracking Bugs. \n•    Preparation of test plans and quality reports.  \n \n\n\uf0d8  Automatic Medical Disease Analysis system \nProject Type   :Healthcare Software \n     Developed by : Hiworth Solutions \nRole: Software Tester \n\nDescription \nIt is a website where users can search for remedies for certain diseases by entering symptoms. \nThe system performs diagnosis, by asking questions about symptoms and accepting \ncorresponding responses. Thus by getting a good initial diagnosis, users can take better \ndecision on whether to go consult a doctor or not. \nResponsibilities  \n•Done the manual testing of the website after development. \n•   Test Case Preparation based on the Requirement Criteria. \n•   Functionality Testing, Regression testing, Re-testing. (Manual) \n•   Raising and tracking Bugs. \n•   Preparation of test plans and quality reports.  \n \nAcademic Qualification \n \n\uf0d8  B.E Computer Science and Engineering from Anna University with 75% marks on  2015. \n\uf0d8  Higher Secondary Education from Girideepam Bethany Central School with 60% marks on \n\n\uf0d8  Completed Higher Secondary Education from OEM Public School with 85% marks on 2009. \n\nPersonal Profile \n\n2011. \n\n \n\n \n\nGender                    :  FemaleDate of Birth           :  12 June 1993Nationality              :  \nIndianLanguages Known  :English, Malayalam,Tamil                                                                                  \nPermanent Address :Kallelil Puthenmadom, Koipuram P.O, Chengannur.   \n\n\x0c'
    assert response.json()[
        0]["_source"]["emailAdress"] == "swapnasusan06@gmail.com"
    assert response.json()[0]["_source"]["phoneNumber"] == "+91-7034215669"


def test_cv_correct_info_only():
    response = client.get("/search_cv?q=CoreJava&contactInfoOnly=true")
    assert response.status_code == 200
    assert response.json()[
        0]["_source"]["emailAdress"] == "swapnasusan06@gmail.com"
    assert response.json()[0]["_source"]["phoneNumber"] == "+91-7034215669"
    assert response.json()[0]["_source"]["variousURL"] == ""


def route_not_found():
    response = client.get("/search_cfdvfe")
    assert response.status_code == 404

