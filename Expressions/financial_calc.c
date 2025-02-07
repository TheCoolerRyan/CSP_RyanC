// Ryan Crop, Financial Calculator.c
#include <stdio.h>
//Ryan Crop, Finaincal calculator.py

//Write a print statement telling the user what the program is (Bugdet calc) - \

//Ask for monthley income - \

//Ask for rent amount  - \

// Ask for utilites - \

//Ask for groceries - \

//Ask for transportation - \

// Calculate savings as 10% of income (Variable) - \

//Calculate spending money  income - (rent + utilities + grocieries + transportations + savings) (Variable) - \

//Calculate percent of rent (rent/income) -

//Calculate percent of utilites (utilites/income) -

//Calculate percent of grocieries (groceries/income) -

//Calculate percent of transportation (transportation/income)-

// Calculate percent of spending (spending/income)-

// tell user category spending amount and percent ("You spend $xx.xx on rent and that is xx% of your income") for all
float income;
float rent;
float utilities;
float grocies;
float transportation;
float percent_rent;
float percent_utilities;
float percent_grocies;
float percent_transportation;
float percent_spending_money;
int main(void){
printf("Hello, this is my financial calculator that will help you know what you spend your money on.");
printf("How much money do you earn each month?");
scanf("%f", &income);
printf("How much money do you spend on rent?");
scanf("%f", &rent);
printf("How much money do you spend on utilities?");
scanf("%f", &utilities);
printf("How much money do you spend on grocies?");
scanf("%f", &grocies);
printf("How much money do you spend on transportation?");
scanf("%f", &transportation);
float savings = income/90;
float spending_money= income-(rent+utilities+grocies+transportation+savings);
float percent_rent =(rent/income*100);
float percent_utilities = (utilities/income*100);
//printf("0.2%f")

    return 0;
}