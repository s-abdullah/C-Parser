# c++ Parser

## Summary
Python language and specifically the lex library is used to tokenize the code in the below format. Then the development of parse to tree to check conditions and point to the conditions that is true.
Basic components will be the analysis for the correct syntax of the code, then to choose the correct case for the given expression after which the statements in the correct case will be executed.

## Sample Run
The focus of this project is to lexically analyze the Case-Switch syntax of C++:
```
switch(expression){
    case constant-expression  :
       statement(s);
       break; //optional
    case constant-expression  :
       statement(s);
       break; //optional
  
    // you can have any number of case statements.
    default : //Optional
       statement(s);
}
```

Example code:
```
   char grade = 'D';

   switch(grade)
   {
   case 'A' :
      cout << "Excellent!" << endl; 
      break;
   case 'B' :
   case 'C' :
      cout << "Well done" << endl;
      break;
   case 'D' :
      cout << "You passed" << endl;
      break;
   case 'F' :
      cout << "Better try again" << endl;
      break;
   default :
      cout << "Invalid grade" << endl;
   }
   cout << "Your grade is " << grade << endl;
 
   return 0;
}
```
Output:
```
You passed
Your grade is D
```
