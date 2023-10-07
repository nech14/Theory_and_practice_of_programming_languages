package com;
import haxe.ds.GenericStack;


class Infix {


    public function new()
	{
	}
    

    public function start(line:String) {
        var r = ~/[ ]+/g;
        var buf = r.split(line);

        var oper = "+-*/";
        return prefixToInfix(oper, buf);
    }


    public function prefixToInfix(oper:String, buf:Array<String>):String{
    
        buf.reverse();
        
        var stack = new GenericStack<String>();
        var str:String = "";
        var k:Int, x:String, x1:String;
        
        for (i in buf){
            if(i == "")
                continue;
            k = oper.indexOf(i);
            switch(k){
                case v if (v >= 0):
                    x = stack.first();
                    stack.pop();
                    x1 = stack.first();
                    stack.pop();
                    switch(i){
                        case "*"|"/" :
                            if(StringTools.contains(x, "+") || StringTools.contains(x, "-")){
                                x = "("+ x + ")";
                            }
                            if(StringTools.contains(x1, "+") || (StringTools.contains(x1, "-"))){
                                x1 = "("+ x1 + ")";
                            }
                            str = x + i + x1;
                        case v if (x1 == null):

                            x = "("+ x + ")";                            
                            str = i + x;
                        
                        case _ :
                            str = x + i + x1;
                    }
                    stack.add(str);
                case _:
                    stack.add(i);
            }
        }
        return str;
    }
}






