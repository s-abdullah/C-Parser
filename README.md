# c++ Parser
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
