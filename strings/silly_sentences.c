//Ryan Crop, Silly Sentences C
#include <stdio.h>
//string variables for my user inputs (at lest 3)  Ask for verb, ajective, person, food -
char name[20];
char verb[20];
char adjective[20];
char person[20];
char food[20];
int main(void){
// Give them a printf satatement telling them what the program does.
printf("What is your name?");
scanf("%s",name);
printf("Hello %s, this is a program where I will ask you for certain things and then put your awnsers into a funny sentence.\n", name);
printf("First off, %s, pick a random verb.(Please only type the verb and include it ending with ing)",name);
scanf("%s",verb);
printf("For the second question, what is your favroite ajective.(Please only type the adjective)\n");
scanf("%s",adjective);
printf("Next please tell me your favroite persons name. (Only there first name.)\n");
scanf("%s",person);
printf("And finally, type a random food you like.(Please only put a food thats name is only one word and make it singular)\n");
scanf("%s",food);
printf("And now, the results of this relentless questioning is the sentence...\n");
printf("While I was %s I acidently ran into a %s version of %s and %s was eating a %s while %s upside down!",verb, adjective,person,person,food,verb);
//create user inputs (print statements with questions AND scanf to collect the info)

//insert variables into the sentence to show the user (print statement, only 1): "Hello %s", name
    return 0;
}