package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  private static VendingMachine instance; // Store the instance

  private int balanceInCents;

  private VendingMachineImpl() {
    this.balanceInCents = 0;
  }

  // Unique instance of VendingMachine static method
  public static VendingMachine getInstance() {
    if (instance == null) {
      instance = new VendingMachineImpl();
    }
    return instance;
  }

  @Override
  public void insertQuarter() {
    // Inser 25 cents in VendingMachine
    balanceInCents += 25;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    if (name.equals("ScottCola")) {
      if (balanceInCents >= 75) {
        balanceInCents -= 75;
        return new Drink() {
          @Override
          public String getName() {
            return "ScottCola";
          }

          @Override
          public boolean isFizzy() {
            return true;
          }
        };
      } else {
        throw new NotEnoughMoneyException();
      }
    } else if (name.equals("KarenTea")) {
      if (balanceInCents >= 100) {
        balanceInCents -= 100;
        return new Drink() {
          @Override
          public String getName() {
            return "KarenTea";
          }

          @Override
          public boolean isFizzy() {
            return false;
          }
        };
      } else {
        throw new NotEnoughMoneyException();
      }
    } else {
      throw new UnknownDrinkException();
    }
  }
}

