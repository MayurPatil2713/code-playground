class SpecificArrayInt {
    // Declaring an array of integer numbers
    int a[];

    // Constructor to load the array
    SpecificArrayInt(int a[]) {
        this.a = a;
    }

    // Method to print the array elements
    void printInt() {
        for(int x : a)
            System.out.println(x + " ");
        System.out.println();
    }

    // Method to reverse the array elements
    void reverseInt() {
        int i = 0;
        int j = a.length - 1;
        while(i < j)
        {
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i++;
            j--;
        } // End of for-loop
    } // end of method
} // end of class

class MainClassInt {
    public static void main(String[] args) {
        //This class use the class SpecificArrayInt to manipulate data in it
        
        int[] data = {1,2,3,4,5};
        SpecificArrayInt obj = new SpecificArrayInt(data);
        
        System.out.print("Original array: ");
        obj.printInt();
        obj.reverseInt();
        System.out.print("Reversed array: ");
        obj.printInt();
    }
}
