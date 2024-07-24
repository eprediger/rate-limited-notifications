Feature: Notification Rule Creation
  As the system manager
  I want to create notification rules
  So that I can limit the amount of emails sent

  Scenario: New notification
    Given the type is "Status"
    And the maximum number of emails is "2"
    And the time period is "minutes"
    When I create the notification
    Then I get the notification created successfully

  Scenario Outline: Invalid notification
    Given a new notification where the key "<key_name>" has value "<value>"
    When I create the notification
    Then I get a validation error message

    Examples:
      | key_name     | value   |
      | type         | -       |
      | max_per_user | 0       |
      | period       | decades |
