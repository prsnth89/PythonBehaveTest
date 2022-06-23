@login2
Feature: Login test2
 # @AUTORETRY
  @login2
  Scenario Outline: Login with valid test1
    Then enter username "<username>" and password "<password>"
    Then click login
    And verify login success
    Examples:
      | username       | password     |
      | standard_user2 | secret_sauce |
      | standard_user  | secret_sauce |

