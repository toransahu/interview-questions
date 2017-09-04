class Test extends Demo
{
	//this missing definition is required
	public void set()
    {
        
    }
	
	//this will not going to fulfill the concept of abstract class
    public void set(int a)
    {
        this.a = a;
    }
 
    final public void get()
    {
        System.out.println("a = " + a);
    }
 
    public static void main(String[] args)
    {
        Test obj = new Test();
        obj.set(20);
        obj.get();
    }
}