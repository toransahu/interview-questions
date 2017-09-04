abstract class Demo
                        {
                            public int a;
                            Demo()
                            {
                                a = 10;
                            }
                         
                            abstract public void set();
                             
                             
                            //abstract final public void get(); //this is wrong, we can't make it final if class is abstract
                            abstract  public void get(); //this is correct
                         
                        }
           