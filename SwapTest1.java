// A simple generic wrapper class to hold our values
class Wrapper<T> {
    T value;
    Wrapper(T value) {
        this.value = value;
    }
}

class SwapTest1 {
    // Correctly defined generic swap method passing the wrappers
    public static <T> void swap(Wrapper<T> x, Wrapper<T> y) {
        T temp = x.value;
        x.value = y.value;
        y.value = temp;
    }
    public static void main(String[] args) {
        // Wrap our integers
        Wrapper<Integer> x = new Wrapper<>(99);
        Wrapper<Integer> y = new Wrapper<>(66);

        System.out.println("Before swap: x = " + x.value + " " + "y = " + y.value);

        // Pass wrappers to the swap method
        swap(x,y);

        System.out.println("After swap: x = " + x.value + " " + "y = " + y.value);
    }
}