from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from ..routers.search import es

from ..main import app

client = TestClient(app)


def test_cv_all_profile():
    es.search = MagicMock(return_value={
        "hits": {
            "hits": [
                {
                    "_index": "cv_search",
                    "_type": "cv",
                    "_id": "6cd3faf4-fd95-5a17-9e0c-7748a11cf477",
                    "_score": 1,
                    "_source": {
                        "info": "RESUME\n\nName: SONY AVARACHAN\nPhone: 9947737613\nEmail: sonyavarachan00@gmail.com\n\nCareer Objective   \n\nTo be an excellent professional and to be a part of an organization which\nprovides constant learning of latest technological upgrades, provides career\ngrowth.                                             \n\n1.\n\nB-Tech\n\nECE\n\nEducation   \n\nNo Course\n\n2.\n\n3.\n\nHSE\n\nSSLC\n\nSummary\n\nBranch/\nSubject\n\nComputer \nScience\n\nCollege/ School\n Indira Gandhi \nInstitute of \nEngineering and \nTechnology, \nNellikuzhi\n\nBoard \n/University\n\nPassing \nYear\n\n(Aggregate \n%)\n\nMahatma \nGandhi\n\n2016\n\nCGPA 6.74/10\n\nGBHSS, Aluva\n\nState\n\nHoly Family HS, \nAngamaly\n\nState\n\n2012\n\n2010\n\n80\n\n98\n\nDoing Testing Course at SPYROSYS, Kaloor (July 2016- August 2016)\n\nManual Testing Proficiency:\n\n Strong in SDLC, STLC and Defect Life Cycle.\n Knowledge on Test Plan, Traceability Matrix.\n Knowledge of writing, reviewing and executing Test Cases.\n Knowledge of writing, reviewing Bug Reports.\n Knowledge on Functional, Integration, and System Testing.\n\n\f Knowledge on Smoke, Regression, Compatibility  and various other\n\ntypes of Testing\n\nAutomation Testing (QTP) Proficiency:\n\n Knowledge on Recording options in QTP such as Checkpoint, Output \n\n Strong knowledge on Object Repository.\n Strong knowledge on Parameterization through MS Excel, Data \n\nvalues.\n\ntables, \n\nSoftware Language: Basics of C and C++ Programming.\n\nTESTING PROJECTS\n\n    Manual Testing\n    \n               The project involved testing of a software application used for Banking. By using this\nsystem it provides better convenience to management. \n\nAutomation Testing using QTP\n\n        The project involved testing of a software application used for Receipt Tracking. By using\nthis system it provides better convenience to management. \n\n Member of Red Cross in school level.\n Event organizer in school and college annual day functions and other technical events.\n\n                    \nAchievements\n\nStrengths\n\n Team Worker\n System and Operational Analysis\n Good Communication Skills\n Active learning and critical thinking\n\nPersonal Details\n\nName\n: Sony Avarachan\nFather’s Name : M V Avarachan\nGender\nDate of Birth\n\n: Female\n: 12/01/1995\n\n\fContact Address: Moozhayil H, Vappalassery P O \n                               Akaparambu, Pin: 683572\n                               Ernakulam\n\nI hereby declare that all the information mentioned above are true and correct to the best of my \nknowledge.\n                                                                                                                                 Sony Avarachan\n\n\f",
                        "emailAdress": "sonyavarachan00@gmail.com",
                        "phoneNumber": "9947737613",
                        "variousURL": ""
                    }
                },
                {
                    "_index": "cv_search",
                    "_type": "cv",
                    "_id": "83c93377-bb4d-5bae-8308-681bb57da2f1",
                    "_score": 1,
                    "_source": {
                        "info": "Kundoor House; Vallachira P.O; Thrissur; Kerala • 8593838691 • esreenath000@gmail.com\n\nSreenath E\n\nCareer Objective\n\nWith the main objective being towards satisfaction, both for myself and the company, I strive to\nwork towards the high standards of loyalty and dedication which has been consistent \nthroughout, thereby making work a pleasure.\n\nEDUCATION PROFILE\n\n Completed B.Tech in Electronics & Communication Engineering in Mala Educational \n\nTrust of Engineering, Mala.\n\n Completed 12 th grade from C.N.N.G.H.S School,Thrissur with an aggregate of 81.3%\n Completed 10 th grade from PARAMEKKAVU VIDYA MANDIR, Thrissur with an \n\naggregate of 68%\n\n Completed a certified course in Software Testing at SPYROSYS.\n\nSKILLS\n      Undergoing Testing Course at SPYROSYS,KALOOR well versed with all the concepts\nin testing.\n \n \nManual Testing Proficiency:\n \n\nØ  Strong in SDLC, STLC and Defect Life Cycle.\nØ  Knowledge on Test Plan, Tracebility Matrix.\nØ  Knowledge of writing, reviewing and executing Test Cases.\nØ  Knowledge on Functional, Integration, and System Testing.\nØ  Knowledge on Smoke, Regression, Compatibility  and various other types of\n\nTesting\n\n \nAutomation Testing(QTP) Proficiency:\n \n\nØ  Knowledge on Recording options in QTP such as Checkpoint, Output values.\n\nTECHNICAL SKILLS\n\n Knowledge in C, MATLAB and VHDL programming.\n\n\fPROJECT\n\n MINI PROJECT :\n\nTopic – ‘WIRELESS GESTURE CONTROLLED ROBOT’\nDesigned a wireless robot using microcontroller which moves in any direction according\nto the movement of our hand. \n\n MAIN PROJECT : \n\nTopic – ‘SIXTH SENCE TECHNOLOGY’\nThrough image processing and Matlab we can interact with deaf people. Also we can take \nphotos and change its properties.\n\n CERTIFICATE:\n\nPublished a paper on ‘Sixth Sense Technology’ in International Research Journal of \nEngineering and Technology (IRJET) Volume-03: Issue-03; March-2016\n\nSTRENGTHS\n\n A good communicator.\n Quick in adapting to changing environment.\n Enthusiastic\n Good in working as an individual or as a team.\n\nPERSONAL PROFILE\n        Date of birth   : 01/10/1994\n\n        Gender            : Male\n\n        Marital status   : Single\n\n        Father’s name  : Haridas P\n\n        Nationality      : Indian\n\n        Known Languages: Malayalam, English, Hindi.\n\nEXTRA CURRICULAR ACTIVITIES\n     Participated in techfest  programs in college level.\n\n    Achieved a certificate from ROBOTECH.\n\n\fDate: 21/11/2016                                                                                  Sd/-\n                                                                                                  SREENATH E   \nPlace: Thrissur\n\n\f",
                        "emailAdress": "esreenath000@gmail.com",
                        "phoneNumber": "",
                        "variousURL": ""
                    }
                }
            ]
        }
    })
    response = client.get("/search_cv")
    assert response.json() == [
        {
            "_index": "cv_search",
            "_type": "cv",
            "_id": "6cd3faf4-fd95-5a17-9e0c-7748a11cf477",
            "_score": 1,
            "_source": {
                "info": "RESUME\n\nName: SONY AVARACHAN\nPhone: 9947737613\nEmail: sonyavarachan00@gmail.com\n\nCareer Objective   \n\nTo be an excellent professional and to be a part of an organization which\nprovides constant learning of latest technological upgrades, provides career\ngrowth.                                             \n\n1.\n\nB-Tech\n\nECE\n\nEducation   \n\nNo Course\n\n2.\n\n3.\n\nHSE\n\nSSLC\n\nSummary\n\nBranch/\nSubject\n\nComputer \nScience\n\nCollege/ School\n Indira Gandhi \nInstitute of \nEngineering and \nTechnology, \nNellikuzhi\n\nBoard \n/University\n\nPassing \nYear\n\n(Aggregate \n%)\n\nMahatma \nGandhi\n\n2016\n\nCGPA 6.74/10\n\nGBHSS, Aluva\n\nState\n\nHoly Family HS, \nAngamaly\n\nState\n\n2012\n\n2010\n\n80\n\n98\n\nDoing Testing Course at SPYROSYS, Kaloor (July 2016- August 2016)\n\nManual Testing Proficiency:\n\n Strong in SDLC, STLC and Defect Life Cycle.\n Knowledge on Test Plan, Traceability Matrix.\n Knowledge of writing, reviewing and executing Test Cases.\n Knowledge of writing, reviewing Bug Reports.\n Knowledge on Functional, Integration, and System Testing.\n\n\f Knowledge on Smoke, Regression, Compatibility  and various other\n\ntypes of Testing\n\nAutomation Testing (QTP) Proficiency:\n\n Knowledge on Recording options in QTP such as Checkpoint, Output \n\n Strong knowledge on Object Repository.\n Strong knowledge on Parameterization through MS Excel, Data \n\nvalues.\n\ntables, \n\nSoftware Language: Basics of C and C++ Programming.\n\nTESTING PROJECTS\n\n    Manual Testing\n    \n               The project involved testing of a software application used for Banking. By using this\nsystem it provides better convenience to management. \n\nAutomation Testing using QTP\n\n        The project involved testing of a software application used for Receipt Tracking. By using\nthis system it provides better convenience to management. \n\n Member of Red Cross in school level.\n Event organizer in school and college annual day functions and other technical events.\n\n                    \nAchievements\n\nStrengths\n\n Team Worker\n System and Operational Analysis\n Good Communication Skills\n Active learning and critical thinking\n\nPersonal Details\n\nName\n: Sony Avarachan\nFather’s Name : M V Avarachan\nGender\nDate of Birth\n\n: Female\n: 12/01/1995\n\n\fContact Address: Moozhayil H, Vappalassery P O \n                               Akaparambu, Pin: 683572\n                               Ernakulam\n\nI hereby declare that all the information mentioned above are true and correct to the best of my \nknowledge.\n                                                                                                                                 Sony Avarachan\n\n\f",
                        "emailAdress": "sonyavarachan00@gmail.com",
                        "phoneNumber": "9947737613",
                        "variousURL": ""
            }
        },
        {
            "_index": "cv_search",
            "_type": "cv",
            "_id": "83c93377-bb4d-5bae-8308-681bb57da2f1",
            "_score": 1,
            "_source": {
                "info": "Kundoor House; Vallachira P.O; Thrissur; Kerala • 8593838691 • esreenath000@gmail.com\n\nSreenath E\n\nCareer Objective\n\nWith the main objective being towards satisfaction, both for myself and the company, I strive to\nwork towards the high standards of loyalty and dedication which has been consistent \nthroughout, thereby making work a pleasure.\n\nEDUCATION PROFILE\n\n Completed B.Tech in Electronics & Communication Engineering in Mala Educational \n\nTrust of Engineering, Mala.\n\n Completed 12 th grade from C.N.N.G.H.S School,Thrissur with an aggregate of 81.3%\n Completed 10 th grade from PARAMEKKAVU VIDYA MANDIR, Thrissur with an \n\naggregate of 68%\n\n Completed a certified course in Software Testing at SPYROSYS.\n\nSKILLS\n      Undergoing Testing Course at SPYROSYS,KALOOR well versed with all the concepts\nin testing.\n \n \nManual Testing Proficiency:\n \n\nØ  Strong in SDLC, STLC and Defect Life Cycle.\nØ  Knowledge on Test Plan, Tracebility Matrix.\nØ  Knowledge of writing, reviewing and executing Test Cases.\nØ  Knowledge on Functional, Integration, and System Testing.\nØ  Knowledge on Smoke, Regression, Compatibility  and various other types of\n\nTesting\n\n \nAutomation Testing(QTP) Proficiency:\n \n\nØ  Knowledge on Recording options in QTP such as Checkpoint, Output values.\n\nTECHNICAL SKILLS\n\n Knowledge in C, MATLAB and VHDL programming.\n\n\fPROJECT\n\n MINI PROJECT :\n\nTopic – ‘WIRELESS GESTURE CONTROLLED ROBOT’\nDesigned a wireless robot using microcontroller which moves in any direction according\nto the movement of our hand. \n\n MAIN PROJECT : \n\nTopic – ‘SIXTH SENCE TECHNOLOGY’\nThrough image processing and Matlab we can interact with deaf people. Also we can take \nphotos and change its properties.\n\n CERTIFICATE:\n\nPublished a paper on ‘Sixth Sense Technology’ in International Research Journal of \nEngineering and Technology (IRJET) Volume-03: Issue-03; March-2016\n\nSTRENGTHS\n\n A good communicator.\n Quick in adapting to changing environment.\n Enthusiastic\n Good in working as an individual or as a team.\n\nPERSONAL PROFILE\n        Date of birth   : 01/10/1994\n\n        Gender            : Male\n\n        Marital status   : Single\n\n        Father’s name  : Haridas P\n\n        Nationality      : Indian\n\n        Known Languages: Malayalam, English, Hindi.\n\nEXTRA CURRICULAR ACTIVITIES\n     Participated in techfest  programs in college level.\n\n    Achieved a certificate from ROBOTECH.\n\n\fDate: 21/11/2016                                                                                  Sd/-\n                                                                                                  SREENATH E   \nPlace: Thrissur\n\n\f",
                        "emailAdress": "esreenath000@gmail.com",
                        "phoneNumber": "",
                        "variousURL": ""
            }
        }
    ]
    assert response.status_code == 200
    assert len(response.json()) >= 2


