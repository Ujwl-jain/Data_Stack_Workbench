using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CSharpLearning.Topics;


namespace CSharpLearning
{
    class Program
    {
        //THIS IS comment

        /*
         this is a multi line comment
        */

        static void Main(string[] args)
        {
            /*
             Data types:
            1. Integer - int that
            2. Float - float this
            3. char - char name = 'Ujjwal'
            4. Boolean - bool isGreat= true;
            5.string - string naming = 'Ujjwal'
            6. Long - long num
            7. Double - double that
            */

            //int num = 34;

            // this return the string, it will contain everythin which is in readline and
            // returns as string whether it is integer, float, it will retur as string
            // readline  will ask me for a input and write line will write it
            string naming = Console.ReadLine();
            Console.WriteLine(naming);


            /*
             Data Types example
            for float and double we may need to apply a specifc suffix in this at it will show the error for flot
            for double its fine to leave it but recommended to add the suffix
             */
            int a = 32;
            float b = 34.5F;
            double c = 34.5D;
            bool isgreat = true;
            char d = 'r';
            string e = "This is a string";
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
            Console.WriteLine(isgreat);
            Console.WriteLine(d);
            Console.WriteLine(e);

            /*
             Type casting

            two types of type casting
            1. implicit: 
            Promotion order: char to int to long to float to double

            In the below scenario, x can be converted into double y, but double y can not convert into int
            As for int z = 'y', string converts into int in a way it stores its ASCII Value inside the variable
            
             2. explicit casting
             */
            int ab = (int)3.5;
            int x = 3;
            double y = x;
            int z = 'y';

            Console.WriteLine(ab);
            Console.WriteLine(x);
            Console.WriteLine(y);
            Console.WriteLine(z);
            Console.ReadLine();

            UserInput.Run();

            Console.ReadLine();
            Console.ReadKey();
        }
    }
}
