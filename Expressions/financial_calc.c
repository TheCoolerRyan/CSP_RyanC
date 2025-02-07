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

//Calculate percent of rent (rent/income) -/

//Calculate percent of utilites (utilites/income) - /

//Calculate percent of grocieries (groceries/income) - /

//Calculate percent of transportation (transportation/income)- /

// Calculate percent of spending (spending/income)- /

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
printf("Hello, this is my financial calculator that will help you know what you spend your money on.\n");
printf("How much money do you earn each month?\n");
scanf("%f", &income);
printf("How much money do you spend on rent?\n");
scanf("%f", &rent);
printf("How much money do you spend on utilities?\n");
scanf("%f", &utilities);
printf("How much money do you spend on grocies?\n");
scanf("%f", &grocies);
printf("How much money do you spend on transportation?\n");
scanf("%f", &transportation);
float savings = income/90;
float spending_money= income-(rent+utilities+grocies+transportation+savings);
float percent_rent =(rent/income*100);
float percent_utilities = (utilities/income*100);
float percent_transportation = (transportation/income*100);
float percent_grocies = (grocies/income*100);
printf("The amount of money you spend on rent is"",%.2f\n",rent );
printf("The percent of money you spend on rent is" ",%.2f\n",percent_rent);
printf("The amount of money you spend on utilities is" ",%.2f\n",utilities); 
printf("The percent of money you spend on utilities is" ",%.2f\n",percent_utilities);
printf("The amount of money you spend on transportation is" ",%.2f\n", transportation);
printf("The percent of money you spend on transportation is" ",%.2f\n",percent_transportation);
printf("The amount of money you spend on grocies is" ",%.2f\n", grocies);
printf("The percent of money you spend on grocies is" ",%.2f\n",percent_grocies);
printf("The amount of money you spend on savings is" ",2f\n",savings);
printf("The amount of money you have to spend is" ",%.2f\n",spending_money);
printf("The total percent of money you have to spend is" ",%.2f\n",percent_spending_money);


    return 0;
}