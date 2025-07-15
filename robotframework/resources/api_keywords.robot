*** Settings ***
Library           RequestsLibrary
Resource          ../resources/api_keywords.robot
Variables         ../variables/api_variables.robot

*** Test Cases ***
Get Single User Should Return 200
    [Tags]    get    sanity
    Create Session    mysession    ${BASE_URL}
    GET User Should Be Successful    2
