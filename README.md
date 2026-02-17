# polynomial-divider-
divides polynomials by eachother in python using long division 

PURPOSE
I want to test my python skills in preparation for the higher computing assignment and I think the problem solving of figuring out how to do it will be a fun and interesting challange
When I divide polynomials in maths class I was thinking about how it could be done in python
I also want to add extra functionality later on to analyse the results of division using graphs to maybe find patterns.
Practice modular code
Practice maths logic

BOUNDARIES 
the dividend must also be a polyunomial
the program should have an option to divide the quotient by something else 
there needs to be input validation to make sure the terms are in decending order of powers and sort them if not
if there are powers missing a new term with a coefficient of zero inserted to the original polynomial. i.e (powers = 1,4,3, coefficients = 4,8,2) ===> (powers = 4,3,2,1, coefficients = 8,2,0,1)

FUNCITONAL REQUIREMENTS  
Inputs - enters the number of terms in the dividend then the coefficient and power for each of them
       - the number of terms in the divisor and the coefficients and powers of each term  
       
Process - sort the terms by decending power
       - insert new terms as needed
       - calculate the quotient via long division
       
Outputs - the quotient and an option to restart with the new quotions as the dividend
