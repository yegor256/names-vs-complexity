public class ForStatement {
  public int cc = 2;

  public int sum(int[] amounts) {
    int result = 0;
    for (int i = 0; i < amounts.length; i++) {
      result += amounts[i];
    }
    return result;
  }
}
