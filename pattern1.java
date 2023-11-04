public class MyClass {
    public static void main(String args[]) {
      print(5);
    }
    public static void print(int size){
        
        if(size%2==0){
            System.out.println("Size must be odd for this pattern");
            return;
        }
        
        int d=1;
        int num=1;
        boolean positive=true;
        
        for(int i=0;i<size;i++){
            
            boolean printStaric=false;
            int triggerOn=(size-d)/2;
            
            for(int j=0;j<size;j++){
                if(j==triggerOn)
                    printStaric=true;
                if(printStaric){
                    System.out.print("*");
                    d--;
                    if(d==0)
                        printStaric=false;
                }else    
             System.out.print("+");
             
            }
           
            
            if(num==size)
                positive=false;
            
            if(positive)
                num+=2;
            else
                num-=2;
                
            d=num;
            System.out.println();
        }
    }
}

/*

++*++
+***+
*****
+***+
++*++

*/
