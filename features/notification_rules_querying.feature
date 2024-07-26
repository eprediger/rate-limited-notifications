Feature: Notification Rule Querying
  As the system manager
  I want to query the notification rules
  So I can check the existent rules

  Scenario: Querying all notification rules
    Given that a notification rule exists
    When I query the notification rules
    Then I should receive them successfully
