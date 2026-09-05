class DemoClass {
    // Correct way: Add <T> before the return type to define it as a generic method
    <T> void genericPrint(T t) {
        System.out.println(t); // Changed System.err to System.out for standard output
    }

    public static void main(String[] args) {
        // Correct way: Initialize the object using the 'new' keyword
        DemoClass aobj = new DemoClass(); 

        // Calling generic method with an Integer argument (auto-boxed from int)
        aobj.genericPrint(101); 

        // Calling generic method with a String argument
        aobj.genericPrint("Joy with Java"); 

        // Calling generic method with a Double argument (auto-boxed from double)
        aobj.genericPrint(3.1412343);
    }
}
