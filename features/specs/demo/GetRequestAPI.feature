@API
Feature: Get request

  @APIGetReq @noGui
  Scenario: validate get request
    Given hit the given url
    Then verify the success response from url
