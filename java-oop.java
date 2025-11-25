class Student {
    private String name;
    private int age;

    Student(String n, int a){
        this.name = n;
        this.age = a;
    }

    public String getName(){
        return name;
    }

    public int getAge(){
        return age;
    }
}

public class Main {
    public static void main(String[] args){
        Student s = new Student("Deepak", 20);
        System.out.println("Name: " + s.getName());
        System.out.println("Age: " + s.getAge());
    }
}
