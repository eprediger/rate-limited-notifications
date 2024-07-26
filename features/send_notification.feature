Feature: Send notification
  As the system
  I want to send messages to the users
  So they are up to date with the notifications

  Background:
    Given a rule with type "Status"
    And the maximum number of emails is "1"
    And this notification rule exists

  @wip
  Scenario: Successful notification
    Given the type "Status"
    And the user with id "jdoe"
    And the message "Message for John"
    When I send the notification
    And it doesn't have any previous notification sent in rule period
    Then I get a successful response with the sent notification
