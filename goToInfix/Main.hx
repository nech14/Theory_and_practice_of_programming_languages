
package;
import src.Infix;



class Main {
  static public function main() {
    Sys.println("Enter the expression in prefix notation: ");
    var line = Sys.stdin().readLine();
    var r = ~/[ ]+/g;
    var buf = r.split(line);

    var oper1 = "+-*/";
    var p = new Infix();
    Sys.println("Infix notation: " + p.prefixToInfix(oper1, buf));
  }
}






