Feature: Functional door

  Scenario: Open the door
     Given the door is closed
      When open the door
      Then the door is open 