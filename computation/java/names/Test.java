/**
 * 5
 * */
public class Test {
  public int thisVariableCounted = 0; // 1
  public static final boolean this_variable_not_counted_too; // 2
  private double nottaken;

  public static void main(String args[]) {
    final Test1 compoundNameOne = new Test1(); // 3
    boolean COUMPOUND_NAME_TWO = false; // 4
    int nottaken = 0;
  }

  void foo() {
    String anotherOneCounted; // 5
    int a0$nottakentoo = 0;
  }
}
