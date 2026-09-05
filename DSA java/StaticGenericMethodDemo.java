class StaticGenericMethodDemo {
    // Defining a static generic method to print any data type
    static <T> void genericPrint (T t) {
        //The following statement print which type parameter T this method is handling
        System.out.println(t.getClass().getName() + ":" + t);
    }

    public static void main(String[] args) {
        genericPrint(101);  // Calling generic method with integer argument
        genericPrint("Joy with Java");  // Calling generic method with String argument
        genericPrint(3.1412343);  // Calling generic method with double argument
    }
}
