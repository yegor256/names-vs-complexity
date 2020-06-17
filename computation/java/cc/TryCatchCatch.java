public class TryCatchCatch {
  private int cc = 4;

  void foo() {
    try {
      throw new Exception();
    } catch (RuntimeException e) {
      System.err.println("catch RuntimeException");
    } catch (Exception e) {
      System.err.println("catch Exception");
    } catch (Throwable e) {
      System.err.println("catch Throwable");
    }
    System.err.println("next statement");
  }
}
