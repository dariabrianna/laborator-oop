// MyJavaFile.java

public class MyJavaFile {
    private String name;

    public MyJavaFile(String name) {
        this.name = name;
    }

    public void greet() {
        System.out.println("Hello from " + name + "!");
    }

    public int add(int a, int b) {
        return a + b;
    }

    public void printEvenNumbers(int limit) {
        System.out.print("Even numbers up to " + limit + ": ");
        for (int i = 0; i <= limit; i += 2) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public String reverseString(String input) {
        StringBuilder reversed = new StringBuilder();
        for (int i = input.length() - 1; i >= 0; i--) {
            reversed.append(input.charAt(i));
        }
        return reversed.toString();
    }

    public static void main(String[] args) {
        MyJavaFile myFile = new MyJavaFile("MyFile");
        myFile.greet();

        int result = myFile.add(5, 7);
        System.out.println("The sum is: " + result);

        myFile.printEvenNumbers(10);

        String reversedString = myFile.reverseString("Java is fun!");
        System.out.println("Reversed String: " + reversedString);
    }

    public static void main(String[] args) {
        MyJavaFile myFile = new MyJavaFile("MyFile");
        myFile.greet();

        int result = myFile.add(5, 7);
        System.out.println("The sum is: " + result);

        myFile.printEvenNumbers(10);

        String reversedString = myFile.reverseString("Java is fun!");
        System.out.println("Reversed String: " + reversedString);
    }
}
