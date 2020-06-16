class LogicAndOperator {
  public int cc = 3;

  public boolean checkWithdrawal(Account acc, int amount) {
    if (!acc.isLocked() && acc.getBalance() >= amount) {
      return true;
    }
    return false;
  }
}
