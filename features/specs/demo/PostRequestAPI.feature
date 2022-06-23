@API
Feature: post request

  @APIGetReq
  Scenario: validate post request
    Given post the body
    Then validate the response code


