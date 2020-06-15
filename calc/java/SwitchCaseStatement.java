class SwitchCaseStatement {
  public int cc = 3;

  void foo( int a ) {
    switch ( a )
    {
      case 1:
        return ;
      case 2:
      case 3:
        return ;
    }
  }
}
