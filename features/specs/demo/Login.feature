@login1
Feature: Login test1
 # @AUTORETRY
  @login1
  Scenario Outline: Login with valid test1
    Then enter username "<username>" and password "<password>"
    Then click login
    And verify login success
    Examples:
      | username       | password     |
      | standard_user1 | secret_sauce |
      | standard_user  | secret_sauce |


