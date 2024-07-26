Feature: Send notification
  As the system
  I want to send messages to the users
  So they are up to date with the notifications

  Background:
    Given a rule with type "Status"
    And the maximum number of emails is "1"
    And this notification rule exists
    And the type "Status"
    And the user with id "jdoe"
    And the message "Message for John"

  Scenario: Successful notification
    When I send the notification
    And it has no prior notification sent within the rule period
    Then I get a successful response with the sent notification

  Scenario: Rate-limit exceeded
    Given it has a prior notification sent
    When I send the notification
    Then I get an erroneous response for exceeding the rate limit
