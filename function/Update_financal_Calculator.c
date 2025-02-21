//Ryan Crop, Update Financal Calculator
#include <stdio.h>

//Write a print statement telling the user what the program is (Bugdet calc) - Done

//Ask for monthley income - Done

//Ask for rent amount  - Done

// Ask for utilites - Done

//Ask for groceries - Done

//Ask for transportation - Done

// Calculate savings as 10% of income (Variable) - 

//Caclulate amount of spending money percent)

//Calculate spending money  income - (rent + utilities + grocieries + transportations + savings) (Variable) - 

//Calculate percent of rent (rent/income) -/

//Calculate percent of utilites (utilites/income) - /

//Calculate percent of grocieries (groceries/income) - /

//Calculate percent of transportation (transportation/income)- /

// Calculate percent of spending (spending/income)- /

// tell user category spending amount and percent ("You spend $xx.xx on rent and that is xx% of your income") for all
float income [50];
float rent [50];
float utilities [50];
float groceries [50];
float transportation [50];

char user(char type[100]){
    printf("How much do you spend on %s\n", type);
    scanf("%s", &type);
    return user;
}
char main(void){
    printf("Welcome to my program, it will tell you how much you spend, what percent you spend, and  more!\n");
    printf("How much do you earn each month?\n");
    scanf("%f", &income);
user("rent?");
user("utilities?");
user("groceries?");
user("transportation?");
    return 0;
}
