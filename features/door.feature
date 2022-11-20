Feature: Functional door

  Scenario: Customer wants to open the door
     Given the door is closed
      When open the door
      Then the door is open 