class Cheating {
  public int cc = 1;

  public boolean checkWithdrawal(Account account, int amount) {
    boolean result = true;
    result &= account.getBalance() >= amount;
    result &= !account.isLocked();
    return result;
  }
}