def test_cv_not_found():
    es.search = MagicMock(return_value={
        "hits": {
            "hits": []
        }
    })
    response = client.get("/search_cv?q=jimnotexist")
    assert response.status_code == 200
    assert response.json() == []


def test_cv_corejava_profile():
    es.search = MagicMock(return_value={
        "hits": {
            "hits": [
                {
                    "_index": "cv_search",
                    "_type": "cv",
                    "_id": "20e1b6a7-9ac4-5960-a665-4d750f50d372",
                    "_score": 2.4588733,
                    "_source": {
                        "info": "    SWAPNA SUSAN JOSE \nJUNIOR SOFTWARE TEST ENGINEER \n \nPhone:+91-7034215669                                                            Email: swapnasusan06@gmail.com \n \n \nPROFILE SUMMARY \n \n  10 months of experience in Testing field as a junior test engineer. \n  Expertise  in  Manual  Testing,  Preparing  Test  cases,  Test  data’s,  Test  execution  and \n\nTracking Defects. \n\n  Have  Good  Knowledge  in  Functional,  Negative,  Regression,  System  Integration  (SIT), \n\nand User Acceptance (UAT) testing methods. \n\n  Testing all the possible situations of the application. \n  Worked in Test Planning, Designing Test Cases, Reporting and Tracking Defects. \n  Have  experience  in  working  with  different  software  development  Models  like Waterfall \n\n  Strong in Presentation, Communication and Team Skills. \n  Coping with change in the workplace, providing effective customer service  \n  Co-ordinate  with  Developers,  Testers,  individuals  involved  in  the  project  to  resolve  the \n\n  Quick learner and excellent  team  player, ability  to meet  tight  deadlines  and work under \n\nand Spiral. \n\nidentified issues. \n\npressure. \n\n \nCareer Path \n \n Worked on Hiworth Solutions as Junior Test Engineer from June 2015 to March 2016 \n \nTechnical Competencies \n \nSoftware Process/Models    : SDLC, STLC, Waterfall, Agile, Manual Testing \nOperating Systems              :   Windows10/8/9, XP \nProgramming Languages     :  C,C++,CoreJava Fundamentals, PHP \nBug Reporting Tool:Jira \nTesting Type    \nDatabase                 \nIDE              :Dreamweaver, Eclipse \nAutomation Tools  \n \nTraining and Certifications \n  Pursuing a certified course on Automation Testing  Tools – Selenium and QTP. \n \n\n:  Manual,Automation \n: My SQL \n\n:   Selenium, QTP \n\n\fProjects Summary \n\n \n\n  Silhouettes Boutique  \n\nProject Type   : E-Commerce Application \n\nDeveloped by:Hiworth Solutions \nRole: Software Tester \nDescription \nSilhouettes Boutique is an online shopping boutique which provides a unique platform to \nbring its customers contemporary on-trend pieces as well as timeless classics in a Quick and \nEasy way. Developed in such a way that the customers or anyone using the site can easily \naccess and understand the features and functionalities. \nResponsibilities \n•Done the manual testing of the website after development. \n•   Test Case Preparation based on the Requirement Criteria. \n•   Functionality Testing, Regression testing, Re-testing. (Manual) \n•   Backend Testing and products validation and verification. \n•   Raising and tracking Bugs. \n•   Preparation of test plans and quality reports. \n \n  Northeast Arkansas Federal Credit Union  \n   Project Type   : Banking Software \n      Developed by : Hiworth Solutions \nRole: Software Tester \nDescription \nNEAFCU  is a web-based reliable and flexible credit union in Arkansas which is operated by  \na volunteer board of directors and offers a full-line of services to members including flexible  \nloans, great deposits, personal member services and debit membership applications and it  \nfeatured as a great financial option to consider for both loans and savings products. \n\nResponsibilities  \n•Done the manual testing of the website  after development. \n•   Test Planning, Test case development and Test script execution skills estimation.. \n•Functionality Testing, Regression testing, Re-testing. (Manual) \n •   Bug Tracking and Reporting.  \n•Re-testing of resolved defects \n \n Arkansas School Board Association  \nProject Type   : Educational Related Software \n     Developed by : Hiworth Solutions \nRole: Software Tester \n \n \nDescription \n\n\fThe ARSBA is a private, non-profit, membership organization that provides leadership, \ntraining, advocacy & specialized services to school boards throughout Arkansas. Its \nspecialized services include board development, legal consultations, Workers compensation \ninsurance, model policy services and promote student focused leadership in Public. \nResponsibilities  \n•Done the manual testing of the website after development. \n•    Test Case Preparation based on the Requirement Criteria. \n•    Functionality Testing, Regression testing, Re-testing. (Manual) \n•    Raising and tracking Bugs. \n•    Preparation of test plans and quality reports.  \n \n\n  Automatic Medical Disease Analysis system \nProject Type   :Healthcare Software \n     Developed by : Hiworth Solutions \nRole: Software Tester \n\nDescription \nIt is a website where users can search for remedies for certain diseases by entering symptoms. \nThe system performs diagnosis, by asking questions about symptoms and accepting \ncorresponding responses. Thus by getting a good initial diagnosis, users can take better \ndecision on whether to go consult a doctor or not. \nResponsibilities  \n•Done the manual testing of the website after development. \n•   Test Case Preparation based on the Requirement Criteria. \n•   Functionality Testing, Regression testing, Re-testing. (Manual) \n•   Raising and tracking Bugs. \n•   Preparation of test plans and quality reports.  \n \nAcademic Qualification \n \n  B.E Computer Science and Engineering from Anna University with 75% marks on  2015. \n  Higher Secondary Education from Girideepam Bethany Central School with 60% marks on \n\n  Completed Higher Secondary Education from OEM Public School with 85% marks on 2009. \n\nPersonal Profile \n\n2011. \n\n \n\n \n\nGender                    :  FemaleDate of Birth           :  12 June 1993Nationality              :  \nIndianLanguages Known  :English, Malayalam,Tamil                                                                                  \nPermanent Address :Kallelil Puthenmadom, Koipuram P.O, Chengannur.   \n\n\f",
                        "emailAdress": "swapnasusan06@gmail.com",
                        "phoneNumber": "+91-7034215669",
                        "variousURL": ""
                    }
                }
            ]
        }
    })
    response = client.get("/search_cv?q=CoreJava")
    assert response.status_code == 200
    assert response.json()[0]["_source"]["info"] == '    SWAPNA SUSAN JOSE \nJUNIOR SOFTWARE TEST ENGINEER \n \nPhone:+91-7034215669                                                            Email: swapnasusan06@gmail.com \n \n \nPROFILE SUMMARY \n \n\uf0b7  10 months of experience in Testing field as a junior test engineer. \n\uf0b7  Expertise  in  Manual  Testing,  Preparing  Test  cases,  Test  data’s,  Test  execution  and \n\nTracking Defects. \n\n\uf0b7  Have  Good  Knowledge  in  Functional,  Negative,  Regression,  System  Integration  (SIT), \n\nand User Acceptance (UAT) testing methods. \n\n\uf0b7  Testing all the possible situations of the application. \n\uf0b7  Worked in Test Planning, Designing Test Cases, Reporting and Tracking Defects. \n\uf0b7  Have  experience  in  working  with  different  software  development  Models  like Waterfall \n\n\uf0b7  Strong in Presentation, Communication and Team Skills. \n\uf0b7  Coping with change in the workplace, providing effective customer service  \n\uf0b7  Co-ordinate  with  Developers,  Testers,  individuals  involved  in  the  project  to  resolve  the \n\n\uf0b7  Quick learner and excellent  team  player, ability  to meet  tight  deadlines  and work under \n\nand Spiral. \n\nidentified issues. \n\npressure. \n\n \nCareer Path \n \n\uf0b7 Worked on Hiworth Solutions as Junior Test Engineer from June 2015 to March 2016 \n \nTechnical Competencies \n \nSoftware Process/Models    : SDLC, STLC, Waterfall, Agile, Manual Testing \nOperating Systems              :   Windows10/8/9, XP \nProgramming Languages     :  C,C++,CoreJava Fundamentals, PHP \nBug Reporting Tool:Jira \nTesting Type    \nDatabase                 \nIDE              :Dreamweaver, Eclipse \nAutomation Tools  \n \nTraining and Certifications \n\uf0b7  Pursuing a certified course on Automation Testing  Tools – Selenium and QTP. \n \n\n:  Manual,Automation \n: My SQL \n\n:   Selenium, QTP \n\n\x0cProjects Summary \n\n \n\n\uf0d8  Silhouettes Boutique  \n\nProject Type   : E-Commerce Application \n\nDeveloped by:Hiworth Solutions \nRole: Software Tester \nDescription \nSilhouettes Boutique is an online shopping boutique which provides a unique platform to \nbring its customers contemporary on-trend pieces as well as timeless classics in a Quick and \nEasy way. Developed in such a way that the customers or anyone using the site can easily \naccess and understand the features and functionalities. \nResponsibilities \n•Done the manual testing of the website after development. \n•   Test Case Preparation based on the Requirement Criteria. \n•   Functionality Testing, Regression testing, Re-testing. (Manual) \n•   Backend Testing and products validation and verification. \n•   Raising and tracking Bugs. \n•   Preparation of test plans and quality reports. \n \n\uf0d8  Northeast Arkansas Federal Credit Union  \n   Project Type   : Banking Software \n      Developed by : Hiworth Solutions \nRole: Software Tester \nDescription \nNEAFCU  is a web-based reliable and flexible credit union in Arkansas which is operated by  \na volunteer board of directors and offers a full-line of services to members including flexible  \nloans, great deposits, personal member services and debit membership applications and it  \nfeatured as a great financial option to consider for both loans and savings products. \n\nResponsibilities  \n•Done the manual testing of the website  after development. \n•   Test Planning, Test case development and Test script execution skills estimation.. \n•Functionality Testing, Regression testing, Re-testing. (Manual) \n •   Bug Tracking and Reporting.  \n•Re-testing of resolved defects \n \n\uf0d8 Arkansas School Board Association  \nProject Type   : Educational Related Software \n     Developed by : Hiworth Solutions \nRole: Software Tester \n \n \nDescription \n\n\x0cThe ARSBA is a private, non-profit, membership organization that provides leadership, \ntraining, advocacy & specialized services to school boards throughout Arkansas. Its \nspecialized services include board development, legal consultations, Workers compensation \ninsurance, model policy services and promote student focused leadership in Public. \nResponsibilities  \n•Done the manual testing of the website after development. \n•    Test Case Preparation based on the Requirement Criteria. \n•    Functionality Testing, Regression testing, Re-testing. (Manual) \n•    Raising and tracking Bugs. \n•    Preparation of test plans and quality reports.  \n \n\n\uf0d8  Automatic Medical Disease Analysis system \nProject Type   :Healthcare Software \n     Developed by : Hiworth Solutions \nRole: Software Tester \n\nDescription \nIt is a website where users can search for remedies for certain diseases by entering symptoms. \nThe system performs diagnosis, by asking questions about symptoms and accepting \ncorresponding responses. Thus by getting a good initial diagnosis, users can take better \ndecision on whether to go consult a doctor or not. \nResponsibilities  \n•Done the manual testing of the website after development. \n•   Test Case Preparation based on the Requirement Criteria. \n•   Functionality Testing, Regression testing, Re-testing. (Manual) \n•   Raising and tracking Bugs. \n•   Preparation of test plans and quality reports.  \n \nAcademic Qualification \n \n\uf0d8  B.E Computer Science and Engineering from Anna University with 75% marks on  2015. \n\uf0d8  Higher Secondary Education from Girideepam Bethany Central School with 60% marks on \n\n\uf0d8  Completed Higher Secondary Education from OEM Public School with 85% marks on 2009. \n\nPersonal Profile \n\n2011. \n\n \n\n \n\nGender                    :  FemaleDate of Birth           :  12 June 1993Nationality              :  \nIndianLanguages Known  :English, Malayalam,Tamil                                                                                  \nPermanent Address :Kallelil Puthenmadom, Koipuram P.O, Chengannur.   \n\n\x0c'
    assert response.json()[
        0]["_source"]["emailAdress"] == "swapnasusan06@gmail.com"
    assert response.json()[0]["_source"]["phoneNumber"] == "+91-7034215669"


def test_cv_correct_info_only():
    es.search = MagicMock(return_value={
        "hits": {
            "hits": [{
                "_index": "cv_search",
                "_type": "cv",
                "_id": "20e1b6a7-9ac4-5960-a665-4d750f50d372",
                "_score": 2.4588733,
                "_source": {
                    "phoneNumber": "+91-7034215669",
                    "variousURL": "",
                    "emailAdress": "swapnasusan06@gmail.com"
                }
            }]
        }
    })
    response = client.get("/search_cv?q=CoreJava&contactInfoOnly=true")
    assert response.status_code == 200
    assert response.json()[
        0]["_source"]["emailAdress"] == "swapnasusan06@gmail.com"
    assert response.json()[0]["_source"]["phoneNumber"] == "+91-7034215669"
    assert response.json()[0]["_source"]["variousURL"] == ""


def test_route_not_found():
    es.search = MagicMock(return_value={
        "hits": {
            "hits": [{"detail": "Not Found"}]
        }
    })
    response = client.get("/search_cfdvfe")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
