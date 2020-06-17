class ElseIfStatement {
  public int cc = 3;

  public boolean checkWithdrawal() {
    boolean result = false;
    if (account.getBalance() >= amount) {
      result = true;
    } else if (account.isLocked()) {
      result = false;
    }
    return result;
  }
}
