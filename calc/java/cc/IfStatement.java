class IfStatement {
  public int cc = 3;

  public boolean checkWithdrawal() {
    boolean result = false;
    if (account.getBalance() >= amount) {
      result = true;
    }
    if (account.isLocked()) {
      result = false;
    }
    return result;
  }
}
